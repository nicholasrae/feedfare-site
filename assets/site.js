// The example stays on the page. No network, cookies, or browser storage.
(() => {
  const steps = document.getElementById('example-steps');
  const minutes = document.getElementById('example-minutes');
  if (!steps || !minutes) return;
  const format = new Intl.NumberFormat(document.documentElement.lang || 'en');
  const update = () => {
    const amount = Number(steps.value);
    if (!Number.isFinite(amount) || amount < 0) return;
    minutes.textContent = `${format.format(Math.floor(amount / 100) * 5)} min`;
  };
  steps.addEventListener('change', update);
  update();
})();
