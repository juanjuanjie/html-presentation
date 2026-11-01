(() => {
 const status=document.getElementById('status');
 // Small, self-contained primitives adapted from the template's decorative styles.
 const specs=[
  ['不规则圆圈','Doodle Cream · .flow-node','<span class="ui-doodle-ring"></span>',
   '.ui-doodle-ring{display:inline-block;box-sizing:border-box;width:112px;height:112px;border:3px solid #292525;border-radius:47% 53% 45% 55%/54% 46% 57% 43%;transform:rotate(-3deg)}'],
  ['暖黄手绘圆','Doodle Cream · .flow-focus','<span class="ui-doodle-disc"></span>',
   '.ui-doodle-disc{display:inline-block;box-sizing:border-box;width:112px;height:112px;border:3px solid #292525;border-radius:46% 54% 43% 57%/56% 44% 58% 42%;background:#ffe477;transform:rotate(-2deg)}'],
  ['淡紫手绘圆','Doodle Cream · 圆形轮廓 + 对比紫','<span class="ui-purple-disc"></span>',
   '.ui-purple-disc{display:inline-block;box-sizing:border-box;width:112px;height:112px;border:3px solid #292525;border-radius:54% 46% 52% 48%/47% 55% 45% 53%;background:#d8d6ff;transform:rotate(3deg)}'],
  ['不规则编号标签','Doodle Cream · .number-tag','<span class="ui-number-tag">01</span>',
   '.ui-number-tag{display:inline-grid;place-items:center;min-width:64px;height:54px;padding:0 12px;box-sizing:border-box;background:#ffe477;color:#211b0d;border:3px solid #292525;border-radius:18px 15px 20px 14px;font:700 28px/1 sans-serif}'],
  ['手绘图标底框','Doodle Cream · .icon-chip','<span class="ui-icon-chip">✦</span>',
   '.ui-icon-chip{display:inline-grid;place-items:center;width:58px;height:52px;background:#ffe477;color:#211b0d;border-radius:17px 14px 18px 13px;font:30px/1 sans-serif}'],
  ['双色 VS 圆标','Doodle Cream · .doodle-comparison__vs','<span class="ui-vs">VS</span>',
   '.ui-vs{display:inline-grid;place-items:center;box-sizing:border-box;width:70px;height:70px;border:3px solid #292525;border-radius:50%;background:linear-gradient(90deg,#ffe477 50%,#d8d6ff 50%);color:#211b0d;font:700 22px/1 sans-serif}'],
  ['文字荧光笔','Doodle Cream · .highlight','<span class="ui-highlight">重点</span>',
   '.ui-highlight{display:inline;color:#171717;font:700 32px/1.5 sans-serif;background:linear-gradient(transparent 68%,#ffe477 68% 92%,transparent 92%);box-decoration-break:clone;-webkit-box-decoration-break:clone}'],
  ['黑底文字贴纸','Doodle Cream · .black-label','<span class="ui-ink-label">重点</span>',
   '.ui-ink-label{display:inline-block;padding:5px 14px 9px;background:#171717;color:#ffe477;border-radius:20px 16px 22px 14px;font:700 28px/1.3 sans-serif}'],
  ['步骤数字框','Professional · .step-detail-num','<span class="ui-step-num">2</span>',
   '.ui-step-num{display:inline-grid;place-items:center;box-sizing:border-box;width:64px;height:64px;border:1px solid #ffc402;border-radius:10px;background:#08090d;color:#ffc402;font:700 28px/1 sans-serif}'],
  ['手绘右箭头','Doodle Cream · 流程箭头改编','<svg xmlns="http://www.w3.org/2000/svg" width="128" height="64" viewBox="0 0 128 64" fill="none" aria-label="右箭头" role="img"><path d="M12 34 Q55 27 110 32 M91 15 Q102 25 114 32 Q101 40 91 49" stroke="#292525" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>',''],
  ['勾选圆标','Doodle Cream · .doodle-comparison__mark','<span class="ui-check">✓</span>',
   '.ui-check{display:inline-grid;place-items:center;box-sizing:border-box;width:36px;height:36px;border:2px solid #292525;border-radius:50%;background:#ffe477;color:#171717;font:700 22px/1 sans-serif}']
 ];
 const $=id=>document.getElementById(id);
 const categories=['图形','图形','图形','标签','图标','图标','文字效果','文字效果','标签','箭头','图标'];
 const items=specs.map(([name,origin,html,css],i)=>({name,origin,html,css,category:categories[i],code:()=>Promise.resolve((css?'<style>'+css+'</style>\n':'')+html)}));
 const aestheticDiscHTML='<span class="ui-aesthetic-disc" role="img" aria-label="紫色错位投影的审美圆形印章"><span class="ui-aesthetic-disc__text">审美</span><span class="ui-aesthetic-disc__spark ui-aesthetic-disc__spark--top" aria-hidden="true">✦</span><span class="ui-aesthetic-disc__spark ui-aesthetic-disc__spark--bottom" aria-hidden="true">✦</span></span>';
 const aestheticDiscCSS='.ui-aesthetic-disc{--ui-disc-paper:#fffefb;--ui-disc-ink:#171717;--ui-disc-purple:#d8d6ff;position:relative;display:inline-grid;place-items:center;box-sizing:border-box;width:148px;aspect-ratio:1;border:4px solid var(--ui-disc-ink);border-radius:48% 52% 46% 54%/53% 47% 55% 45%;background:var(--ui-disc-paper);color:var(--ui-disc-ink);box-shadow:9px 10px 0 var(--ui-disc-purple);transform:rotate(3deg);font-family:"Xiaolai","KaiTi","STKaiti","Microsoft YaHei",cursive}.ui-aesthetic-disc__text{font-size:45px;font-weight:700;line-height:1;letter-spacing:-.08em;transform:translateX(-.04em) rotate(-3deg)}.ui-aesthetic-disc__spark{position:absolute;font:700 24px/1 sans-serif}.ui-aesthetic-disc__spark--top{top:-13px;left:-18px;transform:rotate(-12deg)}.ui-aesthetic-disc__spark--bottom{right:-20px;bottom:-12px;transform:rotate(9deg)}@media(prefers-reduced-motion:reduce){.ui-aesthetic-disc{transform:rotate(3deg)}}';
 items.push({name:'审美圆形印章 · 紫色错位底',aliases:'审美 紫色 淡紫 圆形 圆圈 印章 徽章 错位 投影 封面 Doodle Cream aesthetic circle badge cover',category:'图形',origin:'《AI 时代，技术门槛消失，审美门槛出现》封面 · Doodle Cream',html:aestheticDiscHTML,css:aestheticDiscCSS,previewBackground:'#fffdf5',code:()=>Promise.resolve('<style>'+aestheticDiscCSS+'</style>\n'+aestheticDiscHTML)});
 const sunButtonHTML='<button class="ui-sun-button" type="button" aria-label="切换明亮模式"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/><path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"/></svg></button>';
 const sunButtonCSS='.ui-sun-button{display:inline-grid;place-items:center;box-sizing:border-box;width:62px;height:62px;padding:0;border:3.5px solid #171717;border-radius:48% 52% 46% 54%/53% 47% 55% 45%;background:#fffdf5;color:#171717;cursor:pointer;transform:rotate(-1deg);transition:background-color .18s ease,transform .18s ease}.ui-sun-button svg{display:block;width:30px;height:30px;overflow:visible;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transition:transform .28s ease}.ui-sun-button:hover{background:#ffe477;transform:translateY(-1px) rotate(-3deg) scale(1.03)}.ui-sun-button:hover svg{transform:rotate(12deg)}.ui-sun-button:active{transform:rotate(1deg) scale(.94)}.ui-sun-button:focus-visible{outline:3px solid #d8d6ff;outline-offset:4px}@media(prefers-reduced-motion:reduce){.ui-sun-button,.ui-sun-button svg{transition:none}}';
 items.push({name:'手绘小太阳按钮',aliases:'太阳 阳光 明亮 模式 主题 切换 圆形 粗外框 手绘 图标 sun theme toggle',category:'按钮',origin:'项目顶部主题按钮 · Doodle Cream 手绘版',html:sunButtonHTML,css:sunButtonCSS,previewBackground:'#fffdf5',code:()=>Promise.resolve('<style>'+sunButtonCSS+'</style>\n'+sunButtonHTML)});
 const heroDoodle=(name,aliases,svg)=>({
   name,
   aliases,
   category:'图形',
   origin:'卷卷姐的博客 · Hero 手绘装饰',
   html:svg,
   css:'',
   previewBackground:'#fffdf5',
   code:()=>Promise.resolve(svg)
 });
 items.push(
   heroDoodle('Hero 手绘星星 · 暖黄','星星 四角星 手绘 涂鸦 黄色 装饰 sparkle star hero','<svg class="ui-hero-doodle ui-hero-doodle-star" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 72 72" fill="#FFE477" stroke="#171717" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="暖黄色手绘星星"><path d="m36 5 7 22 23 9-23 8-7 23-8-23-22-8 22-9 8-22Z"/></svg>'),
   heroDoodle('Hero 手绘星星 · 空心','星星 小星星 四角星 手绘 涂鸦 空心 装饰 sparkle star hero','<svg class="ui-hero-doodle ui-hero-doodle-tiny-star" xmlns="http://www.w3.org/2000/svg" width="76" height="76" viewBox="0 0 50 50" fill="none" stroke="#171717" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="空心手绘星星"><path d="m25 4 5 15 15 6-15 5-5 16-6-16-15-5 15-6 6-15Z"/></svg>'),
   heroDoodle('Hero 手绘小花 · 淡紫','小花 花朵 手绘 涂鸦 淡紫 紫色 装饰 flower hero','<svg class="ui-hero-doodle ui-hero-doodle-flower" xmlns="http://www.w3.org/2000/svg" width="92" height="92" viewBox="0 0 82 82" fill="#D8D6FF" stroke="#171717" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="淡紫色手绘小花"><path d="M41 31C32 8 16 13 21 29 4 24 2 43 20 45 7 58 23 70 35 54c4 21 24 16 20-2 18 8 26-10 7-18 13-12-3-25-14-8-2-16-13-19-7 5Z"/><circle cx="41" cy="41" r="7" fill="#FFFDF5"/></svg>'),
   heroDoodle('Hero 手绘爱心','爱心 心形 手绘 涂鸦 黑色线条 装饰 heart hero','<svg class="ui-hero-doodle ui-hero-doodle-heart" xmlns="http://www.w3.org/2000/svg" width="92" height="82" viewBox="0 0 74 66" fill="none" stroke="#171717" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="手绘爱心"><path d="M37 57C27 47 8 35 9 19 10 8 23 5 31 14l6 8 6-8c8-9 21-6 22 5 1 16-18 28-28 38Z"/></svg>'),
   heroDoodle('Hero 手绘卷曲线 · 左','乱画的线 卷曲线 弧线 手绘 涂鸦 黑色线条 装饰 curl scribble hero','<svg class="ui-hero-doodle ui-hero-doodle-curl-left" xmlns="http://www.w3.org/2000/svg" width="164" height="92" viewBox="0 0 130 74" fill="none" stroke="#171717" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="向左卷曲的手绘线条"><path d="M7 61c13-46 49-54 52-21 2 24-25 22-22 4 3-17 37-23 84-9"/></svg>'),
   heroDoodle('Hero 手绘卷曲线 · 右','乱画的线 卷曲线 弧线 手绘 涂鸦 黑色线条 装饰 curl scribble hero','<svg class="ui-hero-doodle ui-hero-doodle-curl-right" xmlns="http://www.w3.org/2000/svg" width="164" height="90" viewBox="0 0 132 72" fill="none" stroke="#171717" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="向右卷曲的手绘线条"><path d="M5 35c25-25 44-26 47-4 2 18-18 21-18 6 0-19 33-31 91 7"/></svg>')
 );
 const seriesImage=new URL('assets/series-character-cutout.png',location.href).href;
 const seriesHTML=src=>'<span class="ui-series-badge"><img class="ui-series-avatar" src="'+src+'" alt="举手讲解的小女孩"><span class="ui-series-title">小白学编程</span><span class="ui-series-dot" aria-hidden="true">·</span><span class="ui-series-episode">第一期</span></span>';
 const seriesCSS='.ui-series-badge{position:relative;isolation:isolate;display:inline-flex;align-items:center;gap:7px;box-sizing:border-box;margin:10px 0 0 8px;padding:13px 12px 13px 65px;min-height:58px;color:#111;white-space:nowrap;font-family:"Microsoft YaHei","PingFang SC",sans-serif}.ui-series-badge::before{content:"";position:absolute;z-index:-1;inset:0 0 0 32px;border:3px solid #171717;border-left:0;border-radius:0 22px 20px 0;background:#ffe477;box-shadow:2px 2px 0 #171717}.ui-series-avatar{position:absolute;left:0;bottom:0;width:61px;height:65px;object-fit:contain;object-position:bottom;border:0;border-radius:0}.ui-series-title{font-size:21px;line-height:1.2;font-weight:900;letter-spacing:-1px}.ui-series-dot{font-size:22px;font-weight:900}.ui-series-episode{padding:5px 7px;border:2px solid #171717;border-radius:12px;font-size:15px;line-height:1.2;font-weight:800}';
 items.push({name:'小白学编程 · 系列标签',aliases:'第一期 人物 角标 栏目 logo',category:'标签',origin:'用户封面参考 · Doodle Cream 系列角标',html:seriesHTML(seriesImage),css:seriesCSS,code:async()=>{
   const response=await fetch(seriesImage);if(!response.ok)throw Error('人物图片加载失败');
   const blob=await response.blob();
   const data=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=()=>reject(Error('人物图片读取失败'));reader.readAsDataURL(blob)});
   return '<style>'+seriesCSS+'</style>\n'+seriesHTML(data);
 }});
 const personCSS='.ui-person-asset{display:inline-grid;place-items:center;width:148px;height:148px;overflow:visible}.ui-person-asset img,.ui-person-asset svg{display:block;width:100%;height:100%;object-fit:contain}';
 function personItem(file,name,aliases,origin='卷卷姐人物素材 · SVG 矢量路径'){
   const image=new URL('assets/'+file,location.href).href;
   const html=src=>'<span class="ui-person-asset" role="img" aria-label="'+name+'"><img src="'+src+'" alt=""></span>';
   return {name,aliases,category:'人物',origin,html:html(image),css:personCSS,previewBackground:'#faf9f6',code:async()=>{
     const response=await fetch(image);if(!response.ok)throw Error('人物图片加载失败');
     if(file.toLowerCase().endsWith('.svg')){
       const svg=await response.text();
       return '<style>'+personCSS+'</style>\n<span class="ui-person-asset" role="img" aria-label="'+name+'">'+svg+'</span>';
     }
     const blob=await response.blob();
     const data=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=()=>reject(Error('人物图片读取失败'));reader.readAsDataURL(blob)});
     return '<style>'+personCSS+'</style>\n'+html(data);
   }};
 }
 items.push(
   personItem('juanjuanjie/juanjuanjie-explaining.svg','卷卷姐 · 举手讲解抠图','卷卷姐 人物 矢量 SVG 举手 指引 讲解 开心 黑白 条纹'),
   personItem('juanjuanjie/juanjuanjie-thinking.svg.png','卷卷姐 · 托腮思考','卷卷姐 人物 PNG 透明抠图 思考 琢磨 犹豫 托腮 黑白 条纹','卷卷姐人物素材 · PNG 透明抠图'),
   personItem('juanjuanjie/juanjuanjie-reaching.svg','卷卷姐 · 伸手指引','卷卷姐 人物 矢量 SVG 全身 伸手 指引 展示 介绍 黑白 条纹'),
   personItem('juanjuanjie/juanjuanjie-surprised-closeup.svg','卷卷姐 · 惊讶特写','卷卷姐 人物 矢量 SVG 惊讶 特写 意外 张嘴 黑白 条纹'),
   personItem('juanjuanjie/juanjuanjie-concerned.svg','卷卷姐 · 担忧','卷卷姐 人物 矢量 SVG 担忧 严肃 困惑 无奈 黑白 条纹'),
   personItem('juanjuanjie/juanjuanjie-questioning.svg','卷卷姐 · 疑问','卷卷姐 人物 矢量 SVG 疑问 问号 思考 困惑 黑白 条纹'),
   personItem('juanjuanjie/juanjuanjie-surprised.svg','卷卷姐 · 惊讶','卷卷姐 人物 矢量 SVG 惊讶 意外 张嘴 黑白 条纹'),
   personItem('juanjuanjie/juanjuanjie-daydreaming.svg','卷卷姐 · 托腮微笑','卷卷姐 人物 矢量 SVG 托腮 微笑 期待 开心 黑白 条纹')
 );
 const westieImage=new URL('assets/juan-westie-mascot.png',location.href).href;
 const westieHTML=src=>'<span class="ui-juan-westie" role="img" aria-label="卷饼灵感吉祥物"><img src="'+src+'" alt=""></span>';
 const westieCSS='.ui-juan-westie{display:inline-grid;place-items:center;width:148px;height:148px;overflow:visible;transform-origin:50% 88%;animation:ui-westie-float 3.2s ease-in-out infinite}.ui-juan-westie img{display:block;width:100%;height:100%;object-fit:contain}.ui-juan-westie:hover{animation:ui-westie-cheer .55s ease-in-out 2}@keyframes ui-westie-float{0%,100%{transform:translateY(2px) rotate(-.7deg)}50%{transform:translateY(-4px) rotate(.7deg)}}@keyframes ui-westie-cheer{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-9px) scale(1.045)}}@media(prefers-reduced-motion:reduce){.ui-juan-westie{animation:none}}';
 items.push({name:'卷饼 · 灵感吉祥物',aliases:'卷饼 角色 动物 卡通 西高地 白梗 狗狗 灵感 教程 mascot westie',category:'角色',origin:'原创品牌吉祥物 · 卷饼 · 西高地白梗 × 极简黑白画风',html:westieHTML(westieImage),css:westieCSS,previewBackground:'#faf9f6',code:async()=>{
   const response=await fetch(westieImage);if(!response.ok)throw Error('吉祥物图片加载失败');
   const blob=await response.blob();
   const data=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=()=>reject(Error('吉祥物图片读取失败'));reader.readAsDataURL(blob)});
   return '<style>'+westieCSS+'</style>\n'+westieHTML(data);
 }});
 for(const [id,name,aliases] of LogoLibrary.entries)items.push({name,aliases,category:'Logo',origin:'本地 Logo 素材 · '+LogoLibrary.path(id).split('/').pop(),id,code:async()=>'<img alt="'+name+'" src="'+await LogoLibrary.asset(id)+'" style="width:64px;height:64px;object-fit:contain">'});
 let category='全部',selected,timer,detailTicket=0;
 for(const motion of window.MotionLibrary||[])items.push({name:motion.name,category:'动效',origin:'动效参考 · '+motion.tech.join(' / '),aliases:motion.scene+' '+motion.tech.join(' '),motion,code:()=>Promise.resolve(motion.demo())});
 const copyIcon='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="3"/><path d="M15 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h3"/></svg>';
 function feedback(message){clearTimeout(timer);status.textContent=message;status.hidden=false;timer=setTimeout(()=>status.hidden=true,2800)}
 async function copy(item,prompt=false){
  try{
   let text=await item.code();
   if(prompt)text='参照下方代码生成单个可复用的小装饰元素（'+item.name+'）。只输出该元素的 HTML/CSS 或 SVG，不生成页面、卡片布局或幻灯片。不设置 body 等全局样式。保留手绘轮廓，背景透明，可调整尺寸颜色。'+(item.category==='Logo'?'品牌 Logo 必须原样复用，不改变品牌造型。':'')+'需求：保留此样式\n参考元素：\n'+text;
   if(prompt && item.motion)text='复用以下动效，保留动画行为和依赖，适配我的 HTML。适用场景：'+item.motion.scene+'。交付可运行代码，说明外部依赖。\n参考源码：\n'+await item.code();
   try{await navigator.clipboard.writeText(text);feedback(prompt?'提示词已复制':'元素代码已复制')}
   catch{$('manual-text').value=text;$('manual').showModal();$('manual-text').focus();$('manual-text').select()}
  }catch(e){feedback(e.message)}
 }
 function preview(item){
  const box=document.createElement('div');box.className='preview';
  if(item.previewBackground)box.style.background=item.previewBackground;
  if(item.motion){box.classList.add('motion-preview');const frame=document.createElement('iframe');frame.title=item.name+'动效预览';frame.loading='lazy';frame.tabIndex=-1;frame.setAttribute('sandbox','allow-scripts');frame.srcdoc=item.motion.demo();box.append(frame);return box;}
  if(item.id){const img=document.createElement('img');img.alt='';img.src=LogoLibrary.path(item.id);box.append(img)}
  else {const frame=document.createElement('iframe');frame.title=item.name+'预览';frame.tabIndex=-1;frame.setAttribute('sandbox','');frame.srcdoc='<!doctype html><html><meta charset="utf-8"><style>html,body{margin:0;height:100%;overflow:hidden}body{display:grid;place-items:center;background:transparent}.stage{transform:scale(.72);display:grid;place-items:center}'+item.css+'</style><body><div class="stage">'+item.html+'</div></body></html>';box.append(frame)}
  return box;
 }
 async function details(item){
  selected=item;const ticket=++detailTicket;$('detail-title').textContent=item.name;$('detail-origin').textContent=item.origin;
  $('detail-class').textContent=item.motion?(item.motion.libs.length?'依赖：'+item.motion.libs.join(' · ')+'（预览需联网）':'内嵌 SVG / CSS · 无外部依赖 · 自动循环'):item.html?'CSS 类名：'+(item.html.match(/class="([^"]+)"/)?.[1]||'独立 SVG'):'内嵌 Logo 图片';
  $('detail-preview').replaceChildren(preview(item));$('detail-code').value='加载中…';$('detail').showModal();
  try{const code=await item.code();if(ticket===detailTicket)$('detail-code').value=code}catch(e){if(ticket===detailTicket)$('detail-code').value=e.message}
 }
 function render(){
  const q=$('search').value.trim().toLowerCase(),matches=items.filter(i=>(category==='全部'||i.category===category)&&[i.name,i.aliases||'',i.category,i.origin].join(' ').toLowerCase().includes(q));
  $('elements').replaceChildren();$('empty').hidden=matches.length>0;
  for(const item of matches){
   const card=document.createElement('article');card.className='asset-card';
   const open=document.createElement('button');open.className='asset-open';open.setAttribute('aria-label','查看'+item.name+'详情');open.append(preview(item));
   const name=document.createElement('span');name.className='asset-name';name.textContent=item.name;open.append(name);open.onclick=()=>details(item);card.append(open);
   const quick=document.createElement('button');quick.className='quick-copy';quick.innerHTML=copyIcon;quick.title='复制代码';quick.setAttribute('aria-label','复制'+item.name+'代码');quick.onclick=()=>copy(item);card.append(quick);
   const prompt=document.createElement('button');prompt.className='quick-prompt';prompt.textContent='复制提示词';prompt.onclick=()=>copy(item,true);card.append(prompt);
   $('elements').append(card);
  }
 }
 for(const name of ['全部','人物','角色','图形','按钮','标签','箭头','文字效果','图标','Logo','动效'].filter(n=>n==='全部'||items.some(i=>i.category===n))){
  const b=document.createElement('button');b.textContent=name;b.setAttribute('aria-pressed',String(name===category));b.onclick=()=>{category=name;for(const el of $('filters').children)el.setAttribute('aria-pressed',String(el===b));render()};$('filters').append(b);
 }
 $('search').oninput=render;
 $('transparent').onchange=()=>document.body.classList.toggle('checker',$('transparent').checked);
 $('detail-copy').onclick=()=>copy(selected);$('detail-prompt').onclick=()=>copy(selected,true);
 $('detail').addEventListener('close',()=>{$('detail-preview').replaceChildren();detailTicket++});
 for(const dialog of document.querySelectorAll('dialog')){dialog.querySelector('[data-close]').onclick=()=>dialog.close();dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}})}
 render();
})();
