/* Shared Fabric.js editor for create.html and analyze.html.
 *
 * Usage:  const ed = ThumbEditor.mount(document.querySelector('#editor-root'));
 *         ed.loadLayers(layerSpec);   // spec from /compose, /generate, /analyze/remake
 *
 * Canvas is 1280x720 internally and zoomed to fit its container.
 */
const ThumbEditor = (() => {
  const W = 1280, H = 720;

  // Text regions must match compose.py TEXT_REGIONS (fractions of the canvas).
  const TEXT_REGIONS = {
    'left':         [0.04, 0.50, 0.55, 'middle', 'left'],
    'right':        [0.41, 0.50, 0.55, 'middle', 'right'],
    'top':          [0.04, 0.10, 0.92, 'top', 'center'],
    'bottom':       [0.04, 0.97, 0.92, 'bottom', 'center'],
    'top-left':     [0.04, 0.06, 0.55, 'top', 'left'],
    'bottom-right': [0.41, 0.96, 0.55, 'bottom', 'right'],
  };

  const EXTRA_PROPS = ['meta', 'selectable', 'evented', 'lockMovementX', 'lockMovementY'];

  function el(tag, attrs = {}, html = '') {
    const node = document.createElement(tag);
    Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, v));
    if (html) node.innerHTML = html;
    return node;
  }

  function status(msg, isError = false, busy = false) {
    const bar = document.querySelector('#status-bar');
    if (!bar) return;
    const text = bar.querySelector('#status-text');
    if (text) text.textContent = msg; else bar.textContent = msg;
    bar.className = 'show' + (isError ? ' error' : '') + (busy ? ' busy' : '');
    if (!msg) bar.className = '';
  }

  async function api(path, body) {
    const resp = await fetch(path, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    const data = await resp.json();
    if (!resp.ok) throw new Error(data.error || resp.statusText);
    return data;
  }

  // Load fonts from assets/fonts so Fabric + the font picker can use them.
  async function loadFonts() {
    const families = ['Arial', 'Impact'];
    try {
      const data = await (await fetch('/fonts/list')).json();
      for (const file of data.fonts) {
        const family = file.replace(/\.(ttf|otf)$/i, '').replace(/[-_]/g, ' ');
        const face = new FontFace(family, `url(/assets/fonts/${encodeURIComponent(file)})`);
        await face.load().catch(() => null);
        document.fonts.add(face);
        families.push(family);
      }
    } catch (e) { /* fonts are optional; system fonts still work */ }
    return families;
  }

  function mount(root) {
    root.innerHTML = `
      <div class="ed-wrap">
        <div class="ed-toolbar">
          <button data-act="text" title="Add text">＋ Text</button>
          <button data-act="circle" title="Add highlight circle">◯ Circle</button>
          <button data-act="arrow" title="Add arrow">➜ Arrow</button>
          <button data-act="badge" title="Add badge">🏷 Badge</button>
          <label class="btn" title="Add an image layer">🖼 Image<input type="file" data-act="image" accept="image/*" hidden></label>
          <label><input type="checkbox" data-act="image-cutout" checked> remove bg on add</label>
          <span class="sep"></span>
          <button data-act="undo" title="Ctrl+Z">↩ Undo</button>
          <button data-act="redo" title="Ctrl+Shift+Z">↪ Redo</button>
          <button data-act="duplicate" title="Ctrl+D">⧉ Duplicate</button>
          <button data-act="fliph" title="Mirror the selected object">⇋ Flip H</button>
          <button data-act="delete" title="Delete / Backspace">✕ Delete</button>
          <span class="sep"></span>
          <button data-act="export" class="primary">⬇ Export PNG</button>
          <button data-act="save-template">Save Template</button>
          <button data-act="save-project">Save Project</button>
          <select data-act="projects"><option value="">Open project…</option></select>
        </div>
        <div class="ed-main">
          <div>
            <div class="ed-canvas-box"><canvas></canvas></div>
            <div class="mobile-preview">
              <img alt="mobile preview">
              <div class="cap">Mobile preview — how it looks in the YouTube sidebar (168px)</div>
            </div>
          </div>
          <div class="ed-side">
            <h4>Layers</h4>
            <ul class="ed-layers"></ul>
            <h4>Selected object</h4>
            <div class="ed-props">
              <label>Font <select data-prop="fontFamily"></select></label>
              <div class="row2">
                <label>Size <input type="number" min="8" max="400" data-prop="fontSize"></label>
                <label>Opacity <input type="range" min="0" max="100" value="100" data-prop="opacity"></label>
              </div>
              <div class="row2">
                <label>Fill <input type="color" data-prop="fill" value="#ffffff"></label>
                <label>Stroke <input type="color" data-prop="stroke" value="#000000"></label>
              </div>
              <label>Stroke width <input type="range" min="0" max="20" data-prop="strokeWidth"></label>
              <label><input type="checkbox" data-prop="allcaps"> ALL CAPS</label>
            </div>
            <h4>Background</h4>
            <div class="ed-bg">
              <label>Pan X <input type="range" min="-400" max="400" value="0" data-bg="shift_x"></label>
              <label>Darken <input type="range" min="0" max="100" data-bg="darken"></label>
              <label>Saturation <input type="range" min="0" max="200" data-bg="saturation"></label>
              <button data-act="bg-apply">Apply to background</button>
              <label><input type="checkbox" data-act="bg-lock" checked> background locked</label>
            </div>
            <h4>Style</h4>
            <select data-act="style"><option value="">Re-apply a style…</option></select>
            <h4>Describe a change</h4>
            <textarea data-act="freeform-text" rows="3"
              placeholder="e.g. make the text yellow and move my face left"></textarea>
            <button data-act="freeform">Apply with AI</button>
          </div>
        </div>
      </div>`;

    const canvasEl = root.querySelector('canvas');
    const canvas = new fabric.Canvas(canvasEl, {
      width: W, height: H, preserveObjectStacking: true, backgroundColor: '#101010',
    });

    const ed = {
      canvas, root, history: [], future: [], suspendHistory: false,
      fontFamilies: ['Arial', 'Impact'], styles: [], lastExport: null,
      onExport: null,  // pages can hook this (analyze.html: "rate my remake")
    };

    fitToContainer(ed);
    window.addEventListener('resize', () => fitToContainer(ed));
    wireHistory(ed);
    wireSnapGuides(ed);
    wireToolbar(ed);
    wireSidePanel(ed);
    wireKeyboard(ed);
    wireMobilePreview(ed);
    refreshProjects(ed);

    loadFonts().then(families => {
      ed.fontFamilies = families;
      const sel = root.querySelector('[data-prop=fontFamily]');
      sel.innerHTML = families.map(f => `<option>${f}</option>`).join('');
    });
    fetch('/styles').then(r => r.json()).then(d => {
      ed.styles = d.styles;
      const sel = root.querySelector('[data-act=style]');
      d.styles.forEach(s => sel.append(el('option', { value: s.id }, s.name)));
    });

    canvas.on('selection:created', () => syncProps(ed));
    canvas.on('selection:updated', () => syncProps(ed));
    canvas.on('object:modified', () => refreshLayers(ed));
    return ed;
  }

  function fitToContainer(ed) {
    const box = ed.root.querySelector('.ed-canvas-box');
    // box is 0-wide while its section is still hidden — keep zoom sane then.
    const zoom = box.clientWidth > 50 ? Math.min(1, (box.clientWidth - 4) / W) : 1;
    ed.zoom = zoom;
    ed.canvas.setZoom(ed.zoom);
    ed.canvas.setDimensions({ width: W * ed.zoom, height: H * ed.zoom });
  }

  // ---- loading a composed layer spec ------------------------------------

  function loadImage(url) {
    return new Promise((resolve, reject) =>
      fabric.Image.fromURL(url, (img, isError) =>
        (isError || !img) ? reject(new Error('image load failed: ' + url)) : resolve(img),
        { crossOrigin: 'anonymous' }));
  }

  async function loadLayers(ed, spec) {
    const c = ed.canvas;
    fitToContainer(ed);  // the section may have just become visible
    ed.suspendHistory = true;
    c.clear();
    c.backgroundColor = '#101010';

    for (const layer of spec.layers) {
      if (layer.type === 'background') {
        const img = await loadImage(layer.rendered_src || layer.src);
        img.scaleToWidth(W);
        img.set({
          left: 0, top: 0, selectable: false, evented: false,
          meta: { kind: 'background', src: layer.src, treatment: layer.treatment,
                  darken: layer.darken, shift_x: layer.shift_x, saturation: layer.saturation },
        });
        c.add(img);
      } else if (layer.type === 'face') {
        const img = await loadImage(layer.src);
        const scale = (H * layer.height_frac) / img.height;
        img.scale(scale);
        const w = img.width * scale;
        let left = layer.anchor === 'right' ? W - w + layer.x_bleed_px
                 : layer.anchor === 'left' ? -layer.x_bleed_px : (W - w) / 2;
        img.set({
          left, top: H - img.height * scale,
          shadow: layer.drop_shadow ? new fabric.Shadow({ color: 'rgba(0,0,0,0.55)', blur: 22, offsetX: -10, offsetY: 8 }) : null,
          meta: { kind: 'face', src: layer.src },
        });
        c.add(img);
      } else if (layer.type === 'extra') {
        addExtra(ed, layer);
      } else if (layer.type === 'text') {
        addTextLayer(ed, layer);
      }
    }
    c.renderAll();
    ed.suspendHistory = false;
    pushHistory(ed);
    refreshLayers(ed);
    syncBgSliders(ed);
  }

  function textRegion(position) {
    const [rx, ry, rw, vAnchor, align] = TEXT_REGIONS[position] || TEXT_REGIONS.left;
    return { x: rx * W, y: ry * H, width: rw * W, vAnchor, align };
  }

  function addTextLayer(ed, layer) {
    const r = textRegion(layer.position);
    const tb = new fabric.Textbox(layer.value || 'TEXT', {
      left: r.x, width: r.width, fontFamily: mapFont(ed, layer.font),
      fontSize: layer.start_size, fill: layer.fill, stroke: layer.stroke,
      strokeWidth: layer.stroke_width, paintFirst: 'stroke',
      textAlign: r.align, fontWeight: 'bold', lineHeight: 1.05,
      meta: { kind: 'text', position: layer.position, accent_bar: !!layer.accent_bar },
    });
    shrinkToFit(tb, layer.max_lines || 2);
    tb.top = r.vAnchor === 'middle' ? r.y - tb.height / 2
           : r.vAnchor === 'bottom' ? r.y - tb.height : r.y;
    ed.canvas.add(tb);
    if (layer.accent_bar) {
      const bar = new fabric.Rect({
        left: tb.left - 22, top: tb.top + 6, width: 14, height: tb.height - 12,
        fill: layer.fill, meta: { kind: 'extra', shape: 'accent_bar' },
      });
      ed.canvas.add(bar);
    }
  }

  function shrinkToFit(tb, maxLines) {
    // mirror compose.py: shrink font until the wrap fits max_lines
    while (tb.fontSize > 24 && tb._splitTextIntoLines(tb.text).lines.length > maxLines) {
      tb.set('fontSize', Math.floor(tb.fontSize * 0.92));
      tb.initDimensions();
    }
  }

  function mapFont(ed, name) {
    const hit = ed.fontFamilies.find(f => f.toLowerCase().includes((name || '').toLowerCase()));
    return hit || 'Impact';
  }

  function addExtra(ed, layer) {
    const c = ed.canvas;
    const shape = layer.shape || layer.type;
    if (shape === 'circle') {
      c.add(new fabric.Circle({
        left: layer.x_frac * W - layer.r_frac * W, top: layer.y_frac * H - layer.r_frac * W,
        radius: layer.r_frac * W, fill: 'transparent',
        stroke: layer.stroke || '#FF2A2A', strokeWidth: layer.stroke_width || 10,
        meta: { kind: 'extra', shape: 'circle' },
      }));
    } else if (shape === 'arrow') {
      c.add(makeArrow(layer.from[0] * W, layer.from[1] * H, layer.to[0] * W, layer.to[1] * H,
                      layer.fill || '#FF2A2A', layer.width || 24));
    } else if (shape === 'badge') {
      const r = (layer.size_frac || 0.15) * H;
      const cx = layer.x_frac * W, cy = layer.y_frac * H;
      const circle = new fabric.Circle({ radius: r, fill: layer.fill || '#E60000',
        originX: 'center', originY: 'center' });
      const label = new fabric.Text(layer.label || '!', {
        fontSize: r, fontFamily: 'Impact', fill: layer.text_fill || '#fff',
        originX: 'center', originY: 'center' });
      c.add(new fabric.Group([circle, label], {
        left: cx - r, top: cy - r, meta: { kind: 'extra', shape: 'badge' } }));
    } else if (shape === 'banner') {
      const y = (layer.y_frac || 0) * H, bh = (layer.height_frac || 0.12) * H;
      const rect = new fabric.Rect({ width: W, height: bh, fill: layer.fill || '#C00000' });
      const label = new fabric.Text(layer.label || '', {
        fontSize: bh * 0.72, fontFamily: 'Impact', fill: layer.text_fill || '#fff',
        left: W * 0.03, top: bh * 0.12 });
      c.add(new fabric.Group([rect, label], {
        left: 0, top: y, meta: { kind: 'extra', shape: 'banner' } }));
    }
  }

  function makeArrow(x1, y1, x2, y2, fill, width) {
    const angle = Math.atan2(y2 - y1, x2 - x1);
    const head = width * 2.4;
    const sx = x2 - head * Math.cos(angle), sy = y2 - head * Math.sin(angle);
    const line = new fabric.Line([x1, y1, sx, sy], { stroke: fill, strokeWidth: width });
    const tri = new fabric.Polygon([
      { x: x2, y: y2 },
      { x: x2 - head * Math.cos(angle - 0.45), y: y2 - head * Math.sin(angle - 0.45) },
      { x: x2 - head * Math.cos(angle + 0.45), y: y2 - head * Math.sin(angle + 0.45) },
    ], { fill });
    return new fabric.Group([line, tri], { meta: { kind: 'extra', shape: 'arrow' } });
  }

  // ---- keyboard shortcuts ---------------------------------------------------

  function typingSomewhere(ed) {
    const tag = document.activeElement?.tagName;
    return tag === 'INPUT' || tag === 'TEXTAREA' || document.activeElement?.isContentEditable
      || ed.canvas.getActiveObject()?.isEditing;  // fabric inline text edit
  }

  function wireKeyboard(ed) {
    document.addEventListener('keydown', e => {
      if (typingSomewhere(ed)) return;
      const obj = ed.canvas.getActiveObject();
      const mod = e.ctrlKey || e.metaKey;
      if (mod && e.key.toLowerCase() === 'z') {
        e.preventDefault();
        e.shiftKey ? redo(ed) : undo(ed);
      } else if (mod && e.key.toLowerCase() === 'y') {
        e.preventDefault(); redo(ed);
      } else if (mod && e.key.toLowerCase() === 'd') {
        e.preventDefault(); duplicate(ed);
      } else if ((e.key === 'Delete' || e.key === 'Backspace') && obj) {
        e.preventDefault();
        ed.canvas.remove(obj); ed.canvas.discardActiveObject(); refreshLayers(ed);
      } else if (e.key.startsWith('Arrow') && obj) {
        e.preventDefault();
        const step = e.shiftKey ? 10 : 1;
        if (e.key === 'ArrowLeft') obj.left -= step;
        if (e.key === 'ArrowRight') obj.left += step;
        if (e.key === 'ArrowUp') obj.top -= step;
        if (e.key === 'ArrowDown') obj.top += step;
        obj.setCoords(); ed.canvas.renderAll();
      }
    });
  }

  function duplicate(ed) {
    const obj = ed.canvas.getActiveObject();
    if (!obj || obj.meta?.kind === 'background') return;
    obj.clone(copy => {
      copy.set({ left: obj.left + 24, top: obj.top + 24, meta: { ...(obj.meta || {}) } });
      ed.canvas.add(copy);
      ed.canvas.setActiveObject(copy);
      refreshLayers(ed);
    }, EXTRA_PROPS);
  }

  // ---- live mobile-size preview ----------------------------------------------

  function wireMobilePreview(ed) {
    const img = ed.root.querySelector('.mobile-preview img');
    let pending = null;
    ed.canvas.on('after:render', () => {
      if (pending) return;            // throttle: at most ~2 updates/sec
      pending = setTimeout(() => {
        pending = null;
        try {
          img.src = ed.canvas.toDataURL({
            format: 'jpeg', quality: 0.8,
            multiplier: 336 / (W * ed.zoom),  // 2x of the 168px display size
          });
        } catch (e) { /* tainted canvas etc — preview is best-effort */ }
      }, 450);
    });
  }

  // ---- history (undo/redo) ------------------------------------------------

  function wireHistory(ed) {
    const push = () => { if (!ed.suspendHistory) pushHistory(ed); };
    ed.canvas.on('object:added', push);
    ed.canvas.on('object:removed', push);
    ed.canvas.on('object:modified', push);
  }

  function pushHistory(ed) {
    ed.history.push(JSON.stringify(ed.canvas.toJSON(EXTRA_PROPS)));
    if (ed.history.length > 60) ed.history.shift();
    ed.future = [];
  }

  function restore(ed, json) {
    ed.suspendHistory = true;
    ed.canvas.loadFromJSON(json, () => {
      ed.canvas.renderAll();
      ed.suspendHistory = false;
      refreshLayers(ed);
    });
  }

  function undo(ed) {
    if (ed.history.length < 2) return;
    ed.future.push(ed.history.pop());
    restore(ed, ed.history[ed.history.length - 1]);
  }

  function redo(ed) {
    if (!ed.future.length) return;
    const json = ed.future.pop();
    ed.history.push(json);
    restore(ed, json);
  }

  // ---- snap-to-center guides ----------------------------------------------

  function wireSnapGuides(ed) {
    const c = ed.canvas;
    let vLine = null, hLine = null;
    const guideOpts = { stroke: '#00d4ff', strokeWidth: 2, selectable: false, evented: false, excludeFromExport: true };
    c.on('object:moving', e => {
      const obj = e.target;
      const cx = obj.left + obj.getScaledWidth() / 2;
      const cy = obj.top + obj.getScaledHeight() / 2;
      if (vLine) { c.remove(vLine); vLine = null; }
      if (hLine) { c.remove(hLine); hLine = null; }
      if (Math.abs(cx - W / 2) < 12) {
        obj.set('left', W / 2 - obj.getScaledWidth() / 2);
        vLine = new fabric.Line([W / 2, 0, W / 2, H], guideOpts);
        c.add(vLine);
      }
      if (Math.abs(cy - H / 2) < 12) {
        obj.set('top', H / 2 - obj.getScaledHeight() / 2);
        hLine = new fabric.Line([0, H / 2, W, H / 2], guideOpts);
        c.add(hLine);
      }
    });
    c.on('mouse:up', () => {
      if (vLine) { c.remove(vLine); vLine = null; }
      if (hLine) { c.remove(hLine); hLine = null; }
    });
  }

  // ---- layers panel ----------------------------------------------------------

  function refreshLayers(ed) {
    const list = ed.root.querySelector('.ed-layers');
    list.innerHTML = '';
    const objects = ed.canvas.getObjects().filter(o => !o.excludeFromExport);
    [...objects].reverse().forEach(obj => {  // top-most first
      const li = el('li', { draggable: 'true' });
      const name = obj.meta?.kind === 'background' ? 'Background'
        : obj.meta?.kind === 'face' ? 'Face'
        : obj.type === 'textbox' ? `Text: ${obj.text.slice(0, 14)}`
        : obj.meta?.shape ? `Extra: ${obj.meta.shape}` : obj.type;
      li.append(el('span', { class: 'lname' }, name));
      const eye = el('button', {}, obj.visible ? '👁' : '🚫');
      eye.onclick = () => { obj.set('visible', !obj.visible); ed.canvas.renderAll(); refreshLayers(ed); };
      const lock = el('button', {}, obj.selectable ? '🔓' : '🔒');
      lock.onclick = () => { setLocked(obj, obj.selectable); ed.canvas.renderAll(); refreshLayers(ed); };
      const del = el('button', {}, '✕');
      del.onclick = () => { ed.canvas.remove(obj); refreshLayers(ed); };
      li.append(eye, lock, del);
      li.onclick = e => {
        if (e.target.tagName === 'BUTTON') return;
        if (obj.selectable) { ed.canvas.setActiveObject(obj); ed.canvas.renderAll(); }
      };
      // drag to reorder z
      li.ondragstart = e => e.dataTransfer.setData('text', String(objects.indexOf(obj)));
      li.ondragover = e => e.preventDefault();
      li.ondrop = e => {
        e.preventDefault();
        const from = Number(e.dataTransfer.getData('text'));
        const to = objects.indexOf(obj);
        ed.canvas.moveTo(objects[from], to);
        ed.canvas.renderAll();
        refreshLayers(ed);
      };
      if (ed.canvas.getActiveObject() === obj) li.classList.add('active');
      list.append(li);
    });
  }

  function setLocked(obj, locked) {
    obj.set({ selectable: !locked, evented: !locked,
              lockMovementX: locked, lockMovementY: locked });
  }

  // ---- toolbar -----------------------------------------------------------------

  function wireToolbar(ed) {
    const q = sel => ed.root.querySelector(sel);
    q('[data-act=text]').onclick = () => {
      const tb = new fabric.Textbox('NEW TEXT', {
        left: 80, top: 80, width: 500, fontSize: 90, fontFamily: mapFont(ed, 'Anton'),
        fill: '#FFFFFF', stroke: '#000000', strokeWidth: 6, paintFirst: 'stroke',
        fontWeight: 'bold', meta: { kind: 'text' } });
      ed.canvas.add(tb); ed.canvas.setActiveObject(tb); refreshLayers(ed);
    };
    q('[data-act=circle]').onclick = () => {
      addExtra(ed, { shape: 'circle', x_frac: 0.4, y_frac: 0.5, r_frac: 0.12,
                     stroke: '#FF2A2A', stroke_width: 10 });
      refreshLayers(ed);
    };
    q('[data-act=arrow]').onclick = () => {
      ed.canvas.add(makeArrow(300, 500, 520, 360, '#FFE600', 24)); refreshLayers(ed);
    };
    q('[data-act=badge]').onclick = () => {
      addExtra(ed, { shape: 'badge', x_frac: 0.5, y_frac: 0.3, size_frac: 0.14,
                     fill: '#E60000', text_fill: '#fff', label: 'NEW' });
      refreshLayers(ed);
    };
    q('[data-act=image]').onchange = async e => {
      const file = e.target.files[0];
      if (!file) return;
      try {
        let url;
        if (q('[data-act=image-cutout]').checked) {
          status('Removing background…');
          const fd = new FormData(); fd.append('image', file);
          const resp = await fetch('/cutout', { method: 'POST', body: fd });
          const data = await resp.json();
          if (!resp.ok) throw new Error(data.error);
          url = data.cutout;
        } else {
          url = URL.createObjectURL(file);
        }
        const img = await loadImage(url);
        if (img.height > H * 0.8) img.scaleToHeight(H * 0.8);
        img.set({ left: 100, top: 100, meta: { kind: 'image' } });
        ed.canvas.add(img); refreshLayers(ed); status('Image added.');
      } catch (err) { status(err.message, true); }
      e.target.value = '';
    };
    q('[data-act=undo]').onclick = () => undo(ed);
    q('[data-act=redo]').onclick = () => redo(ed);
    q('[data-act=duplicate]').onclick = () => duplicate(ed);
    q('[data-act=fliph]').onclick = () => {
      const obj = ed.canvas.getActiveObject();
      if (obj) { obj.set('flipX', !obj.flipX); ed.canvas.renderAll(); }
    };
    q('[data-act=delete]').onclick = () => {
      const obj = ed.canvas.getActiveObject();
      if (obj) { ed.canvas.remove(obj); refreshLayers(ed); }
    };
    q('[data-act=export]').onclick = () => exportPNG(ed);
    q('[data-act=save-template]').onclick = () => saveTemplate(ed);
    q('[data-act=save-project]').onclick = async () => {
      const name = prompt('Project name?');
      if (!name) return;
      await api('/projects/save', { name, state: ed.canvas.toJSON(EXTRA_PROPS) });
      status(`Project "${name}" saved.`);
      refreshProjects(ed);
    };
    q('[data-act=projects]').onchange = async e => {
      if (!e.target.value) return;
      const data = await (await fetch(`/projects/load?name=${encodeURIComponent(e.target.value)}`)).json();
      restore(ed, JSON.stringify(data.state));
      pushHistory(ed);
      status(`Project "${e.target.value}" loaded.`);
    };
  }

  async function refreshProjects(ed) {
    const sel = ed.root.querySelector('[data-act=projects]');
    const data = await (await fetch('/projects/list')).json();
    sel.innerHTML = '<option value="">Open project…</option>' +
      data.projects.map(p => `<option>${p}</option>`).join('');
  }

  async function exportPNG(ed) {
    // multiplier cancels the display zoom so the file is exactly 1280x720,
    // pixel-identical to the canvas contents.
    const dataUrl = ed.canvas.toDataURL({ format: 'png', multiplier: 1 / ed.zoom });
    const name = prompt('File name?', 'thumbnail') || 'thumbnail';
    try {
      const data = await api('/export', { png: dataUrl, name });
      ed.lastExport = data.file;
      const a = el('a', { href: data.file, download: name + '.png' });
      document.body.append(a); a.click(); a.remove();
      status(`Exported ${data.file}`);
      if (ed.onExport) ed.onExport(data.file);
    } catch (err) { status(err.message, true); }
  }

  // ---- save current layout as a style template ---------------------------------

  function saveTemplate(ed) {
    const name = prompt('Template name?');
    if (!name) return;
    const objs = ed.canvas.getObjects();
    const bg = objs.find(o => o.meta?.kind === 'background');
    const face = objs.find(o => o.meta?.kind === 'face');
    const text = objs.find(o => o.meta?.kind === 'text' || o.type === 'textbox');
    const faceCx = face ? face.left + face.getScaledWidth() / 2 : W;
    const style = {
      id: name.toLowerCase().replace(/\s+/g, '_'),
      name, description: `User template saved from the editor (${name}).`,
      face: {
        height_frac: face ? +(face.getScaledHeight() / H).toFixed(2) : 0.85,
        anchor: faceCx < W * 0.38 ? 'left' : faceCx > W * 0.62 ? 'right' : 'center',
        x_bleed_px: 30, rim_light: true, drop_shadow: !!(face && face.shadow),
      },
      text: {
        position: text?.meta?.position || nearestRegion(text),
        max_words: 4, case: 'upper',
        font: text ? text.fontFamily : 'Anton',
        start_size: text ? Math.round(text.fontSize * (text.scaleX || 1)) : 130,
        max_lines: 2,
        fill: text ? text.fill : '#FFFFFF',
        stroke: text ? text.stroke : '#000000',
        stroke_width: text ? text.strokeWidth : 8,
        accent_bar: !!text?.meta?.accent_bar,
      },
      background: {
        treatment: bg?.meta?.treatment || 'darken_left',
        darken: bg?.meta?.darken ?? 0.5,
        shift_x: bg?.meta?.shift_x ?? 0,
        saturation: bg?.meta?.saturation ?? 1.1,
        prompt_style_suffix: 'dramatic lighting, bold colors, high contrast',
      },
      extras: objs.filter(o => o.meta?.kind === 'extra' && o.meta.shape !== 'accent_bar')
        .map(o => extraToJSON(o)).filter(Boolean),
    };
    api('/templates/save', { style })
      .then(d => status(`Template saved as "${d.id}" — it appears in the style list next run.`))
      .catch(err => status(err.message, true));
  }

  function nearestRegion(text) {
    if (!text) return 'left';
    const cx = (text.left + text.getScaledWidth() / 2) / W;
    const cy = (text.top + text.getScaledHeight() / 2) / H;
    let best = 'left', dist = 9e9;
    for (const [pos, [rx, ry, rw]] of Object.entries(TEXT_REGIONS)) {
      const d = Math.hypot(cx - (rx + rw / 2), cy - ry);
      if (d < dist) { dist = d; best = pos; }
    }
    return best;
  }

  function extraToJSON(o) {
    const shape = o.meta.shape;
    if (shape === 'circle') {
      const r = o.radius * (o.scaleX || 1);
      return { type: 'circle', x_frac: +((o.left + r) / W).toFixed(3),
               y_frac: +((o.top + r) / H).toFixed(3), r_frac: +(r / W).toFixed(3),
               stroke: o.stroke, stroke_width: o.strokeWidth };
    }
    if (shape === 'badge') {
      const r = o.getScaledWidth() / 2;
      const label = o.getObjects?.().find(x => x.type === 'text');
      return { type: 'badge', x_frac: +((o.left + r) / W).toFixed(3),
               y_frac: +((o.top + r) / H).toFixed(3), size_frac: +(r / H).toFixed(3),
               fill: o.getObjects?.()[0]?.fill || '#E60000',
               text_fill: label?.fill || '#fff', label: label?.text || '!' };
    }
    if (shape === 'banner') {
      const label = o.getObjects?.().find(x => x.type === 'text');
      return { type: 'banner', y_frac: +(o.top / H).toFixed(3),
               height_frac: +(o.getScaledHeight() / H).toFixed(3),
               fill: o.getObjects?.()[0]?.fill || '#C00000',
               text_fill: label?.fill || '#fff', label: label?.text || '' };
    }
    if (shape === 'arrow') {
      const x1 = o.left, y1 = o.top + o.getScaledHeight();
      const x2 = o.left + o.getScaledWidth(), y2 = o.top;
      return { type: 'arrow', from: [+(x1 / W).toFixed(3), +(y1 / H).toFixed(3)],
               to: [+(x2 / W).toFixed(3), +(y2 / H).toFixed(3)],
               fill: o.getObjects?.()[1]?.fill || '#FF2A2A', width: 24 };
    }
    return null;
  }

  // ---- side panel --------------------------------------------------------------

  function syncProps(ed) {
    const obj = ed.canvas.getActiveObject();
    if (!obj) return;
    const q = sel => ed.root.querySelector(sel);
    if (obj.fontFamily) q('[data-prop=fontFamily]').value = obj.fontFamily;
    if (obj.fontSize) q('[data-prop=fontSize]').value = Math.round(obj.fontSize);
    if (typeof obj.fill === 'string') q('[data-prop=fill]').value = toHex(obj.fill);
    if (typeof obj.stroke === 'string') q('[data-prop=stroke]').value = toHex(obj.stroke);
    q('[data-prop=strokeWidth]').value = obj.strokeWidth || 0;
    q('[data-prop=opacity]').value = Math.round((obj.opacity ?? 1) * 100);
    refreshLayers(ed);
  }

  function toHex(color) {
    if (/^#[0-9a-f]{6}$/i.test(color)) return color;
    const ctx = document.createElement('canvas').getContext('2d');
    ctx.fillStyle = color;
    return ctx.fillStyle;
  }

  function wireSidePanel(ed) {
    const q = sel => ed.root.querySelector(sel);
    const apply = (prop, value) => {
      const obj = ed.canvas.getActiveObject();
      if (!obj) return;
      obj.set(prop, value);
      ed.canvas.renderAll();
    };
    q('[data-prop=fontFamily]').onchange = e => apply('fontFamily', e.target.value);
    q('[data-prop=fontSize]').oninput = e => apply('fontSize', Number(e.target.value) || 12);
    q('[data-prop=opacity]').oninput = e => apply('opacity', Number(e.target.value) / 100);
    q('[data-prop=fill]').oninput = e => apply('fill', e.target.value);
    q('[data-prop=stroke]').oninput = e => apply('stroke', e.target.value);
    q('[data-prop=strokeWidth]').oninput = e => apply('strokeWidth', Number(e.target.value));
    q('[data-prop=allcaps]').onchange = e => {
      const obj = ed.canvas.getActiveObject();
      if (obj && obj.text != null) {
        if (e.target.checked) { obj.meta = obj.meta || {}; obj.meta.lowerText = obj.text; obj.set('text', obj.text.toUpperCase()); }
        else if (obj.meta?.lowerText) obj.set('text', obj.meta.lowerText);
        ed.canvas.renderAll();
      }
    };

    q('[data-act=bg-lock]').onchange = e => {
      const bg = ed.canvas.getObjects().find(o => o.meta?.kind === 'background');
      if (bg) { setLocked(bg, e.target.checked); ed.canvas.renderAll(); }
    };

    q('[data-act=bg-apply]').onclick = async () => {
      const bg = ed.canvas.getObjects().find(o => o.meta?.kind === 'background');
      if (!bg) return status('No background layer.', true);
      const m = bg.meta;
      try {
        status('Re-rendering background…');
        const data = await api('/background/adjust', {
          src: m.src, treatment: m.treatment,
          shift_x: Number(q('[data-bg=shift_x]').value),
          darken: Number(q('[data-bg=darken]').value) / 100,
          saturation: Number(q('[data-bg=saturation]').value) / 100,
        });
        m.shift_x = Number(q('[data-bg=shift_x]').value);
        m.darken = Number(q('[data-bg=darken]').value) / 100;
        m.saturation = Number(q('[data-bg=saturation]').value) / 100;
        await new Promise(res => bg.setSrc(data.file + '?t=' + Date.now(), () => res()));
        bg.scaleToWidth(W);
        ed.canvas.renderAll();
        status('Background updated.');
      } catch (err) { status(err.message, true); }
    };

    q('[data-act=style]').onchange = e => {
      const style = ed.styles.find(s => s.id === e.target.value);
      if (style) applyStyle(ed, style);
      e.target.value = '';
    };

    q('[data-act=freeform]').onclick = async () => {
      const instruction = q('[data-act=freeform-text]').value.trim();
      if (!instruction) return;
      try {
        status('Asking Claude…');
        const data = await api('/freeform', {
          state: ed.canvas.toJSON(EXTRA_PROPS), instruction });
        restore(ed, JSON.stringify(data.state));
        pushHistory(ed);
        status('Change applied. Undo if it missed.');
      } catch (err) { status(err.message, true); }
    };
  }

  // Re-apply a style JSON to whatever is on the canvas now.
  function applyStyle(ed, style) {
    const c = ed.canvas;
    const face = c.getObjects().find(o => o.meta?.kind === 'face');
    if (face) {
      const scale = (H * style.face.height_frac) / face.height;
      face.scale(scale);
      const w = face.width * scale;
      face.set({
        left: style.face.anchor === 'right' ? W - w + style.face.x_bleed_px
            : style.face.anchor === 'left' ? -style.face.x_bleed_px : (W - w) / 2,
        top: H - face.height * scale,
        shadow: style.face.drop_shadow ? new fabric.Shadow({ color: 'rgba(0,0,0,0.55)', blur: 22, offsetX: -10, offsetY: 8 }) : null,
      });
    }
    const text = c.getObjects().find(o => o.type === 'textbox');
    if (text) {
      const r = textRegion(style.text.position);
      let value = text.text;
      if (style.text.case === 'upper') value = value.toUpperCase();
      text.set({
        left: r.x, width: r.width, textAlign: r.align,
        fontFamily: mapFont(ed, style.text.font), fontSize: style.text.start_size,
        fill: style.text.fill, stroke: style.text.stroke,
        strokeWidth: style.text.stroke_width, text: value,
      });
      shrinkToFit(text, style.text.max_lines);
      text.set('top', r.vAnchor === 'middle' ? r.y - text.height / 2
                    : r.vAnchor === 'bottom' ? r.y - text.height : r.y);
      text.meta = { ...(text.meta || {}), position: style.text.position };
    }
    c.renderAll();
    refreshLayers(ed);
    status(`Style "${style.name}" applied. (Background treatment: use the sliders + Apply.)`);
  }

  return {
    mount,
    loadLayers: (ed, spec) => loadLayers(ed, spec),
    status,
    api,
  };
})();
