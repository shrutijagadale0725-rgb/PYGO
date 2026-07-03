/**
 * Inline "live preview" of the Variables lesson for logged-out visitors.
 * Triggered by clicking the Variables tile (data-demo-preview="variables").
 * Plays a scripted typewriter -> run -> output -> XP sequence entirely
 * inline, above the Basics grid, then reveals a signup/login CTA.
 *
 * No navigation, no modal, no dimming - the homepage stays fully visible
 * and interactive the whole time.
 */
(function () {
  const panel = document.getElementById("variables-preview");
  if (!panel) return;

  const codeTypedEl = document.getElementById("vp-code-typed");
  const runBtn = document.getElementById("vp-run-btn");
  const statusEl = document.getElementById("vp-status");
  const outputEl = document.getElementById("vp-output");
  const resultEl = document.getElementById("vp-result");
  const xpEl = document.getElementById("vp-xp");
  const ctaEl = document.getElementById("vp-cta");

  const DEMO_CODE = 'print("Let\'s code!")';
  const DEMO_OUTPUT = "Let's code!";
  const CHAR_DELAY = 35;
  const HOLD_BEFORE_CTA = 3000;

  let runToken = 0;
  const timers = [];

  function clearTimers() {
    timers.forEach(clearTimeout);
    timers.length = 0;
  }

  function after(ms, fn) {
    const id = setTimeout(fn, ms);
    timers.push(id);
    return id;
  }

  function reset() {
    clearTimers();
    codeTypedEl.textContent = "";
    runBtn.disabled = true;
    runBtn.classList.remove("pressed");
    statusEl.textContent = "Watching this run itself…";
    outputEl.innerHTML = '<span class="placeholder">&gt; output will appear here</span>';
    resultEl.classList.remove("show");
    xpEl.textContent = "+0 XP";
    ctaEl.classList.remove("show");
  }

  function typeCode(token, onDone) {
    let i = 0;
    function step() {
      if (token !== runToken) return;
      if (i > DEMO_CODE.length) { onDone(); return; }
      codeTypedEl.textContent = DEMO_CODE.slice(0, i);
      i += 1;
      after(CHAR_DELAY, step);
    }
    step();
  }

  function animateXP(token) {
    let xp = 0;
    function step() {
      if (token !== runToken) return;
      xp = Math.min(50, xp + 5);
      xpEl.textContent = `+${xp} XP`;
      if (xp < 50) after(80, step);
    }
    step();
  }

  function play() {
    runToken += 1;
    const token = runToken;
    reset();

    panel.classList.add("open");
    panel.setAttribute("aria-hidden", "false");

    after(500, () => {
      if (token !== runToken) return;
      runBtn.disabled = false;
      typeCode(token, () => {
        if (token !== runToken) return;
        after(500, () => {
          if (token !== runToken) return;
          runBtn.classList.add("pressed");
          statusEl.textContent = "Running…";
          after(250, () => runBtn.classList.remove("pressed"));

          after(700, () => {
            if (token !== runToken) return;
            outputEl.textContent = DEMO_OUTPUT;
            statusEl.textContent = "Ready when you are.";

            after(400, () => {
              if (token !== runToken) return;
              resultEl.classList.add("show");
              animateXP(token);

              after(HOLD_BEFORE_CTA, () => {
                if (token !== runToken) return;
                ctaEl.classList.add("show");
              });
            });
          });
        });
      });
    });
  }

  function close() {
    runToken += 1;
    clearTimers();
    panel.classList.remove("open");
    panel.setAttribute("aria-hidden", "true");
  }

  document.addEventListener("click", (e) => {
    const trigger = e.target.closest('[data-demo-preview="print-statements"]');
    if (trigger) {
      e.preventDefault();
      play();
      return;
    }
    if (e.target.closest("#vp-close-btn") || e.target.closest("#vp-close-x")) {
      e.preventDefault();
      close();
    }
  });
})();