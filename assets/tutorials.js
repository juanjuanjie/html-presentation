/* Public collection snapshot: https://space.bilibili.com/229150291/lists/6797294?type=season
 * Add new episodes here: [bvid, title, duration, category]. No browser API/CORS dependency.
 * This is a curated directory, not an automatic Bilibili collection synchronizer.
 */
(() => {
  const episodes = [
    ['BV1jCAGzpE7i', 'PPT正在被HTML淘汰 | 我开始用html做视频素材', '03:08', 'HTML'],
    ['BV1adMC6AEGU', 'HyperFrames，一个让HTML变视频的神级开源项目！', '05:31', 'HTML'],
    ['BV1HToiBCEwg', '手把手教你打造专属HTML SKILL！让AI完全懂你的设计风格', '03:18', 'HTML'],
    ['BV1g5j46iE5C', '开源！用HTML替代PPT做分镜，我踩完坑了！', '03:59', 'HTML'],
    ['BV1TKNA6eEhX', '我用 HTML + AI做视频封面', '04:50', 'HTML'],
    ['BV1Sopn6PEkJ', '我的AI剪辑工作台大揭秘：从逐字稿到粗剪成片，AI 干活，我验收', '10:07', 'HTML'],
    ['BV1HbJR66E3a', '认识一下我吧！20W播放的后续彩蛋', '00:55', 'HTML'],
    ['BV1dPeB6XEBY', 'Chrome变身工作台：1个配置+5个神仙插件，效率翻倍', '05:18', '工作台'],
    ['BV1uDGE6NEEo', 'Vibecoding时代，我从「看板」升级为「工作台」搭建', '05:13', '工作台'],
    ['BV1smEb6BEHD', '用AI让「数据」变成「可视化图表」| Vibecoding 实战 EP02', '04:57', '工作台'],
    ['BV1yMJA6AER5', '搭建高颜值数据表格 + 全局提醒功能 | VibeCoding实战 EP03', '06:50', '工作台'],
    ['BV1sUK86CEBF', 'AI音频坦白局！IndexTTS！克隆+情感', '06:33', 'AI音频'],
    ['BV15nNQ6EEGs', 'AI配音坦白局！开源！chatTTS！', '05:57', 'AI音频'],
    ['BV1dyhK6sEcJ', 'MOSS Transcribe Diarize，AI字幕君，比人工更快更准', '07:40', 'AI音频'],
    ['BV1RFR1BHEtC', '视频里的卡通小人怎么做的？手把手打造专属动漫IP分身', '02:52', 'AI图片'],
    ['BV1USw3zvEoi', '我用OpenClaw手搓了个投资网站，让 AI 从“动口”到“动手”', '09:56', '其他'],
    ['BV1VrX9BzEkr', '我用VSCode+Codex手搓了个跟踪网页 | vibe coding实战', '04:18', '其他'],
    ['BV1Dbaa6sEY5', '我用过最强的 AI 投研网页，板块、WSB、13F 一次看完，还提供 API | MarketGrep', '06:30', '其他']
  ].filter(episode => episode[3] === 'HTML'); // Only HTML tutorials belong in this project.
  let selected = 0;
  let active = false;
  const player = document.getElementById('tutorial-player');
  const list = document.getElementById('tutorial-episodes');
  function mountPlayer() {
    const [bvid, title] = episodes[selected];
    const frame = document.createElement('iframe');
    frame.title = title;
    frame.src = `https://player.bilibili.com/player.html?bvid=${encodeURIComponent(bvid)}&p=1&autoplay=0&danmaku=0&poster=1`;
    frame.allow = 'fullscreen; picture-in-picture; encrypted-media';
    frame.allowFullscreen = true;
    player.replaceChildren(frame);
    document.getElementById('tutorial-title').textContent = title;
    document.getElementById('tutorial-original').href = `https://www.bilibili.com/video/${bvid}/`;
  }
  function renderList() {
    list.replaceChildren();
    episodes.forEach((episode, index) => {
      const li = document.createElement('li');
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'tutorial-episode';
      button.setAttribute('aria-current', String(index === selected));
      const number = document.createElement('small');
      number.textContent = String(index + 1).padStart(2, '0');
      const title = document.createElement('span');
      title.textContent = episode[1];
      const duration = document.createElement('small');
      duration.textContent = episode[2];
      button.append(number, title, duration);
      button.addEventListener('click', () => {
        if (selected === index) return;
        selected = index;
        mountPlayer();
        list.querySelectorAll('button').forEach(item => item.setAttribute('aria-current', String(item === button)));
      });
      li.append(button);
      list.append(li);
    });
    list.scrollTop = 0;
  }
  renderList();
  window.setTutorialPageActive = value => {
    if (active === value) return;
    active = value;
    if (active) mountPlayer();
    else player.replaceChildren(); // Stop playback when leaving; preserve manuscript and selected episode.
  };
})();
