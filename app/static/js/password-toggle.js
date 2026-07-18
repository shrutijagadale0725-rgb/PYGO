document.querySelectorAll('.password-toggle').forEach(btn => {
  btn.addEventListener('click', () => {
    const input = document.getElementById(btn.dataset.target);
    const showing = input.type === 'text';
    input.type = showing ? 'password' : 'text';
    btn.textContent = showing ? '😵' : '😯';
    btn.setAttribute('aria-label', showing ? 'Show password' : 'Hide password');
  });
});