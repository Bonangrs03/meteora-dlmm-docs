#!/usr/bin/env python3
"""Rebuild Meteora DLMM HTML + PDF from source markdown files. Dual-language (EN/ID)."""

import markdown
from pathlib import Path

ACTS_EN_DIR = Path('/home/bonangrs03/meteora-dlmm-docs/acts')
ACTS_ID_DIR = Path('/home/bonangrs03/meteora-dlmm-docs/acts-id')
OUTPUT_HTML = Path('/home/bonangrs03/meteora-dlmm-docs/index.html')
OUTPUT_PDF = Path('/home/bonangrs03/meteora-dlmm-docs/Meteora_DLMM_Docs_v2.pdf')

CSS = """
:root {
    --yellow: #FFD700;
    --red: #FF5E5B;
    --blue: #5B8CFF;
    --green: #3DDC84;
    --purple: #A855F7;
    --bg: #FFFDF7;
    --fg: #1A1A1A;
    --card-bg: #FFFDF7;
    --border: #1A1A1A;
}

@page {
    size: A4;
    margin: 1.8cm 2cm;
    @bottom-center {
        content: "Meteora DLMM · The Complete Guide — Page " counter(page);
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 8px;
        color: #999;
    }
}
@page :first { @bottom-center { content: none; } }
@page :blank { @bottom-center { content: none; } }

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background: var(--bg);
    color: var(--fg);
    line-height: 1.7;
    font-size: 11pt;
}

/* Lang toggle */
.lang-toggle-wrap {
    display: flex;
    justify-content: center;
    margin: 0.8rem 0 0 0;
}
.lang-toggle {
    display: inline-flex;
    border: 3px solid var(--fg);
    border-radius: 0;
    overflow: hidden;
    background: var(--fg);
}
.lang-btn {
    padding: 0.4em 1.4em;
    font-family: inherit;
    font-weight: 700;
    font-size: 0.85rem;
    cursor: pointer;
    border: none;
    background: var(--fg);
    color: var(--bg);
    transition: background 0.15s, color 0.15s;
    letter-spacing: 0.02em;
}
.lang-btn.active {
    background: var(--yellow);
    color: var(--fg);
}
.lang-btn:hover { opacity: 0.9; }

/* Language visibility */
.lang-en, .lang-id { display: none; }
body.show-en .lang-en { display: block; }
body.show-id .lang-id { display: block; }
/* Default: show EN */
body.show-en .lang-en { display: block; }

/* Hero */
.hero {
    background: var(--yellow);
    border-bottom: 3px solid var(--fg);
    padding: 2.5rem 2rem 1.5rem;
    text-align: center;
    margin-bottom: 2rem;
}
.hero h1 {
    font-size: 2.2rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: -0.02em;
    margin-bottom: 0.5rem;
}
.hero .subtitle {
    font-size: 0.95rem;
    max-width: 550px;
    margin: 0 auto;
}
.chapter-count {
    display: inline-block;
    margin-top: 0.8rem;
    background: var(--fg);
    color: var(--bg);
    padding: 0.3em 1em;
    font-weight: 700;
    font-size: 0.8rem;
}

/* TOC */
.toc-section {
    margin: 1.5rem 0 2.5rem;
    page-break-after: always;
}
.toc-section h2 {
    font-size: 1.5rem;
    font-weight: 900;
    border-bottom: 3px solid var(--fg);
    padding-bottom: 0.3em;
    margin-bottom: 1rem;
    display: inline-block;
}
.toc-list {
    list-style: none;
    padding: 0;
}
.toc-list li {
    padding: 0.35rem 0;
    border-bottom: 1px dashed #ccc;
    font-size: 0.9rem;
}
.toc-num {
    display: inline-block;
    width: 2em;
    font-weight: 700;
    color: #666;
}

/* Chapter cards */
.chapter {
    border: 3px solid var(--fg);
    background: var(--card-bg);
    margin-bottom: 2rem;
    padding: 1.8rem 2rem;
    page-break-inside: avoid;
}

.chapter h1 {
    font-size: 1.5rem;
    font-weight: 900;
    margin-top: 0;
    line-height: 1.3;
}

.chapter h2 {
    font-size: 1.2rem;
    font-weight: 800;
    border-bottom: 2px solid var(--fg);
    padding-bottom: 0.2em;
    margin: 1.5em 0 0.6em;
    display: inline-block;
}

.chapter h3 {
    font-size: 1.05rem;
    font-weight: 700;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
}

p { margin-bottom: 0.8em; }
strong { font-weight: 700; }
em { font-style: italic; }

hr {
    border: none;
    border-top: 2px solid var(--fg);
    margin: 1.2em 0;
}

ul, ol { margin: 0.6em 0 0.8em 1.5em; }
li { margin-bottom: 0.25em; }

blockquote {
    border-left: 4px solid var(--yellow);
    margin: 1em 0;
    padding: 0.5em 1em;
    background: rgba(255, 215, 0, 0.08);
    font-style: italic;
}
blockquote p { margin-bottom: 0.3em; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 0.9rem;
}
thead th {
    background: var(--fg);
    color: var(--bg);
    padding: 0.5em 0.8em;
    text-align: left;
    font-weight: 700;
    border: 2px solid var(--fg);
}
tbody td {
    padding: 0.45em 0.8em;
    border: 1px solid rgba(26, 26, 26, 0.2);
    vertical-align: top;
}
tbody tr:nth-child(odd) { background: rgba(0,0,0,0.02); }

pre {
    background: #F7F5ED;
    border: 2px solid var(--fg);
    padding: 0.8em 1em;
    font-family: 'Courier New', monospace;
    font-size: 0.82rem;
    line-height: 1.5;
    margin: 0.8em 0;
    white-space: pre-wrap;
    word-break: break-word;
}
code {
    font-family: 'Courier New', monospace;
    background: #F7F5ED;
    padding: 0.1em 0.3em;
    font-size: 0.9em;
}
pre code { background: none; padding: 0; }

.footer {
    text-align: center;
    padding: 1.5rem;
    border-top: 3px solid var(--fg);
    margin-top: 2rem;
    font-size: 0.8rem;
    color: #888;
}

/* ===== MOBILE RESPONSIVE ===== */
@media (max-width: 768px) {
    @page { margin: 1cm 1.2cm; }
    .hero { padding: 1.5rem 1rem 1rem; }
    .hero h1 { font-size: 1.5rem; }
    .hero .subtitle { font-size: 0.82rem; }
    .chapter-count { font-size: 0.7rem; padding: 0.25em 0.8em; }
    .lang-btn { padding: 0.35em 1em; font-size: 0.78rem; }
    .chapter { padding: 1.2rem 1rem; margin-bottom: 1.5rem; border-width: 2px; }
    .chapter h1 { font-size: 1.25rem; }
    .chapter h2 { font-size: 1.05rem; }
    .chapter h3 { font-size: 0.95rem; }
    body { font-size: 10.5pt; line-height: 1.65; }
    p { margin-bottom: 0.65em; }
    .toc-section { margin: 1rem 0 2rem; }
    .toc-section h2 { font-size: 1.2rem; }
    .toc-list li { font-size: 0.8rem; padding: 0.25rem 0; }
    table { display: block; overflow-x: auto; white-space: nowrap; font-size: 0.75rem; -webkit-overflow-scrolling: touch; }
    thead th, tbody td { padding: 0.35em 0.55em; }
    pre { font-size: 0.7rem; padding: 0.6em 0.8em; }
    blockquote { margin: 0.8em 0; padding: 0.4em 0.8em; border-left-width: 3px; }
    .footer { font-size: 0.7rem; padding: 1rem; }
}

@media (max-width: 480px) {
    .hero { padding: 1.2rem 0.8rem 0.8rem; }
    .hero h1 { font-size: 1.3rem; }
    .lang-btn { padding: 0.3em 0.8em; font-size: 0.72rem; }
    .chapter { padding: 1rem 0.8rem; }
    .chapter h1 { font-size: 1.15rem; }
    body { font-size: 10pt; }
    table { font-size: 0.68rem; }
    ul, ol { margin-left: 1.2em; }
}

/* PDF: show both languages (no JS) */
@media print {
    .lang-toggle-wrap { display: none; }
    .lang-en, .lang-id { display: block !important; }
}
"""

LANG_JS = """
<script>
(function() {
    function setLang(lang) {
        document.body.className = 'show-' + lang;
        localStorage.setItem('meteora-lang', lang);
        document.querySelectorAll('.lang-btn').forEach(function(b) {
            b.classList.toggle('active', b.dataset.lang === lang);
        });
    }
    var saved = localStorage.getItem('meteora-lang') || 'en';
    setLang(saved);
    document.querySelectorAll('.lang-btn').forEach(function(b) {
        b.addEventListener('click', function() { setLang(this.dataset.lang); });
    });
})();
</script>
"""

def build_html():
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite'])
    
    act_files = sorted(ACTS_EN_DIR.glob('*.md'))
    chapters_html = []
    toc_entries = []
    
    for f in act_files:
        # English
        content_en = f.read_text()
        html_en = md.convert(content_en)
        
        # Indonesian
        f_id = ACTS_ID_DIR / f.name
        content_id = f_id.read_text() if f_id.exists() else content_en
        html_id = md.convert(content_id)
        
        num = f.stem[:2]
        
        # Wrap in chapter div with both languages
        chapter_id = f.stem
        chapters_html.append(f'''
        <div class="chapter" id="{chapter_id}">
            <div class="lang-en">{html_en}</div>
            <div class="lang-id">{html_id}</div>
        </div>''')
    
    # Build TOC (EN only for print/PDF)
    toc_html = ''
    
    # Full document
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meteora DLMM: The Complete Guide</title>
    <style>{CSS}</style>
</head>
<body class="show-en">
    <header class="hero">
        <h1>Meteora DLMM<br>The Complete Guide</h1>
        <p class="subtitle lang-en">From Budi's bus terminal to your first liquidity position — a story-driven journey through DeFi's most capital-efficient protocol.</p>
        <p class="subtitle lang-id">Dari terminal bus Budi ke posisi likuiditas pertama lo — perjalanan story-driven melalui protokol DeFi paling capital-efficient.</p>
        <span class="chapter-count lang-en">15 CHAPTERS</span>
        <span class="chapter-count lang-id">15 BAB</span>
        <div class="lang-toggle-wrap">
            <div class="lang-toggle">
                <button class="lang-btn active" data-lang="en">🇬🇧 EN</button>
                <button class="lang-btn" data-lang="id">🇮🇩 ID</button>
            </div>
        </div>
    </header>
    
    {chr(10).join(chapters_html)}
    
    <div class="footer lang-en">
        Meteora DLMM: The Complete Guide — built for absolute beginners on Solana ♥
    </div>
    <div class="footer lang-id">
        Meteora DLMM: Panduan Lengkap — dibuat untuk pemula absolut di Solana ♥
    </div>
    
    {LANG_JS}
</body>
</html>'''
    
    OUTPUT_HTML.write_text(full_html)
    print(f"HTML written: {OUTPUT_HTML} ({len(full_html)} chars)")
    return full_html


def convert_to_pdf():
    import subprocess
    result = subprocess.run(
        ['python3', '-m', 'weasyprint', str(OUTPUT_HTML), str(OUTPUT_PDF)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        return False
    for line in result.stderr.strip().split('\n'):
        if line.strip():
            print(f"  [weasyprint] {line.strip()}")
    return True


if __name__ == '__main__':
    print("Building dual-language HTML from markdown...")
    build_html()
    print("\nConverting to PDF...")
    if convert_to_pdf():
        import os
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"\n✓ PDF ready: {OUTPUT_PDF} ({size_kb:.0f} KB)")
    else:
        print("\n✗ PDF conversion failed")
