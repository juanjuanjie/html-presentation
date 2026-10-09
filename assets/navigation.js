/* Hash routes keep Pages deployment simple and preserve in-page manuscript edits. */
(() => {
  const pages = {
    generator: ['从稿件到 HTML', '上课演讲，用逐字稿提炼重点；视频分镜，用导演稿逐镜还原。选择制作模式和模板，复制完整提示词，交给你常用的 AI 生成。'],
    templates: ['模板广场', '先挑选适合内容的视觉风格，预览配色与布局，再回到稿件生成选择模板。'],
    motion: ['动效参考', '浏览可复用的动效组件，为导演稿寻找合适的画面表达。']
  };
  let current;
  function navigate() {
    const hash = location.hash.slice(1);
    const next = Object.hasOwn(pages, hash) ? hash : 'generator';
    Object.keys(pages).forEach(id => { document.getElementById(id).hidden = id !== next; });
    document.querySelectorAll('[data-page-link]').forEach(link => {
      if (link.dataset.pageLink === next) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
    document.getElementById('hero-title').textContent = pages[next][0];
    document.querySelector('.hero p').textContent = pages[next][1];
    document.title = pages[next][0] + ' · HTML Presentation';
    if (current !== next) {
      renderComponentLab(); // Load motion previews only while their page is visible.
      window.scrollTo(0, 0);
    }
    current = next;
  }
  window.addEventListener('hashchange', navigate);
  navigate();
})();
