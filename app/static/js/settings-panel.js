(function () {
  const openBtn = document.getElementById("settings-open-btn");
  const closeBtn = document.getElementById("settings-close-btn");
  const sidebar = document.getElementById("settings-sidebar");
  const sidebarBackdrop = document.getElementById("settings-backdrop");

  const deleteBtn = document.getElementById("settings-delete-btn");
  const confirmPopup = document.getElementById("confirm-popup");
  const confirmBackdrop = document.getElementById("confirm-backdrop");
  const cancelBtn = document.getElementById("confirm-cancel-btn");

  if (!openBtn || !sidebar) return;

  function openSidebar() {
    sidebar.classList.add("open");
    sidebarBackdrop.classList.add("show");
    sidebar.setAttribute("aria-hidden", "false");
  }
  function closeSidebar() {
    sidebar.classList.remove("open");
    sidebarBackdrop.classList.remove("show");
    sidebar.setAttribute("aria-hidden", "true");
  }
  function openConfirm() {
    confirmPopup.classList.add("show");
    confirmBackdrop.classList.add("show");
    confirmPopup.setAttribute("aria-hidden", "false");
  }
  function closeConfirm() {
    confirmPopup.classList.remove("show");
    confirmBackdrop.classList.remove("show");
    confirmPopup.setAttribute("aria-hidden", "true");
  }

  openBtn.addEventListener("click", openSidebar);
  closeBtn.addEventListener("click", closeSidebar);
  sidebarBackdrop.addEventListener("click", closeSidebar);
  deleteBtn.addEventListener("click", openConfirm);
  cancelBtn.addEventListener("click", closeConfirm);
  confirmBackdrop.addEventListener("click", closeConfirm);

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    if (confirmPopup.classList.contains("show")) closeConfirm();
    else if (sidebar.classList.contains("open")) closeSidebar();
  });
})();