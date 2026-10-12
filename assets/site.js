// No analytics, cookies, or browser storage. Video stays on this host and loads on demand.
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

(() => {
  const button = document.querySelector('[data-demo-play]');
  const video = document.getElementById('feedfare-demo');
  const cover = document.getElementById('demo-cover');
  const status = document.getElementById('demo-status');
  if (!button || !video || !cover || !status) return;

  button.addEventListener('click', () => {
    const source = video.dataset.demoSource;
    if (!source) return;
    const track = video.querySelector('[data-demo-track]');
    video.src = source;
    if (track) track.src = track.dataset.demoTrack;
    cover.hidden = true;
    video.hidden = false;
    video.tabIndex = 0;
    video.focus({ preventScroll: true });
    video.addEventListener('error', () => {
      status.hidden = false;
      status.textContent = 'The video could not load. You can watch the same captioned demo using the YouTube link below.';
    }, { once: true });
    video.play().catch(() => {
      if (!video.error) {
        status.hidden = false;
        status.textContent = 'The video is ready. Use its play control to begin.';
      }
    });
  }, { once: true });
})();
