window.LogoLibrary = {
 entries: [['vscode','VS Code','vscode|vs code|visual studio code'],['pycharm','PyCharm','pycharm'],['notion','Notion','notion'],['obsidian','Obsidian','obsidian|黑曜石']],
 path(id) { return 'assets/logos/'+id+(['notion','obsidian'].includes(id)?'.webp':'.svg'); },
 async asset(id) {
  const r=await fetch(this.path(id));if(!r.ok)throw Error('Logo 加载失败：'+id);
  if(!this.path(id).endsWith('.webp'))return 'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(await r.text());
  const bytes=new Uint8Array(await r.arrayBuffer());
  return 'data:image/webp;base64,'+btoa(Array.from(bytes,b=>String.fromCharCode(b)).join(''));
 },
 async prompt(text) {
  const normalized=text.toLowerCase().replace(/visual studio code/g,'vscode');
  const matches=this.entries.filter(([id,name,aliases])=>new RegExp('(^|[^a-z0-9])('+aliases+')(?=$|[^a-z0-9])','i').test(normalized));
  const assets=await Promise.all(matches.map(async ([id,name])=>name+': '+await this.asset(id)));
  return '【品牌 Logo 规则】优先原样复用以下真实 logo data URL，用 img 和 object-fit:contain，保留透明背景与原始比例。缺少的品牌先查 https://devicon.dev/ 或品牌官方网站，确认名称且成功下载图片后内嵌。禁止猜测 URL、手绘仿制 logo 或输出破损图片。无联网能力或找不到可靠素材时使用品牌文字，并在交付说明列出缺失项。视频图片必须内嵌，避免远程加载失败。\n'+assets.join('\n');
 }
};
