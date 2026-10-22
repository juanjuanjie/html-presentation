/* Hash routes keep Pages deployment simple and preserve in-page manuscript edits. */
(() => {
  const pages = {
    generator: ['稿件 → HTML', '上课演讲，用逐字稿提炼重点；视频分镜，用导演稿逐镜还原。选择制作模式和模板，复制完整提示词，交给你常用的 AI 生成。'],
    templates: ['模板广场', '先挑选适合内容的视觉风格，预览配色与布局，再回到稿件生成选择模板。'],
    'ui-elements': ['UI素材库', '小元素，随取随用。'],
    readme: ['README', '了解 HTML Presentation 的使用方式、模板结构与项目说明。']
  };
  let current;
  function navigate() {
    const hash = location.hash.slice(1);
    if (hash === 'motion') { location.replace('#ui-elements'); return; }
    const next = Object.hasOwn(pages, hash) ? hash : 'generator';
    Object.keys(pages).forEach(id => { document.getElementById(id).hidden = id !== next; });
    document.querySelectorAll('[data-page-link]').forEach(link => {
      if (link.dataset.pageLink === next) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
    const hero = document.querySelector('.hero');
    hero.hidden = next === 'readme';
    const heroTitle = document.getElementById('hero-title');
    if (next === 'generator') {
      heroTitle.innerHTML = '<span class="hero-title__highlight">稿件</span><span class="hero-title__arrow">→</span><span class="hero-title__highlight">HTML</span>';
    } else {
      heroTitle.textContent = pages[next][0];
    }
    document.querySelector('.hero p').textContent = pages[next][1];
    document.documentElement.dataset.page = next;
    document.title = pages[next][0] + ' · HTML Presentation';
    if (next === 'readme' && typeof window.loadReadmePage === 'function') {
      window.loadReadmePage();
    }
    if (next === 'ui-elements') {
      const frame = document.getElementById('ui-elements-frame');
      if (!frame.hasAttribute('src')) frame.src = frame.dataset.src;
    }
    if (current !== next) {
      window.scrollTo(0, 0);
    }
    current = next;
  }
  window.addEventListener('hashchange', navigate);
  window.addEventListener('message', event => {
    const frame = document.getElementById('ui-elements-frame');
    if (event.source !== frame.contentWindow || event.data?.type !== 'ui-elements-height') return;
    const height = Number(event.data.height);
    if (Number.isFinite(height) && height > 0) frame.style.height = Math.ceil(height) + 'px';
  });
  navigate();
})();
