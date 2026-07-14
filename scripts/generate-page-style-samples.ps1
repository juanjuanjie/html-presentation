param(
    [string]$OutputRoot
)

$ErrorActionPreference = "Stop"
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillRoot = Split-Path -Parent $scriptRoot
if (-not $OutputRoot) {
    $OutputRoot = Join-Path $skillRoot "assets\previews\page-style-samples"
}
New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

function Write-Utf8File {
    param(
        [string]$Path,
        [string]$Content
    )
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Wrap-Page {
    param(
        [string]$Title,
        [string]$Css,
        [string]$Body
    )
    return @"
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$Title</title>
<style>
*{box-sizing:border-box}
html,body{margin:0;height:100%;overflow:hidden}
body{display:grid;place-items:center;background:#111;font-family:"Microsoft YaHei","PingFang SC",Arial,sans-serif}
.stage{position:relative;width:min(100vw,177.7778vh);height:min(100vh,56.25vw);overflow:hidden}
$Css
</style>
</head>
<body>
$Body
</body>
</html>
"@
}

$samples = @()

$css = @'
.stage{background:#fff;color:#17223b}
.top{position:absolute;left:0;right:0;top:0;height:13%;background:#062662}
.logo{position:absolute;right:7%;top:3.6%;background:#fff;color:#062662;padding:.55em 2.2em;font-weight:900;letter-spacing:.08em;font-size:clamp(18px,2.1vw,34px)}
.title{position:absolute;left:7%;top:5.1%;color:#fff}
.title h1{margin:0;font-size:clamp(26px,3.2vw,56px);letter-spacing:.02em}
.title p{margin:.5em 0 0;color:#dce8f7;font-size:clamp(13px,1.2vw,22px)}
.grid{position:absolute;left:7%;right:7%;top:21%;bottom:18%;display:grid;grid-template-columns:1fr 1fr;gap:4.2% 5%}
.q{border-top:3px solid #194b9b;padding:1.3em 1em 1em 0}
.q h2{margin:0 0 .7em;color:#0b3a8a;font-size:clamp(18px,1.8vw,32px)}
.q p{margin:0;color:#3f4a5f;line-height:1.72;font-size:clamp(13px,1.12vw,21px)}
.wave{position:absolute;left:-8%;right:-8%;bottom:5%;height:15%;background:
radial-gradient(70% 85% at 25% 100%,rgba(158,187,226,.34) 0 42%,transparent 43%),
radial-gradient(70% 85% at 75% 100%,rgba(102,148,207,.34) 0 42%,transparent 43%),
#edf4fb;clip-path:ellipse(62% 58% at 50% 100%)}
.footer{position:absolute;left:0;right:0;bottom:0;height:5%;background:#062662;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 7%;font-size:clamp(10px,.9vw,16px);font-weight:700}
'@
$body = @'
<section class="stage">
  <div class="top"></div><div class="logo">MFLEX</div>
  <div class="title"><h1>项目周报 / 工作汇报</h1><p>MFLEX 蓝白项目汇报 · 四象限信息结构</p></div>
  <div class="grid">
    <div class="q"><h2>01 本周进展</h2><p>完成核心流程联调，关键数据链路进入稳定验证阶段，交付节奏清晰。</p></div>
    <div class="q"><h2>02 关键数据</h2><p>任务完成率 82%，阻塞项 3 个，风险等级保持可控，下一步聚焦闭环。</p></div>
    <div class="q"><h2>03 风险问题</h2><p>设备一致性、参数版本和现场操作习惯仍需通过 SOP 固化。</p></div>
    <div class="q"><h2>04 下周计划</h2><p>完成复测、交付检查和文档同步，形成可复用流程模板。</p></div>
  </div>
  <div class="wave"></div><div class="footer"><span>MFLEX · WEEKLY REPORT</span><span>01 / 06</span></div>
</section>
'@
$samples += @{ File="01_weekly_report_mflex.html"; Title="MFLEX 蓝白项目汇报"; Html=(Wrap-Page "MFLEX 蓝白项目汇报" $css $body) }

$css = @'
.stage{background:#0d0c0a;color:#efe3c9}
.stage:before{content:"";position:absolute;inset:4%;border:1px solid rgba(216,167,79,.55)}
.stage:after{content:"";position:absolute;inset:0;background:
radial-gradient(circle at 28% 62%,rgba(216,167,79,.18),transparent 24%),
radial-gradient(circle at 54% 62%,rgba(69,215,207,.16),transparent 23%),
radial-gradient(circle at 77% 62%,rgba(154,114,255,.17),transparent 24%),
repeating-radial-gradient(circle at 50% 50%,rgba(255,255,255,.025) 0 1px,transparent 1px 4px);pointer-events:none}
.inner{position:absolute;inset:9%;z-index:1}
.kicker{text-align:center;color:#b7a78c;letter-spacing:.22em;font-size:clamp(10px,.95vw,16px)}
h1{text-align:center;margin:.26em 0 .12em;font-family:Georgia,"Times New Roman",serif;font-size:clamp(34px,5.3vw,88px);font-weight:500;color:#f5dec0}
.sub{text-align:center;color:#d8a74f;font-style:italic;font-size:clamp(15px,1.35vw,24px)}
.diamond{width:.75em;height:.75em;background:#d8a74f;transform:rotate(45deg);margin:2.1em auto}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:4%;margin-top:3%}
.col{min-height:44%;padding:2em 1.5em;border-top:1px solid rgba(216,167,79,.55);border-bottom:1px solid rgba(216,167,79,.28);background:rgba(255,255,255,.025)}
.col h2{margin:0 0 1em;font-size:clamp(18px,1.8vw,30px);font-weight:700}
.gold h2{color:#d8a74f}.cyan h2{color:#45d7cf}.purple h2{color:#9a72ff}
.col p{margin:0;color:#c9b99b;line-height:1.8;font-size:clamp(13px,1.1vw,19px)}
.meta{position:absolute;left:9%;right:9%;bottom:7%;display:flex;justify-content:space-between;color:#8f7e63;font-size:clamp(10px,.85vw,15px);z-index:2}
'@
$body = @'
<section class="stage">
  <div class="inner">
    <div class="kicker">DARK GOLD INSIGHT</div>
    <h1>数据之光，洞见未来</h1>
    <div class="sub">Insight / Filter / Model</div>
    <div class="diamond"></div>
    <div class="cols">
      <div class="col gold"><h2>主观 · 洞察</h2><p>数据不是结论，而是打开问题的镜面。先看趋势，再追问异常背后的机制。</p></div>
      <div class="col cyan"><h2>筛选 · 过滤</h2><p>去掉噪声、重复和伪相关，让真正有解释力的信号浮出水面。</p></div>
      <div class="col purple"><h2>建模 · 预测</h2><p>用结构化假设连接过去与未来，把判断转化为可复核的行动。</p></div>
    </div>
  </div>
  <div class="meta"><span>FIELD NOTE 02</span><span>暗金数据洞察</span></div>
</section>
'@
$samples += @{ File="02_dark_gold_insight.html"; Title="暗金数据洞察"; Html=(Wrap-Page "暗金数据洞察" $css $body) }

$css = @'
.stage{background:#f7f5ef;color:#111}
.stage:before{content:"";position:absolute;inset:0;background:
linear-gradient(rgba(0,0,0,.025) 1px,transparent 1px),
linear-gradient(90deg,rgba(0,0,0,.018) 1px,transparent 1px);background-size:22px 22px;opacity:.8}
.left{position:absolute;left:7%;top:14%;width:42%;z-index:2}
.label{display:inline-block;background:#111;color:#f7f5ef;padding:.45em .8em;border-radius:999px;font-weight:900;font-size:clamp(11px,.9vw,16px)}
h1{margin:.34em 0 .16em;font-size:clamp(46px,7.2vw,118px);line-height:.9;letter-spacing:-.03em;font-weight:1000}
.note{max-width:78%;font-size:clamp(14px,1.25vw,22px);line-height:1.65;color:#2c2c2c}
.tags{display:flex;gap:.8em;flex-wrap:wrap;margin-top:2em}
.tag{background:#efd49b;border:1px solid rgba(0,0,0,.16);border-radius:999px;padding:.45em .9em;font-weight:800;font-size:clamp(11px,.9vw,16px)}
.panel{position:absolute;right:8%;top:12%;width:39%;height:70%;background:#fff;box-shadow:0 20px 42px rgba(0,0,0,.18);transform:rotate(-2deg);padding:3.2em 2.5em;z-index:2}
.panel:before{content:"";position:absolute;left:-7%;top:12%;width:34%;height:22%;background:#f2ead9;box-shadow:0 8px 18px rgba(0,0,0,.12);transform:rotate(9deg)}
.panel:after{content:"";position:absolute;right:-6%;bottom:10%;width:38%;height:28%;background:#b89c72;opacity:.75;transform:rotate(7deg)}
.paper{position:relative;z-index:1;border-left:5px solid #111;padding-left:1.1em}
.paper h2{margin:0 0 .8em;font-size:clamp(22px,2.3vw,42px)}
.paper p{font-size:clamp(14px,1.15vw,21px);line-height:1.85;color:#2c2c2c}
.stamp{position:absolute;right:9%;top:9%;border:2px solid #111;padding:.35em .55em;font-weight:1000;transform:rotate(8deg)}
'@
$body = @'
<section class="stage">
  <div class="left">
    <span class="label">RAW PAPER NOTES</span>
    <h1>未完成的<br>想法现场</h1>
    <p class="note">米白纸面、粗黑标题、扫描纹理和拼贴块，保留草稿状态里的判断痕迹。</p>
    <div class="tags"><span class="tag">draft</span><span class="tag">scan</span><span class="tag">anti-polish</span></div>
  </div>
  <div class="panel">
    <div class="stamp">V2</div>
    <div class="paper"><h2>纸感故事板</h2><p>把摘录、批注和临时结论放在同一张纸上，不追求完美排版，而强调思考正在发生。</p></div>
  </div>
</section>
'@
$samples += @{ File="03_raw_paper_notes.html"; Title="Raw Paper 米白黑纸感文本笔记"; Html=(Wrap-Page "Raw Paper 米白黑纸感文本笔记" $css $body) }

$css = @'
.stage{background:linear-gradient(90deg,#f3e9e5 0 50%,#d9f3ff 50% 100%);color:#10182d}
.left{position:absolute;left:7%;top:12%;width:38%;z-index:3}
.eyebrow{font-weight:900;letter-spacing:.16em;color:#2536d9;font-size:clamp(12px,1vw,18px)}
h1{font-size:clamp(46px,6.8vw,116px);line-height:.92;margin:.18em 0;font-weight:1000;letter-spacing:-.04em}
.lead{font-size:clamp(15px,1.35vw,24px);line-height:1.65;max-width:86%}
.panel{position:absolute;right:7%;top:10%;width:43%;height:77%;background:#fff;border-radius:28px;box-shadow:0 28px 70px rgba(18,35,80,.2);overflow:hidden}
.shape{position:absolute;border-radius:24px}
.blue{left:12%;top:12%;width:54%;height:23%;background:#2536d9}
.violet{right:10%;top:25%;width:48%;height:24%;background:#4b4cf2}
.orange{left:18%;top:45%;width:62%;height:18%;background:#ff7416}
.peach{right:8%;bottom:9%;width:56%;height:25%;background:#ffd9bd}
.whitecard{position:absolute;left:10%;bottom:12%;width:48%;background:#fff;border-radius:18px;padding:1.2em;box-shadow:0 18px 42px rgba(16,24,45,.2);font-weight:900}
.info{position:absolute;left:10%;right:10%;top:70%;display:grid;grid-template-columns:repeat(3,1fr);gap:.8em}
.info div{font-size:clamp(10px,.9vw,15px);font-weight:900;color:#10182d}
.pill{display:inline-block;margin-top:1.8em;background:#10182d;color:#fff;border-radius:999px;padding:.75em 1.1em;font-weight:900}
'@
$body = @'
<section class="stage">
  <div class="left">
    <div class="eyebrow">SOCIAL COVER V2A</div>
    <h1>DIMENSIONAL<br>LAYERING</h1>
    <p class="lead">蓝紫橙高饱和色块叠加白色面板，适合观点封面、课程首屏和视觉卡片。</p>
    <span class="pill">high contrast / stacked cards</span>
  </div>
  <div class="panel">
    <div class="shape blue"></div><div class="shape violet"></div><div class="shape orange"></div><div class="shape peach"></div>
    <div class="whitecard">Layer 03<br><span style="color:#ff7416">Key Point</span></div>
    <div class="info"><div>01 Depth</div><div>02 Focus</div><div>03 Impact</div></div>
  </div>
</section>
'@
$samples += @{ File="04_social_card_layering_v2a.html"; Title="自媒体 V2a 蓝紫橙层叠卡片"; Html=(Wrap-Page "自媒体 V2a 蓝紫橙层叠卡片" $css $body) }

$css = @'
.stage{background:#f1f4f8;color:#1f2d3d;padding:5% 6%}
.header{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:2.4%}
h1{margin:0;font-size:clamp(28px,3.8vw,68px);line-height:1;font-weight:1000}
.date{color:#718096;font-weight:800;font-size:clamp(12px,1vw,18px)}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:1.4%;height:24%}
.card{background:#fff;border:1px solid #dfe6ef;border-radius:18px;padding:1.25em;box-shadow:0 14px 32px rgba(31,45,61,.08)}
.num{font-size:clamp(26px,3vw,54px);font-weight:1000;color:#f15a24}
.card p{margin:.4em 0 0;color:#718096;font-size:clamp(12px,1vw,18px)}
.main{display:grid;grid-template-columns:1fr 1.25fr;gap:2%;height:49%;margin-top:2%}
.progress,.feed{background:#fff;border-radius:20px;border:1px solid #dfe6ef;padding:1.7em}
.ring{width:min(22vw,34vh);aspect-ratio:1;margin:1.2em auto;border-radius:50%;background:conic-gradient(#f15a24 0 72%,#e6edf5 72%);display:grid;place-items:center}
.ring span{width:72%;height:72%;border-radius:50%;background:#fff;display:grid;place-items:center;font-size:clamp(24px,3vw,54px);font-weight:1000;color:#f15a24}
h2{margin:0;color:#1f2d3d;font-size:clamp(18px,1.7vw,30px)}
.item{display:grid;grid-template-columns:auto 1fr auto;gap:1em;align-items:center;border-bottom:1px solid #dfe6ef;padding:1em 0;font-size:clamp(12px,1vw,18px)}
.dot{width:.75em;height:.75em;border-radius:50%;background:#f15a24}.status{color:#718096;font-weight:800}
.footer{position:absolute;left:6%;right:6%;bottom:3.4%;color:#718096;font-weight:800;font-size:clamp(11px,.9vw,16px)}
'@
$body = @'
<section class="stage">
  <div class="header"><h1>项目看板 · 本周节奏</h1><div class="date">V2B DASHBOARD / 2026</div></div>
  <div class="metrics">
    <div class="card"><div class="num">82%</div><p>任务完成率</p></div>
    <div class="card"><div class="num">18</div><p>已关闭事项</p></div>
    <div class="card"><div class="num">03</div><p>待处理风险</p></div>
    <div class="card"><div class="num">6.4h</div><p>平均响应</p></div>
  </div>
  <div class="main">
    <div class="progress"><h2>整体进度</h2><div class="ring"><span>72%</span></div></div>
    <div class="feed"><h2>近期动态</h2><div class="item"><span class="dot"></span><b>SOP 复测完成</b><span class="status">Done</span></div><div class="item"><span class="dot"></span><b>参数文件归档</b><span class="status">Today</span></div><div class="item"><span class="dot"></span><b>交付清单确认</b><span class="status">Next</span></div></div>
  </div>
  <div class="footer">浅灰白橙仪表盘信息流 · metric cards / progress / activity</div>
</section>
'@
$samples += @{ File="05_social_dashboard_v2b.html"; Title="自媒体 V2b 浅灰白橙仪表盘"; Html=(Wrap-Page "自媒体 V2b 浅灰白橙仪表盘" $css $body) }

$css = @'
.stage{background:
radial-gradient(circle at 18% 22%,rgba(255,59,152,.35),transparent 22%),
radial-gradient(circle at 78% 30%,rgba(16,215,232,.38),transparent 24%),
radial-gradient(circle at 66% 78%,rgba(77,45,131,.55),transparent 28%),
linear-gradient(135deg,#071324 0%,#111044 46%,#061a2a 100%);color:#f5f7ff}
.stage:before{content:"";position:absolute;inset:0;background:linear-gradient(120deg,transparent,rgba(255,255,255,.08),transparent);filter:blur(1px)}
.left{position:absolute;left:7%;top:18%;width:43%;z-index:2}
.kicker{color:#10d7e8;font-weight:900;letter-spacing:.18em;font-size:clamp(12px,1vw,18px)}
h1{font-size:clamp(44px,6.2vw,108px);line-height:.98;margin:.25em 0;font-weight:1000}
.lead{color:#cbd1e2;font-size:clamp(15px,1.35vw,24px);line-height:1.65;max-width:82%}
.glass{position:absolute;right:8%;top:15%;width:38%;height:68%;border:1px solid rgba(255,255,255,.24);background:rgba(255,255,255,.14);backdrop-filter:blur(18px);border-radius:30px;box-shadow:0 28px 80px rgba(0,0,0,.35);padding:2em;z-index:2}
.orb{position:absolute;border-radius:50%;filter:blur(2px);opacity:.9}.o1{right:32%;top:9%;width:9%;aspect-ratio:1;background:#10d7e8}.o2{right:7%;bottom:13%;width:12%;aspect-ratio:1;background:#ff3b98}
.glass h2{font-size:clamp(24px,2.6vw,48px);margin:.2em 0 .9em}
.mini{display:grid;gap:1em}
.mini div{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.18);border-radius:18px;padding:1.1em;color:#f5f7ff;font-weight:800;font-size:clamp(12px,1vw,18px)}
.chip{display:inline-block;margin-top:2em;border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:.75em 1em;color:#f5f7ff;font-weight:900}
'@
$body = @'
<section class="stage">
  <div class="left">
    <div class="kicker">AURORA UI</div>
    <h1>极光科技<br>界面语言</h1>
    <p class="lead">深蓝、黑紫、青色与粉色柔光叠加，配合玻璃拟态面板，形成沉浸式科技封面。</p>
    <span class="chip">glass panel / neon glow / dark depth</span>
  </div>
  <div class="orb o1"></div><div class="orb o2"></div>
  <div class="glass">
    <h2>Signal Stack</h2>
    <div class="mini"><div>01 · Real-time Insight</div><div>02 · Generative Workflow</div><div>03 · Adaptive Interface</div></div>
  </div>
</section>
'@
$samples += @{ File="06_aurora_ui.html"; Title="Aurora UI 极光科技"; Html=(Wrap-Page "Aurora UI 极光科技" $css $body) }

foreach ($sample in $samples) {
    Write-Utf8File -Path (Join-Path $OutputRoot $sample.File) -Content $sample.Html
}

$cards = ($samples | ForEach-Object {
    $file = $_.File
    $title = $_.Title
    @"
    <article class="card">
      <iframe src="$file" title="$title"></iframe>
      <div class="meta"><h2>$title</h2><a href="$file">打开单独文件</a></div>
    </article>
"@
}) -join "`n"

$index = @"
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>html-presentation page 风格样例总览</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#eef2f7;color:#111827;font-family:"Microsoft YaHei","PingFang SC",Arial,sans-serif}
header{padding:36px 44px 18px}
h1{margin:0;font-size:34px}
p{margin:10px 0 0;color:#5b6778}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;padding:24px 44px 44px}
.card{background:#fff;border:1px solid #d8e0ea;border-radius:12px;overflow:hidden;box-shadow:0 16px 36px rgba(15,23,42,.08)}
iframe{display:block;width:100%;aspect-ratio:16/9;border:0;background:#111}
.meta{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:16px 18px}
h2{font-size:18px;margin:0}
a{color:#0b3a8a;font-weight:800;text-decoration:none}
@media(max-width:980px){.grid{grid-template-columns:1fr;padding:18px}.meta{display:block}header{padding:26px 18px 10px}}
</style>
</head>
<body>
<header>
  <h1>html-presentation · page 风格样例总览</h1>
  <p>每个样例都是独立、可离线打开的 16:9 HTML 文件。</p>
</header>
<main class="grid">
$cards
</main>
</body>
</html>
"@
Write-Utf8File -Path (Join-Path $OutputRoot "index.html") -Content $index

"Generated $($samples.Count) sample files + index at $OutputRoot"

