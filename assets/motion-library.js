/* Self-contained Doodle Cream motions. SVG viewBox fits both cards and dialogs. */
(() => {
 const ink='#292525',yellow='#ffe477';
 const common=`
 html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#fffdf5}
 body{display:grid;place-items:center}
 svg{display:block;width:100%;height:100%;max-width:640px}
 text{fill:${ink};font-family:"KaiTi","STKaiti","Microsoft YaHei",sans-serif}
 .line{fill:none;stroke:${ink};stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
 .yellow{fill:${yellow}}
 @keyframes rise{0%,8%,100%{transform:translateY(12px);opacity:0}24%,78%{transform:translateY(0);opacity:1}}
 @keyframes draw{0%,8%,100%{stroke-dashoffset:1}65%,86%{stroke-dashoffset:0}}
 @keyframes pop{0%,10%,100%{transform:scale(.85) rotate(-8deg)}40%,80%{transform:scale(1) rotate(3deg)}}
 @media(prefers-reduced-motion:reduce){svg *{animation:none!important;opacity:1!important;stroke-dashoffset:0!important}}
 `;
 function demo(content,css='',script=''){
  return '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+common+css+'</style><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img" aria-label="白纸暖黄循环动效">'+content+'</svg>'+(script?'<script>'+script+'</script>':'')+'</body></html>';
 }
 const entries=[
  ['echart-dynamic','手绘柱状图','数据报告、指标展示',
   '<path class="line" d="M62 35L61 140 264 140"/>'+[48,78,60,100].map((h,i)=>'<g transform="translate('+(84+i*43)+' 140)"><rect class="bar line yellow" x="0" y="-'+h+'" width="27" height="'+h+'" rx="5" style="animation-delay:'+i*.15+'s"/></g><text x="'+(97+i*43)+'" y="158" text-anchor="middle" font-size="12">Q'+(i+1)+'</text>').join(''),
   '.bar{animation:bars 3.6s ease-in-out infinite;transform-origin:0 0}@keyframes bars{0%,100%{transform:scaleY(.12)}40%,75%{transform:scaleY(1)}}'],
  ['stagger-text','手写文字入场','标题、金句',
   '<path class="farewell-highlight" d="M51 118Q160 111 269 117" fill="none" stroke="#ffe477" stroke-width="14" stroke-linecap="round" pathLength="1"/>'+['我','们','下','期','再','见'].map((t,i)=>'<text class="farewell-word word-'+i+'" x="'+(65+i*38)+'" y="104" text-anchor="middle" font-size="32" font-weight="700">'+t+'</text>').join(''),
   '.farewell-word{transform-box:fill-box;transform-origin:center;animation-duration:4.8s;animation-iteration-count:infinite;animation-fill-mode:both}.farewell-highlight{stroke-dasharray:1;animation:farewellInk 4.8s ease-in-out infinite}@keyframes farewellInk{0%,40%{stroke-dashoffset:1;opacity:0}41%{opacity:1;stroke-dashoffset:1}56%,88%{opacity:1;stroke-dashoffset:0}96%,100%{opacity:0;stroke-dashoffset:0}}'+Array.from({length:6},(_,i)=>'.word-'+i+'{animation-name:farewellPop'+i+'}@keyframes farewellPop'+i+'{0%,'+(4+i*4)+'%{opacity:0;transform:translateY(12px) scale(.35)}'+(11+i*4)+'%{opacity:1;transform:translateY(-3px) scale(1.18)}'+(17+i*4)+'%,88%{opacity:1;transform:translateY(0) scale(1)}96%,100%{opacity:0;transform:translateY(0) scale(1)}}').join('')],
  ['typewriter','手绘打字机','短句、口播重点',
   '<rect x="47" y="48" width="226" height="84" rx="15" fill="white" class="line"/><defs><clipPath id="reveal"><rect class="reveal" x="65" y="64" width="0" height="48"/></clipPath></defs><text x="65" y="101" font-size="26" font-weight="700" clip-path="url(#reveal)">从一个想法开始</text><path class="cursor line" d="M66 73V105"/>',
   '.reveal{animation:type 4s steps(7,end) infinite}.cursor{animation:cursor 4s steps(7,end) infinite}@keyframes type{0%,10%,100%{width:0}65%,90%{width:196px}}@keyframes cursor{0%,10%,100%{transform:translateX(0)}65%,90%{transform:translateX(196px)}}'],
  ['lottie-icon','手绘灵感灯泡','提示、灵感、重点',
   '<g class="bulb"><path class="yellow line" d="M139 106C136 91 120 87 125 66C130 37 178 35 190 59C201 82 184 92 181 106Z"/><path class="line" d="M140 114L180 113M145 123L175 123M153 133H168M151 102L146 78 160 86 173 77 168 102"/><g class="rays line"><path d="M160 20V10M111 34L103 26M95 65L82 63M206 36L217 27M220 66L234 64"/></g></g>',
   '.bulb{transform-origin:160px 90px;animation:pop 3s ease-in-out infinite}.rays{animation:rise 3s ease infinite}'],
  ['morph-grid','手绘色块变形','节奏过渡、布局变化',
   '<rect class="tile a line yellow" x="90" y="36" width="60" height="48" rx="12"/><rect class="tile b line" fill="#d8d6ff" x="169" y="36" width="60" height="48" rx="12"/><rect class="tile c line" fill="white" x="90" y="99" width="60" height="48" rx="12"/><rect class="tile d line yellow" x="169" y="99" width="60" height="48" rx="12"/>',
   '.tile{transform-box:fill-box;transform-origin:center;animation:morph 4s ease-in-out infinite}.b,.c{animation-delay:-2s}@keyframes morph{0%,100%{rx:12px;transform:rotate(-4deg)}50%{rx:25px;transform:rotate(8deg) scale(.85)}}'],
  ['counter','暖黄数字计数','数据亮点、成果',
   '<rect class="yellow" x="100" y="98" width="120" height="13"/><text id="number" x="160" y="108" text-anchor="middle" font-family="sans-serif" font-size="64" font-weight="700">0</text>',
   '',"const number=document.getElementById('number');const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;if(reduced){number.textContent='128';}else{let start;function tick(t){if(start===undefined)start=t;const phase=(t-start)%4000;const value=phase<2400?Math.round(128*(1-Math.pow(1-phase/2400,3))):128;number.textContent=value;requestAnimationFrame(tick)}requestAnimationFrame(tick);}"],
  ['svg-draw','手绘路径描绘','强调、路线指引',
   '<path class="yellow" d="M204 51Q238 35 260 66Q269 99 237 105Q207 104 204 78Z"/><path class="trace line" pathLength="1" d="M54 128C76 128 100 112 111 88S110 46 95 57S89 111 127 115S186 67 238 70M221 54L240 70 219 86"/>',
   '.trace{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 3.5s ease-in-out infinite}']
 ];
 window.MotionLibrary=entries.map(([id,name,scene,content,css,script])=>({id,name,scene,tech:['SVG','CSS 动画',...(script?['原生 JavaScript']:[])],libs:[],demo:()=>demo(content,css,script)}));
})();
