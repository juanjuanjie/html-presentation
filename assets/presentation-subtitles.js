(() => {
  const slides = [...document.querySelectorAll('.slide')];
  slides.forEach(slide => {
    let subtitle = slide.querySelector(':scope > .slide-subtitle');
    if (!subtitle) {
      subtitle = document.createElement('p');
      subtitle.className = 'slide-subtitle';
      const title = slide.querySelector('h1, h2, h3');
      subtitle.textContent = slide.dataset.subtitle || slide.dataset.caption || (title ? title.textContent.trim().replace(/\s+/g, ' ') : '');
      slide.appendChild(subtitle);
    }
  });

  let toggle = document.getElementById('subtitle-toggle');
  if (!toggle) {
    toggle = document.createElement('button');
    toggle.id = 'subtitle-toggle';
    toggle.className = 'subtitle-toggle';
    toggle.type = 'button';
    document.body.appendChild(toggle);
  }

  const value = new URLSearchParams(location.search).get('subtitles');
  let visible = !['0', 'off', 'false', 'no'].includes(String(value).toLowerCase());

  function setSubtitles(next) {
    visible = Boolean(next);
    document.body.classList.toggle('subtitles-hidden', !visible);
    toggle.setAttribute('aria-pressed', String(visible));
    toggle.setAttribute('aria-label', visible ? '关闭字幕' : '显示字幕');
    toggle.title = visible ? '关闭字幕（S）' : '显示字幕（S）';
    toggle.textContent = visible ? '字幕开' : '字幕关';
    return visible;
  }

  toggle.addEventListener('click', () => setSubtitles(!visible));
  document.addEventListener('keydown', event => {
    if (event.key.toLowerCase() !== 's' || /input|textarea|select/i.test(event.target.tagName)) return;
    event.preventDefault();
    setSubtitles(!visible);
  });

  window.presentation = window.presentation || {};
  window.presentation.setSubtitles = setSubtitles;
  window.presentation.subtitlesVisible = () => visible;
  if (typeof window.presentation.goTo !== 'function') {
    window.presentation.goTo = (requestedIndex) => {
      const targetIndex = Math.max(0, Math.min(slides.length - 1, Number(requestedIndex) || 0));
      const currentIndex = () => slides.findIndex(slide => slide.classList.contains('active'));
      const previous = document.querySelector('[data-dir="prev"],#prevBtn,[aria-label="Previous slide"],[aria-label="上一页"]');
      const next = document.querySelector('[data-dir="next"],#nextBtn,[aria-label="Next slide"],[aria-label="下一页"]');
      let guard = slides.length + 1;
      while (currentIndex() > targetIndex && previous && guard > 0) {
        previous.click();
        guard -= 1;
      }
      guard = slides.length + 1;
      while (currentIndex() < targetIndex && next && guard > 0) {
        next.click();
        guard -= 1;
      }
      if (currentIndex() !== targetIndex) {
        slides.forEach((slide, index) => {
          slide.classList.toggle('active', index === targetIndex);
          slide.classList.toggle('prev', index < targetIndex);
        });
      }
      return targetIndex;
    };
  }
  window.subtitleController = { setVisible: setSubtitles, isVisible: () => visible };
  setSubtitles(visible);
})();
