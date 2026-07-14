param(
    [string]$OutputRoot
)

$ErrorActionPreference = "Stop"
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillRoot = Split-Path -Parent $scriptRoot
if (-not $OutputRoot) {
    $OutputRoot = Join-Path $skillRoot "assets\previews\deck-theme-samples"
}
New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

function Write-Utf8File {
    param([string]$Path, [string]$Content)
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Wrap-Theme {
    param([string]$Title, [string]$Css, [string]$Body)
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
body{display:grid;place-items:center;background:#0f172a;font-family:"Inter","Space Grotesk","Microsoft YaHei","PingFang SC",Arial,sans-serif}
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
.stage{background:#FFFDF5;color:#000;padding:6.4%}
.hero{position:absolute;left:6.4%;top:8%;width:54%;background:#fff;border:4px solid #000;box-shadow:8px 8px 0 #000;padding:3.4em 3em;z-index:2}
.label{display:inline-block;border:4px solid #000;background:#F7CB46;box-shadow:4px 4px 0 #000;padding:.55em .85em;font-weight:900;letter-spacing:.08em;font-size:clamp(12px,1vw,18px)}
h1{font-size:clamp(48px,6vw,104px);line-height:.92;margin:.32em 0 .22em;font-weight:1000;text-transform:uppercase;letter-spacing:-.03em}
p{font-size:clamp(15px,1.18vw,22px);line-height:1.55;margin:0;max-width:82%}
.shape{position:absolute;border:4px solid #000;box-shadow:8px 8px 0 #000}
.pink{right:9%;top:14%;width:25%;height:23%;background:#FE90E8;transform:rotate(6deg)}
.blue{right:18%;top:44%;width:22%;height:22%;background:#C0F7FE;transform:rotate(-7deg)}
.green{right:7%;bottom:11%;width:30%;height:17%;background:#99E885}
.badge{position:absolute;right:13%;top:34%;background:#FFDC8B;border:4px solid #000;border-radius:50%;width:10.5em;height:10.5em;display:grid;place-items:center;font-weight:1000;transform:rotate(-13deg);z-index:3}
.footer{position:absolute;left:6.4%;right:6.4%;bottom:5%;display:flex;justify-content:space-between;font-weight:900;font-size:clamp(12px,1vw,18px)}
'@
$body = @'
<section class="stage">
  <div class="hero">
    <span class="label">BLOCKFRAME · LIGHT</span>
    <h1>Bold Deck<br>One Page</h1>
    <p>新粗野主义亮色主题：黑色粗边框、硬阴影、糖果色块和强图形感，适合创意提案与发布页。</p>
  </div>
  <div class="shape pink"></div><div class="shape blue"></div><div class="shape green"></div>
  <div class="badge">THEME<br>01</div>
  <div class="footer"><span>NEOBRUTALIST HTML SLIDE</span><span>01 / 04</span></div>
</section>
'@
$samples += @{ File="01_blockframe.html"; Title="BlockFrame 新粗野主义亮色"; Html=(Wrap-Theme "BlockFrame 新粗野主义亮色" $css $body) }

$css = @'
.stage{background:#0a0a0a;color:#f6f6f6;padding:6.4%}
.hero{position:absolute;left:6.4%;top:10%;width:56%;background:#141414;border:4px solid #f6f6f6;box-shadow:8px 8px 0 rgba(246,246,246,.18);padding:3.2em;z-index:2}
.label{display:inline-block;border:3px solid #f6f6f6;background:#FE90E8;color:#0a0a0a;box-shadow:4px 4px 0 rgba(246,246,246,.24);padding:.55em .85em;font-weight:1000;letter-spacing:.08em}
h1{font-size:clamp(48px,6vw,104px);line-height:.92;margin:.34em 0 .22em;font-weight:1000;text-transform:uppercase;letter-spacing:-.03em}
p{font-size:clamp(15px,1.2vw,22px);line-height:1.58;color:#d8d8d8;max-width:86%;margin:0}
.cards{position:absolute;right:7%;top:13%;width:30%;display:grid;gap:1.2em}
.card{background:#1c1c1c;border:4px solid #f6f6f6;padding:1.25em;box-shadow:8px 8px 0 rgba(246,246,246,.16);font-weight:1000;font-size:clamp(18px,1.8vw,32px)}
.c1{color:#C0F7FE;box-shadow:0 0 28px rgba(192,247,254,.28),8px 8px 0 rgba(246,246,246,.16)}
.c2{color:#99E885;transform:rotate(3deg)}
.c3{color:#F7CB46;transform:rotate(-3deg)}
.sticker{position:absolute;right:11%;bottom:10%;background:#FFDC8B;color:#0a0a0a;border:4px solid #f6f6f6;border-radius:999px;padding:1.2em 1.6em;font-weight:1000;transform:rotate(-10deg)}
.footer{position:absolute;left:6.4%;right:6.4%;bottom:5%;display:flex;justify-content:space-between;color:#a0a0a0;font-weight:900}
'@
$body = @'
<section class="stage">
  <div class="hero">
    <span class="label">BLOCKFRAME · DARK</span>
    <h1>Dark Candy<br>Impact</h1>
    <p>暗色新粗野主义主题：近黑画布、白色粗边框、荧光糖果色和硬阴影，强烈但不怯场。</p>
  </div>
  <div class="cards"><div class="card c1">01 GRAPHIC</div><div class="card c2">02 BOLD</div><div class="card c3">03 PLAYFUL</div></div>
  <div class="sticker">THEME 02</div>
  <div class="footer"><span>DARK NEOBRUTALIST SLIDE</span><span>02 / 04</span></div>
</section>
'@
$samples += @{ File="02_blockframe_dark.html"; Title="BlockFrame Dark 暗色新粗野"; Html=(Wrap-Theme "BlockFrame Dark 暗色新粗野" $css $body) }

$css = @'
.stage{background:#fdfae7;color:#111;padding:6% 7%}
.top{display:flex;justify-content:space-between;align-items:flex-start}
.eyebrow{color:#1e2bfa;font-weight:800;letter-spacing:.08em;text-transform:uppercase;font-size:clamp(13px,1vw,17px)}
.date{color:#6b6b6b;font-weight:600;font-size:clamp(12px,.9vw,16px)}
h1{font-size:clamp(40px,4.5vw,72px);line-height:1.04;margin:.42em 0 .22em;font-weight:800;letter-spacing:-.02em;max-width:58%}
.lead{font-size:clamp(14px,1.08vw,19px);line-height:1.55;color:#6b6b6b;max-width:48%;margin:0}
.metrics{position:absolute;left:7%;right:7%;bottom:8%;display:grid;grid-template-columns:repeat(3,1fr);gap:2%}
.metric{background:rgba(30,43,250,.04);border:1.5px solid rgba(30,43,250,.2);border-radius:14px;padding:1.15em}
.num{font-size:clamp(30px,3vw,52px);line-height:1;color:#1e2bfa;font-weight:900}
.metric h2{font-size:clamp(16px,1.3vw,23px);margin:.55em 0 .28em}
.metric p{margin:0;color:#6b6b6b;line-height:1.45;font-size:clamp(11px,.9vw,15px)}
.panel{position:absolute;right:7%;top:20%;width:26%;height:28%;border-radius:18px;background:rgba(30,43,250,.08);border:1.5px solid rgba(30,43,250,.2);display:grid;place-items:center;color:#1e2bfa;font-size:clamp(34px,4.4vw,74px);font-weight:900}
'@
$body = @'
<section class="stage">
  <div class="top"><div class="eyebrow">BLUE PROFESSIONAL</div><div class="date">CONSULTING DECK / SAMPLE</div></div>
  <h1>克制、清晰的商务蓝主题</h1>
  <p class="lead">奶油色画布搭配单一电光钴蓝强调，适合咨询交付物、内部评审和 B2B 产品介绍。</p>
  <div class="panel">42%</div>
  <div class="metrics">
    <div class="metric"><div class="num">01</div><h2>现代专业</h2><p>低饱和背景和单一强调色，减少视觉噪声。</p></div>
    <div class="metric"><div class="num">02</div><h2>数据友好</h2><p>指标卡、图表和说明文字都能保持远距离可读。</p></div>
    <div class="metric"><div class="num">03</div><h2>企业语境</h2><p>适合严肃内容，但不会显得老派或沉闷。</p></div>
  </div>
</section>
'@
$samples += @{ File="03_blue_professional.html"; Title="Blue Professional 奶油钴蓝专业"; Html=(Wrap-Theme "Blue Professional 奶油钴蓝专业" $css $body) }

$css = @'
.stage{background:#08090d;color:#f6f2e8;padding:6% 8%}
.stage:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 82% 18%,rgba(185,142,255,.18),transparent 24%),radial-gradient(circle at 78% 82%,rgba(255,196,2,.12),transparent 22%)}
.content{position:relative;z-index:1;max-width:70%}
.tag{display:inline-block;color:#b98eff;background:rgba(185,142,255,.1);border:1px solid rgba(255,255,255,.16);border-radius:999px;padding:.65em 1.25em;font-weight:800;letter-spacing:.08em}
h1{font-size:clamp(64px,7vw,118px);line-height:1.02;margin:.32em 0 .18em;font-weight:800;letter-spacing:-.02em}
.gold{color:#ffc402}.purple{color:#b98eff}
p{font-size:clamp(20px,1.75vw,30px);line-height:1.68;color:#aaa59a;max-width:74%;margin:0}
.cards{position:absolute;right:8%;bottom:12%;display:grid;gap:1em;width:29%;z-index:2}
.card{background:rgba(255,255,255,.055);border:1.5px solid rgba(255,255,255,.16);border-radius:14px;padding:1.4em}
.card b{display:block;color:#b98eff;font-size:clamp(22px,2vw,36px);margin-bottom:.35em}
.card span{color:#aaa59a;line-height:1.5}
.footer{position:absolute;left:8%;right:8%;bottom:5%;display:flex;justify-content:space-between;color:#746f66;font-weight:800}
'@
$body = @'
<section class="stage">
  <div class="content">
    <span class="tag">PURPLE GOLD PRESENTATION</span>
    <h1>暗色视频感<br><span class="purple">结构</span> + <span class="gold">重点</span></h1>
    <p>近黑画布、紫色结构强调和金色结论高亮，适合知识分享、技术教程和视频友好型演示。</p>
  </div>
  <div class="cards"><div class="card"><b>01</b><span>单页单点，信息密度克制。</span></div><div class="card"><b>02</b><span>紫色负责结构，金色只强调关键结论。</span></div></div>
  <div class="footer"><span>DARK CINEMATIC HTML DECK</span><span>04 / 04</span></div>
</section>
'@
$samples += @{ File="04_purple_gold_presentation.html"; Title="Purple Gold Presentation 紫金暗色视频"; Html=(Wrap-Theme "Purple Gold Presentation 紫金暗色视频" $css $body) }

$pageSampleScript = Join-Path $scriptRoot "generate-page-style-samples.ps1"
$pageSampleRoot = Join-Path $skillRoot "assets\previews\page-style-samples"
if (Test-Path -LiteralPath $pageSampleScript) {
    & powershell -ExecutionPolicy Bypass -File $pageSampleScript -OutputRoot $pageSampleRoot | Out-Null
}

$pageThemeSamples = @(
    @{ Source="01_weekly_report_mflex.html"; File="05_weekly_report_mflex.html"; Title="MFLEX 蓝白项目汇报" },
    @{ Source="02_dark_gold_insight.html"; File="06_dark_gold_insight.html"; Title="暗金数据洞察" },
    @{ Source="03_raw_paper_notes.html"; File="07_raw_paper_notes.html"; Title="Raw Paper 米白黑纸感文本笔记" },
    @{ Source="04_social_card_layering_v2a.html"; File="08_social_card_layering_v2a.html"; Title="自媒体 V2a 蓝紫橙层叠卡片" },
    @{ Source="05_social_dashboard_v2b.html"; File="09_social_dashboard_v2b.html"; Title="自媒体 V2b 浅灰白橙仪表盘" },
    @{ Source="06_aurora_ui.html"; File="10_aurora_ui.html"; Title="Aurora UI 极光科技" }
)

foreach ($pageSample in $pageThemeSamples) {
    $sourcePath = Join-Path $pageSampleRoot $pageSample.Source
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Missing page style sample for deck theme adapter: $sourcePath"
    }
    $html = Get-Content -Encoding UTF8 -Raw -LiteralPath $sourcePath
    $html = $html -replace '<title>.*?</title>', "<title>$($pageSample.Title) · deck 适配主题</title>"
    $samples += @{ File=$pageSample.File; Title="$($pageSample.Title) · deck 适配"; Html=$html }
}

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
<title>html-presentation deck 主题样例总览</title>
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
  <h1>html-presentation · deck 主题样例总览</h1>
  <p>每个 theme_id 只生成一页，用于快速查看 deck 主题气质。前 4 个是原生 deck 主题，后 6 个是 page 风格适配 deck。完整 deck 仍会按 slide_structure 生成多页。</p>
</header>
<main class="grid">
$cards
</main>
</body>
</html>
"@
Write-Utf8File -Path (Join-Path $OutputRoot "index.html") -Content $index

"Generated $($samples.Count) deck theme sample files + index at $OutputRoot"



