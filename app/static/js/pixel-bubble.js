/**
 * PygoBubble — a reusable pixel-art "NPC speech bubble" used to nudge
 * logged-out users toward signing up, without ever redirecting them away
 * from the page they're on.
 *
 * Usage:
 *   PygoBubble.show("🔒 Sign up to save this!");
 *
 * Or declaratively, on any element:
 *   <button data-requires-auth data-auth-message="✨ Just one click!">Save</button>
 * Clicking it while logged out shows the bubble and cancels the click;
 * logged-in users pass through untouched.
 *
 * Relies on `window.PYGO_LOGGED_IN` being set (see base.html) and a
 * `#auth-anchor` element wrapping the Login/Sign Up buttons.
 */
(function () {
  const CORNER = 10; // px "radius" of the pixel-stair corner
  const STEP = 5;     // px size of each stair step (CORNER should be a multiple of STEP)

  const COPY_POOL = [
    "👉 This way!",
    "✨ Come join!",
    "🌱 Let's begin!",
    "💛 Join us!",
    "🎈 Hop in!",
    "🚪 Almost in!",
    "🎉 Join the fun!",
    "😊 It's free!",
  ];

  let bubbleEl, innerEl, arrowEl, textEl;
  let hideTimer = null;
  let built = false;

  function pixelClipPath(w, h) {
    if (w <= 0 || h <= 0) return "none";
    const c = Math.min(CORNER, w / 2, h / 2);
    const steps = Math.max(1, Math.round(c / STEP));
    const s = c / steps;

    const tl = [], tr = [], br = [], bl = [];
    for (let i = 0; i <= steps; i++) {
      const a = i * s;
      const b = c - i * s;
      tl.push(`${b}px ${a}px`);
      tr.push(`${w - c + a}px ${b}px`);
      br.push(`${w - b}px ${h - c + a}px`);
      bl.push(`${c - a}px ${h - b}px`);
    }
    const points = [
      `${c}px 0`, ...tr.map((_, i) => tr[i]),
      `${w}px ${c}px`, ...br.map((_, i) => br[i]),
      `${w - c}px ${h}px`, ...bl.map((_, i) => bl[i]),
      `0 ${h - c}px`, ...tl.map((_, i) => tl[i]),
    ];
    return `polygon(${points.join(",")})`;
  }

  function build() {
    if (built) return;
    bubbleEl = document.createElement("div");
    bubbleEl.id = "pixel-bubble";
    bubbleEl.setAttribute("role", "status");
    bubbleEl.setAttribute("aria-live", "polite");

    innerEl = document.createElement("div");
    innerEl.className = "pixel-bubble-inner";

    textEl = document.createElement("span");
    textEl.className = "pixel-bubble-text";

    arrowEl = document.createElement("div");
    arrowEl.className = "pixel-bubble-arrow";

    innerEl.appendChild(textEl);
    bubbleEl.appendChild(innerEl);
    bubbleEl.appendChild(arrowEl);
    document.body.appendChild(bubbleEl);
    built = true;

    bubbleEl.addEventListener("click", hide);
  }

  function position() {
    const anchor = document.getElementById("auth-anchor");
    if (!anchor) return;
    const rect = anchor.getBoundingClientRect();

    bubbleEl.style.visibility = "hidden";
    bubbleEl.style.left = "0px";
    bubbleEl.style.top = "0px";
    bubbleEl.style.display = "block";

    const bw = bubbleEl.offsetWidth;
    const bh = bubbleEl.offsetHeight;

    let left = rect.right - bw;
    left = Math.max(8, Math.min(left, window.innerWidth - bw - 8));
    let top = rect.bottom + 14;
    if (top + bh > window.innerHeight - 8) {
      top = rect.top - bh - 14;
    }

    bubbleEl.style.left = `${left}px`;
    bubbleEl.style.top = `${top}px`;
    bubbleEl.style.visibility = "visible";

    const arrowTarget = rect.left + rect.width / 2 - left;
    const arrowLeft = Math.max(14, Math.min(arrowTarget, bw - 14));
    arrowEl.style.left = `${arrowLeft - 7}px`;
    arrowEl.style.right = "auto";
    arrowEl.style.top = top < rect.top ? "auto" : "-11px";
    arrowEl.style.bottom = top < rect.top ? "-11px" : "auto";
    arrowEl.classList.toggle("pixel-bubble-arrow-down", top >= rect.top);
    arrowEl.classList.toggle("pixel-bubble-arrow-up", top < rect.top);

    bubbleEl.style.clipPath = pixelClipPath(bw, bh);
    innerEl.style.clipPath = pixelClipPath(bw - 6, bh - 6);
  }

  function show(message) {
    build();
    textEl.textContent = message;

    clearTimeout(hideTimer);
    bubbleEl.classList.remove("hide");
    bubbleEl.classList.remove("show");
    void bubbleEl.offsetWidth;

    position();
    bubbleEl.classList.add("show");

    hideTimer = setTimeout(hide, 6500);
  }

  function hide() {
    if (!bubbleEl) return;
    clearTimeout(hideTimer);
    bubbleEl.classList.remove("show");
    bubbleEl.classList.add("hide");
  }

  let copyIndex = 0;
  function nextCopy() {
    const msg = COPY_POOL[copyIndex % COPY_POOL.length];
    copyIndex += 1;
    return msg;
  }

  document.addEventListener("click", (e) => {
    const el = e.target.closest("[data-requires-auth]");
    if (!el) return;
    if (window.PYGO_LOGGED_IN) return;

    e.preventDefault();
    e.stopPropagation();

    const msg = el.getAttribute("data-auth-message") || nextCopy();
    show(msg);
  });

  window.addEventListener("resize", () => {
    if (bubbleEl && bubbleEl.classList.contains("show")) position();
  });

  window.PygoBubble = { show, hide };
})();