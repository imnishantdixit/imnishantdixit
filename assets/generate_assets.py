import math, random, html
random.seed(7)
OUT = "/mnt/user-data/outputs/readme-kit/assets/"
MONO = "'JetBrains Mono','Fira Code','SFMono-Regular',Consolas,'Courier New',monospace"
SANS = "'Segoe UI',-apple-system,'Helvetica Neue',Arial,sans-serif"
TEAL, VIO, AMB, PINK, SKY = "#2dd4bf", "#a78bfa", "#fbbf24", "#f472b6", "#38bdf8"
esc = html.escape

# ---------------- HERO ----------------
W, H = 1200, 380
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Nishant Dixit - AI/ML, Bioinformatics, Entrepreneur">')
s.append('''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#060912"/><stop offset="1" stop-color="#0c1526"/></linearGradient>
<linearGradient id="nm" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#7dd3fc"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1e293b" stroke-width="1" opacity=".55"/></pattern>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="aura"><stop offset="0" stop-color="#2dd4bf" stop-opacity=".22"/><stop offset="1" stop-color="#2dd4bf" stop-opacity="0"/></radialGradient>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/><rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>')
# drifting aura
s.append('<circle cx="900" cy="190" r="260" fill="url(#aura)"><animate attributeName="cx" values="820;980;820" dur="14s" repeatCount="indefinite"/></circle>')
# nucleotide rain
cols = {"A":TEAL,"T":VIO,"G":AMB,"C":PINK}
for c in range(26):
    x = 600 + c*23 + random.randint(-4,4)
    dur = random.uniform(8,15); beg = -random.uniform(0,dur)
    letters = "".join(random.choice("ATGC") for _ in range(7))
    ts = "".join(f'<tspan x="{x}" dy="22" fill="{cols[l]}">{l}</tspan>' for l in letters)
    s.append(f'<text y="0" font-family="{MONO}" font-size="15" opacity=".16">{ts}<animateTransform attributeName="transform" type="translate" values="0,-170;0,{H+20}" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/></text>')
# helix
N, M, A, CY, X0, X1, DUR = 46, 20, 82, 190, 650, 1150, 6
dx = (X1-X0)/(N-1)
def vals(fn): return ";".join(f"{fn(2*math.pi*k/M):.1f}" for k in range(M+1))
# rungs
for i in range(0, N, 2):
    th = i*0.42; x = X0+i*dx
    y1 = vals(lambda p: CY + A*math.sin(th-p)); y2 = vals(lambda p: CY - A*math.sin(th-p))
    s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{CY}" y2="{CY}" stroke="#7dd3fc" stroke-opacity=".32" stroke-width="2"><animate attributeName="y1" values="{y1}" dur="{DUR}s" repeatCount="indefinite"/><animate attributeName="y2" values="{y2}" dur="{DUR}s" repeatCount="indefinite"/></line>')
s.append('<g filter="url(#glow)">')
for sidx, col in ((0, TEAL), (1, VIO)):
    for i in range(N):
        th = i*0.42 + sidx*math.pi; x = X0+i*dx
        cy = vals(lambda p: CY + A*math.sin(th-p)); r = vals(lambda p: 5 + 2.4*math.cos(th-p))
        s.append(f'<circle cx="{x:.1f}" cy="{CY}" r="5" fill="{col}"><animate attributeName="cy" values="{cy}" dur="{DUR}s" repeatCount="indefinite"/><animate attributeName="r" values="{r}" dur="{DUR}s" repeatCount="indefinite"/></circle>')
s.append('</g>')
# text
s.append(f'<text x="60" y="92" font-family="{MONO}" font-size="14" letter-spacing="3" fill="{TEAL}">// AI/ML · BIOINFORMATICS · FOUNDER</text>')
s.append(f'<text x="60" y="172" font-family="{SANS}" font-size="70" font-weight="800" fill="url(#nm)" textLength="520" lengthAdjust="spacingAndGlyphs">Nishant Dixit</text>')
roles = ["Co-Founder & CTO — Vibely", "Co-Founder — postnp, 24/7 marketing agent", "Open source — Trapiche · MalariaGEN", "Published — NPvert, structure-first RAG"]
s.append(f'<text x="60" y="226" font-family="{MONO}" font-size="20" fill="{TEAL}">$</text>')
P = 4*3
for k, t in enumerate(roles):
    L = len(t)*11.5
    s.append(f'<text x="86" y="226" font-family="{MONO}" font-size="20" fill="#e2e8f0" opacity="0" textLength="{L:.0f}" lengthAdjust="spacing">{esc(t)}<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.04;0.22;0.26;1" dur="{P}s" begin="{k*3}s" repeatCount="indefinite"/></text>')
# pills
for (x, w, label, col, d) in ((60,112,"AI / ML",TEAL,0),(184,196,"BIOINFORMATICS",VIO,.6),(392,176,"ENTREPRENEUR",AMB,1.2)):
    s.append(f'<rect x="{x}" y="270" width="{w}" height="36" rx="18" fill="{col}" fill-opacity=".08" stroke="{col}" stroke-width="1.5"><animate attributeName="stroke-opacity" values="1;.3;1" dur="3s" begin="{d}s" repeatCount="indefinite"/></rect>')
    s.append(f'<text x="{x+w/2}" y="293" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="2" fill="{col}">{label}</text>')
s.append('</svg>')
open(OUT+"hero.svg","w",encoding="utf-8").write("\n".join(s))

# ---------------- PIPELINE ----------------
W, H = 1200, 270
s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="From raw sequences to shipped products">']
s.append('''<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#060912"/><stop offset="1" stop-color="#0c1526"/></linearGradient>
<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2dd4bf"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#fbbf24"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>''')
s.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>')
s.append(f'<text x="40" y="44" font-family="{MONO}" font-size="13" letter-spacing="3" fill="#64748b">// PIPELINE: FROM SEQUENCE TO SHIPPED PRODUCT</text>')
xs = [120,360,600,840,1080]; cy = 118
s.append(f'<path d="M{xs[0]},{cy} L{xs[-1]},{cy}" stroke="#1e293b" stroke-width="3"/>')
s.append(f'<path d="M{xs[0]},{cy} L{xs[-1]},{cy}" stroke="url(#ln)" stroke-width="3" stroke-dasharray="8 10" fill="none"><animate attributeName="stroke-dashoffset" values="0;-36" dur="1.2s" repeatCount="indefinite"/></path>')
nodes = [("ACGT",TEAL,"Raw biology","sequences · genomes"),("ALIGN",SKY,"Open-source tooling","Trapiche · MalariaGEN"),("EMBED",VIO,"Models & retrieval","RAG · fine-tuning · evals"),("AGENT",PINK,"Agents","LangChain · FastAPI · LLMs"),("SHIP",AMB,"Products","Vibely · postnp · KALQY")]
for k,(x,(tag,col,t1,t2)) in enumerate(zip(xs,nodes)):
    b = (1.5*k) % 2
    s.append(f'<circle cx="{x}" cy="{cy}" r="34" fill="none" stroke="{col}" stroke-width="2" opacity="0"><animate attributeName="r" values="34;56" dur="2s" begin="{b}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="2s" begin="{b}s" repeatCount="indefinite"/></circle>')
    s.append(f'<circle cx="{x}" cy="{cy}" r="34" fill="#0b1220" stroke="{col}" stroke-width="2.5" filter="url(#glow)"/>')
    s.append(f'<text x="{x}" y="{cy+5}" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="{col}">{tag}</text>')
    s.append(f'<text x="{x}" y="{cy+66}" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="700" fill="#f1f5f9">{esc(t1)}</text>')
    s.append(f'<text x="{x}" y="{cy+90}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#94a3b8">{esc(t2)}</text>')
for j in range(3):
    s.append(f'<circle r="6" fill="#ffffff" filter="url(#glow)"><animateMotion dur="6s" begin="{2*j}s" repeatCount="indefinite" path="M{xs[0]},{cy} L{xs[-1]},{cy}"/></circle>')
s.append('</svg>')
open(OUT+"pipeline.svg","w",encoding="utf-8").write("\n".join(s))

# ---------------- TERMINAL ----------------
W, H = 1200, 340
P = 16
lines = [
 ("$","whoami",0.5,1.0,"cmd"),
 ("","nishant-dixit   # ai/ml · bioinformatics · founder",1.8,1.8,"out"),
 ("$","ls ventures/",4.0,1.0,"cmd"),
 ("","mana-intelligence/   vibely/   postnp/   kalqy/",5.1,1.8,"out"),
 ("$","cat now.txt",7.2,1.0,"cmd"),
 ("","agents that ship software",8.4,1.2,"out"),
 ("","open-source tooling for genomics",9.8,1.4,"out"),
 ("","coffee -> code -> companies",11.4,1.2,"out"),
 ("$","",13.0,0.2,"cursor"),
]
s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Terminal intro">']
s.append(f'<rect width="{W}" height="{H}" rx="16" fill="#0d1117" stroke="#30363d" stroke-width="2"/><path d="M2,48 H{W-2}" stroke="#30363d"/>')
for i,c in enumerate(("#ff5f56","#ffbd2e","#27c93f")): s.append(f'<circle cx="{34+i*24}" cy="25" r="7" fill="{c}"/>')
s.append(f'<text x="{W/2}" y="30" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#8b949e">nishant@founder-mode: ~</text>')
CW = 11
for k,(pr,txt,t0,d,kind) in enumerate(lines):
    y = 92 + k*28
    s.append(f'<text x="40" y="{y}" font-family="{MONO}" font-size="18" fill="{TEAL}" opacity="0">{pr}<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{(t0-0.05)/P:.4f};{t0/P:.4f};0.96;1" dur="{P}s" repeatCount="indefinite"/></text>' if pr else '')
    if not txt: continue
    x = 62 if pr else 40
    wfull = len(txt)*CW
    col = "#e6edf3" if kind=="cmd" else "#9fb3c8"
    s.append(f'<clipPath id="c{k}"><rect x="{x-2}" y="{y-22}" height="30" width="0"><animate attributeName="width" values="0;0;{wfull+6};{wfull+6};0" keyTimes="0;{t0/P:.4f};{(t0+d)/P:.4f};0.96;1" dur="{P}s" repeatCount="indefinite"/></rect></clipPath>')
    s.append(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="18" fill="{col}" textLength="{wfull}" lengthAdjust="spacing" clip-path="url(#c{k})">{esc(txt)}</text>')
y = 92 + 8*28
s.append(f'<rect x="62" y="{y-16}" width="10" height="20" fill="{TEAL}" opacity="0"><animate attributeName="opacity" values="0;0;1;0;1;0;1;0;1;0;0" keyTimes="0;{13/P:.4f};{13.1/P:.4f};{13.6/P:.4f};{14/P:.4f};{14.4/P:.4f};{14.7/P:.4f};{15.1/P:.4f};{15.3/P:.4f};0.96;1" dur="{P}s" repeatCount="indefinite"/></rect>')
s.append('</svg>')
open(OUT+"terminal.svg","w",encoding="utf-8").write("\n".join(s))

# ---------------- FOOTER ticker ----------------
W, H = 1200, 70
CWF = 14; n = 120
seq = [random.choice("ATGC") for _ in range(n)]
tsp = "".join(f'<tspan fill="{cols[b]}">{b}</tspan>' for b in seq)
tl = n*CWF
s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="DNA sequence ticker">']
s.append(f'<rect width="{W}" height="{H}" rx="14" fill="#060912"/><clipPath id="cl"><rect width="{W}" height="{H}" rx="14"/></clipPath><g clip-path="url(#cl)">')
for yy, op, dur, sgn in ((26,.9,40,1),(52,.35,60,-1)):
    a,b = (0,-tl) if sgn==1 else (-tl,0)
    s.append(f'<g><text y="{yy}" font-family="{MONO}" font-size="20" opacity="{op}" textLength="{tl}" lengthAdjust="spacing">{tsp}</text><text x="{tl}" y="{yy}" font-family="{MONO}" font-size="20" opacity="{op}" textLength="{tl}" lengthAdjust="spacing">{tsp}</text><animateTransform attributeName="transform" type="translate" values="{a},0;{b},0" dur="{dur}s" repeatCount="indefinite"/></g>')
s.append(f'<rect width="{W}" height="{H}" fill="#060912" opacity=".0"/></g>')
s.append(f'<text x="{W/2}" y="45" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" letter-spacing="4" fill="#ffffff" stroke="#060912" stroke-width="6" paint-order="stroke">BUILD · BREAK · SEQUENCE · SHIP</text>')
s.append('</svg>')
open(OUT+"footer.svg","w",encoding="utf-8").write("\n".join(s))
