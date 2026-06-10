"""Configuration + shared headless-Claude helper.

Loads .env, exposes API keys, and provides claude_json(): one place where
every `claude -p` subprocess call happens.
"""
import json
import os
import re
import subprocess

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "")
# Image model id, verified against OpenAI docs (June 2026). Override in .env if needed.
IMAGE_MODEL = os.getenv("IMAGE_MODEL", "gpt-image-2")

# Common directories used across modules.
STYLES_DIR = os.path.join(BASE_DIR, "templates", "styles")
FONTS_DIR = os.path.join(BASE_DIR, "assets", "fonts")
FACES_DIR = os.path.join(BASE_DIR, "assets", "faces")
BACKGROUNDS_DIR = os.path.join(BASE_DIR, "assets", "backgrounds")
CHANNELS_DIR = os.path.join(BASE_DIR, "assets", "channels")
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
CTR_GUIDE_PATH = os.path.join(BASE_DIR, "references", "thumbnail-ctr-guide.md")

for d in (FONTS_DIR, FACES_DIR, BACKGROUNDS_DIR, CHANNELS_DIR, PROJECTS_DIR, OUTPUTS_DIR):
    os.makedirs(d, exist_ok=True)


class ConfigError(Exception):
    """Raised when a required API key is missing. Message is user-readable."""


def require_openai():
    if not OPENAI_API_KEY:
        raise ConfigError(
            "OPENAI_API_KEY is missing. Add it to viral-thumbnail-studio/.env "
            "(get one at https://platform.openai.com/api-keys).")
    return OPENAI_API_KEY


def require_serpapi():
    if not SERPAPI_API_KEY:
        raise ConfigError(
            "SERPAPI_API_KEY is missing. Add it to viral-thumbnail-studio/.env "
            "(get one at https://serpapi.com/manage-api-key).")
    return SERPAPI_API_KEY


def ctr_guide_rules(max_chars=4000):
    """Key rules from the vendored CTR guide, trimmed to keep prompts small."""
    try:
        with open(CTR_GUIDE_PATH) as f:
            return f.read()[:max_chars]
    except OSError:
        return "(CTR guide not available)"


def _claude_env():
    """Subprocess env for claude -p. Strips ANTHROPIC_API_KEY so calls bill
    to the user's Claude subscription, never an API key."""
    env = dict(os.environ)
    if env.pop("ANTHROPIC_API_KEY", None):
        print("WARNING: ANTHROPIC_API_KEY was set; ignoring it for claude -p "
              "calls so usage bills to your Claude subscription.")
    return env


def _strip_fences(text):
    """Remove markdown code fences Claude sometimes adds despite instructions."""
    text = text.strip()
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        return match.group(1)
    # Also tolerate prose before/after a JSON object or array.
    match = re.search(r"(\{.*\}|\[.*\])", text, re.DOTALL)
    return match.group(1) if match else text


def claude_raw(prompt, timeout=600):
    """Run `claude -p <prompt> --output-format json` and return its text result."""
    result = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "json"],
        capture_output=True, text=True, timeout=timeout, env=_claude_env())
    if result.returncode != 0:
        raise RuntimeError(f"claude -p failed: {result.stderr.strip()[:500]}")
    outer = json.loads(result.stdout)
    return outer.get("result", "")


def claude_json(prompt, timeout=600):
    """Ask Claude for raw JSON; strip fences defensively; retry once on parse failure."""
    prompt = prompt + "\n\nRespond with ONLY raw JSON. No markdown, no code fences, no commentary."
    text = claude_raw(prompt, timeout)
    try:
        return json.loads(_strip_fences(text))
    except (json.JSONDecodeError, ValueError):
        retry = (prompt + "\n\nYour previous reply was not valid JSON. "
                 "Reply again with strictly valid raw JSON and nothing else.")
        text = claude_raw(retry, timeout)
        return json.loads(_strip_fences(text))
