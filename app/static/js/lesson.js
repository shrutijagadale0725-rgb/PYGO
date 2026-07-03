(function () {
  const runBtn = document.getElementById('run-btn');
  const runStatus = document.getElementById('run-status');
  const outputEl = document.getElementById('output');
  const codeEl = document.getElementById('code');
  const banner = document.getElementById('result-banner');

  let solved = ALREADY_COMPLETED;
  let pyodideReady = null;

  function setStatus(text, tone) {
    runStatus.textContent = text;
    runStatus.classList.remove('warn', 'success');
    if (tone) runStatus.classList.add(tone);
  }

  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // Pyodide wraps the full Python traceback as the error's message. The
  // last non-empty line is always the actual "ErrorType: message" part -
  // the one line that's actually useful for a beginner to read, without
  // the internal "<string>, line N" frames above it.
  function extractPythonError(err) {
    const raw = (err && err.message) ? err.message : String(err);
    const lines = raw.trim().split('\n').filter(Boolean);
    return lines.length ? lines[lines.length - 1] : 'An error occurred while running your code.';
  }

  const CONFETTI_COLORS = ['#FFD23F', '#FF5A3C', '#1FAE7A', '#3457D5', '#14171A'];

  function triggerConfetti() {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const count = 46;
    for (let i = 0; i < count; i++) {
      const piece = document.createElement('div');
      piece.className = 'confetti-piece';
      piece.style.left = Math.random() * 100 + 'vw';
      piece.style.background = CONFETTI_COLORS[Math.floor(Math.random() * CONFETTI_COLORS.length)];
      const duration = 2 + Math.random() * 1.5;
      const delay = Math.random() * 0.3;
      piece.style.animationDuration = duration + 's';
      piece.style.animationDelay = delay + 's';
      piece.style.setProperty('--start-rotate', Math.floor(Math.random() * 360) + 'deg');
      document.body.appendChild(piece);
      setTimeout(() => piece.remove(), (duration + delay) * 1000 + 150);
    }
  }

  async function setupPyodide() {
    try {
      const pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.28.3/full/",
      });
      let buffer = "";
      pyodide.setStdout({ batched: (msg) => { buffer += msg + "\n"; } });
      pyodide.setStderr({ batched: (msg) => { buffer += msg + "\n"; } });
      pyodide.__getBuffer = () => buffer;
      pyodide.__resetBuffer = () => { buffer = ""; };
      runBtn.disabled = false;
      runBtn.textContent = "▶ RUN";
      setStatus("Ready when you are.", null);
      return pyodide;
    } catch (e) {
      setStatus("Couldn't load Python — check your connection and reload.", "warn");
      throw e;
    }
  }
  pyodideReady = setupPyodide();

  codeEl.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = codeEl.selectionStart, end = codeEl.selectionEnd;
      codeEl.value = codeEl.value.slice(0, start) + "    " + codeEl.value.slice(end);
      codeEl.selectionStart = codeEl.selectionEnd = start + 4;
    }
  });

  async function reportCompletion() {
    if (!IS_LOGGED_IN) {
      setStatus("Solved! Log in to save your XP and progress.", "success");
      return;
    }
    try {
      const res = await fetch('/api/complete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ slug: LESSON_SLUG }),
      });
      const data = await res.json();
      if (data.ok) {
        const levelPill = document.querySelector('.stamp-pill.level');
        if (levelPill) {
          levelPill.textContent = `LV ${data.level} · ${data.total_xp} XP`;
        }
      }
    } catch (e) {
      // Non-fatal: the student still sees their local success state.
    }
  }

  runBtn.addEventListener('click', async () => {
    runBtn.disabled = true;
    runBtn.textContent = "RUNNING…";
    setStatus("Casting…", null);
    try {
      const pyodide = await pyodideReady;
      pyodide.__resetBuffer();
      let errored = false;
      let errorMessage = "";
      try {
        pyodide.runPython(codeEl.value);
      } catch (err) {
        errored = true;
        errorMessage = extractPythonError(err);
      }
      const out = pyodide.__getBuffer();

      if (errored) {
        const safeError = escapeHtml(errorMessage);
        if (out.trim().length > 0) {
          outputEl.innerHTML = escapeHtml(out).replace(/\n/g, '<br>') + `<br><span class="err">${safeError}</span>`;
        } else {
          outputEl.innerHTML = `<span class="err">${safeError}</span>`;
        }
      } else {
        outputEl.textContent = out || "(no output — did you forget to print()?)";
      }

      const pattern = new RegExp(CHECK_PATTERN);
      const match = out.match(pattern);
      const capturedValue = match && match[1] ? match[1].trim() : null;

      if (capturedValue && capturedValue !== PLACEHOLDER_VALUE && !solved) {
        solved = true;
        banner.classList.add('show', 'pop');
        document.getElementById('result-text').textContent = `${SUCCESS_MESSAGE} +${XP_REWARD} XP`;
        triggerConfetti();
        await reportCompletion();
      } else if (errored) {
        setStatus("Your code hit an error — check the red message above.", "warn");
      } else if (capturedValue === PLACEHOLDER_VALUE) {
        setStatus("Close — change the placeholder value first.", "warn");
      } else if (!solved) {
        setStatus("Not quite — check the expected output format.", "warn");
      } else {
        setStatus("Lesson already complete. Nice work!", "success");
      }
    } finally {
      runBtn.disabled = false;
      runBtn.textContent = "▶ RUN";
    }
  });
})();