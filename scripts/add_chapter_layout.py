"""Add the optional chapter divider to bundled templates, retaining existing slides."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CSS = '''
/* Chapter divider: independent of the original transition layouts. */
.slide.chapter-slide{background:var(--chapter-paper);color:var(--chapter-ink);padding:0}
.chapter-layout{position:absolute;inset:16% 8% 24%;display:flex;flex-direction:column;justify-content:space-between;text-align:left}
.chapter-heading{display:grid;grid-template-columns:22% minmax(0,1fr);align-items:center;gap:3.5%;min-height:52%}
.chapter-number{font-size:clamp(72px,13vw,250px);font-weight:700;font-style:italic;line-height:1;color:var(--chapter-accent);letter-spacing:-.06em}
.chapter-copy{border-left:3px solid var(--chapter-ink);padding:1.5vw 0 1.5vw 3vw;min-width:0}
.chapter-copy .chapter-kicker{margin:0 0 2vw;color:var(--chapter-accent);font-size:clamp(14px,1.8vw,34px);font-style:italic;letter-spacing:.08em}
.chapter-copy .chapter-title{margin:0;color:var(--chapter-ink);font-size:clamp(30px,4.8vw,92px);line-height:1.2;letter-spacing:0;overflow-wrap:anywhere}
.chapter-copy .chapter-description{margin:1.5vw 0 0;color:var(--chapter-muted);font-size:clamp(16px,2.1vw,40px);line-height:1.4}
.chapter-track{display:flex;list-style:none!important;margin:3vw 0 0!important;padding:0!important;width:100%}
.chapter-track li{position:relative;flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:1.5vw;padding:0!important;margin:0!important;color:var(--chapter-muted);text-align:center;font-size:clamp(12px,1.4vw,27px);line-height:1.3}
.chapter-track li::before{content:'';position:absolute;top:calc(1.82vw + 1.5vw + 8px);left:0;width:100%;height:2px;background:var(--chapter-muted);opacity:.45}
.chapter-track li:first-child::before{left:50%;width:50%}.chapter-track li:last-child::before{width:50%}
.chapter-track .chapter-index{font-size:1.4vw;line-height:1.3;font-style:italic}
.chapter-dot{position:relative;z-index:1;display:grid;place-items:center;width:18px;height:18px;box-sizing:border-box;border:2px solid var(--chapter-muted);border-radius:47% 53% 49% 51%;background:var(--chapter-paper);font:700 12px/1 sans-serif}
.chapter-track .is-complete .chapter-dot{background:var(--chapter-ink);border-color:var(--chapter-ink);color:var(--chapter-paper)}
.chapter-track .is-current{color:var(--chapter-accent);font-weight:700}
.chapter-track .is-current .chapter-dot{background:var(--chapter-accent);border-color:var(--chapter-accent);transform:scale(1.5)}
.chapter-name{max-width:95%;overflow-wrap:anywhere}
@media(max-width:600px){.chapter-layout{inset:16% 7% 24%}.chapter-heading{grid-template-columns:22% minmax(0,1fr)}.chapter-number{font-size:17vw}.chapter-copy .chapter-title{font-size:7vw}.chapter-copy .chapter-description{font-size:3.4vw}.chapter-track{flex-wrap:wrap;row-gap:20px}.chapter-track li{flex:0 0 25%;font-size:12px;gap:10px}.chapter-track .chapter-index{font-size:12px}.chapter-track li::before{top:34px}.chapter-track li:nth-child(4)::before{width:50%}.chapter-track li:nth-child(5)::before{left:50%;width:50%}}
'''
LABELS = ['开场', '核心问题', '方法', '案例', '实践', '进阶', '回顾', '下一步']
TRACK = ''.join(f'<li class="{"is-complete" if i == 0 else "is-current" if i == 1 else "is-upcoming"}"'+(' aria-current="step"' if i == 1 else '')+f'><span class="chapter-index">{i+1:02}</span><span class="chapter-dot" aria-hidden="true">'+('✓' if i == 0 else '')+f'</span><span class="chapter-name">{label}</span></li>' for i, label in enumerate(LABELS))
HTML = f'''<section class="slide chapter-slide" data-layout="chapter" data-caption="第二章，先找到真正要解决的问题。">
      <div class="chapter-layout">
        <div class="chapter-heading"><div class="chapter-number" aria-hidden="true">02</div><div class="chapter-copy"><p class="chapter-kicker">CHAPTER 02 / 08</p><h2 class="chapter-title">找到核心问题</h2><p class="chapter-description">从观察现象，到明确方向</p></div></div>
        <ol class="chapter-track" aria-label="章节进度">{TRACK}</ol>
      </div>
    </section>

    '''

def main():
    files = list((ROOT / 'themes').glob('*/template.html'))
    for p in files:
        s = p.read_text(encoding='utf-8')
        if 'data-layout="chapter"' in s:
            continue
        slug = p.parent.name
        if slug.startswith('doodle'):
            palette = 'var(--paper)', 'var(--ink)', 'var(--yellow)', 'var(--muted)'
        elif slug == 'blockframe':
            palette = 'var(--offwhite)', 'var(--black)', 'var(--yellow)', 'color-mix(in srgb,var(--black) 65%,var(--offwhite))'
        elif slug == 'blockframe-dark':
            palette = 'var(--black)', 'var(--white)', 'var(--yellow)', 'var(--muted)'
        else:
            palette = 'var(--bg)', 'var(--text)', 'var(--primary,var(--title))', 'var(--text-muted,var(--text-secondary))'
        variables = '.chapter-slide{' + ';'.join(f'--chapter-{k}:{v}' for k,v in zip(['paper','ink','accent','muted'],palette)) + '}\n'
        s = s.replace('</style>', variables + CSS + '</style>', 1)
        matches = [m for m in re.finditer(r'<(?:section|div)\b[^>]*class="([^"]*)"[^>]*>', s) if 'slide' in m[1].split()]
        s = s[:matches[-1].start()] + HTML + s[matches[-1].start():]
        p.write_text(s, encoding='utf-8')
        meta = p.with_name('template.json')
        if meta.exists():
            data = json.loads(meta.read_text(encoding='utf-8'))
            data['slide_count'] = len(matches) + 1
            meta.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
