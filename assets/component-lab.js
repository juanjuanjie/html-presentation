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
 for(const name of ['全部','图形','标签','箭头','文字效果','图标','Logo','动效'].filter(n=>n==='全部'||items.some(i=>i.category===n))){
  const b=document.createElement('button');b.textContent=name;b.setAttribute('aria-pressed',String(name===category));b.onclick=()=>{category=name;for(const el of $('filters').children)el.setAttribute('aria-pressed',String(el===b));render()};$('filters').append(b);
 }
 $('search').oninput=render;
 $('transparent').onchange=()=>document.body.classList.toggle('checker',$('transparent').checked);
 $('detail-copy').onclick=()=>copy(selected);$('detail-prompt').onclick=()=>copy(selected,true);
 $('detail').addEventListener('close',()=>{$('detail-preview').replaceChildren();detailTicket++});
 for(const dialog of document.querySelectorAll('dialog')){dialog.querySelector('[data-close]').onclick=()=>dialog.close();dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}})}
 render();
})();
