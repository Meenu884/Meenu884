import os, math, random

OUT = '/mnt/user-data/outputs/Jayameenakshi/assets'
os.makedirs(OUT, exist_ok=True)
random.seed(11)

SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'Courier New',Consolas,Menlo,monospace"
CY, PU, PK, BL, AM, GR = '#22d3ee', '#8b5cf6', '#f472b6', '#3b82f6', '#fbbf24', '#34d399'

COMMON = '''
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07051a"/><stop offset=".55" stop-color="#0f0a2e"/><stop offset="1" stop-color="#160b3d"/></linearGradient>
<radialGradient id="glowP"><stop offset="0" stop-color="#8b5cf6" stop-opacity=".5"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>
<radialGradient id="glowC"><stop offset="0" stop-color="#22d3ee" stop-opacity=".4"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="glowK"><stop offset="0" stop-color="#f472b6" stop-opacity=".4"/><stop offset="1" stop-color="#f472b6" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#a78bfa" stroke-opacity=".08"/></pattern>
<linearGradient id="neon" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#8b5cf6"/><stop offset="1" stop-color="#f472b6"/></linearGradient>
<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="0" spreadMethod="reflect"><stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/><animate attributeName="x1" values="0;600;0" dur="10s" repeatCount="indefinite"/><animate attributeName="x2" values="600;1200;600" dur="10s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".13"/><stop offset="1" stop-color="#fff" stop-opacity=".03"/></linearGradient>
<filter id="glow" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="12"/></filter>
'''


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def T(x, y, txt, size=16, fill='#e2e8f0', weight=400, anchor='start', font=None, extra=''):
    font = font or SANS
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{esc(txt)}</text>')


def save(name, w, h, label, body, defs=''):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'role="img" aria-label="{esc(label)}"><title>{esc(label)}</title><defs>{COMMON}{defs}</defs>{body}</svg>')
    with open(f'{OUT}/{name}', 'w') as f:
        f.write(svg)


def bg(w, h, rx=24):
    return (f'<rect width="{w}" height="{h}" rx="{rx}" fill="url(#bg)"/>'
            f'<ellipse cx="{w*.2:.0f}" cy="{h*.3:.0f}" rx="{w*.35:.0f}" ry="{h*.7:.0f}" fill="url(#glowP)"><animate attributeName="cx" values="{w*.12:.0f};{w*.3:.0f};{w*.12:.0f}" dur="14s" repeatCount="indefinite"/></ellipse>'
            f'<ellipse cx="{w*.85:.0f}" cy="{h*.75:.0f}" rx="{w*.3:.0f}" ry="{h*.6:.0f}" fill="url(#glowC)"><animate attributeName="cx" values="{w*.9:.0f};{w*.7:.0f};{w*.9:.0f}" dur="16s" repeatCount="indefinite"/></ellipse>'
            f'<ellipse cx="{w*.55:.0f}" cy="{h*.95:.0f}" rx="{w*.2:.0f}" ry="{h*.3:.0f}" fill="url(#glowK)"/>'
            f'<rect width="{w}" height="{h}" rx="{rx}" fill="url(#grid)"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="none" stroke="#a78bfa" stroke-opacity=".25"/>')


def particles(w, h, n, colors=(CY, PU, PK)):
    s = ''
    for _ in range(n):
        x = random.uniform(10, w - 10); y = random.uniform(20, h - 10)
        r = random.uniform(1, 2.6); c = random.choice(colors)
        d = random.uniform(5, 11); dy = random.uniform(12, 32)
        s += (f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{c}" opacity=".6">'
              f'<animate attributeName="cy" values="{y:.0f};{y-dy:.0f};{y:.0f}" dur="{d:.1f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values=".15;.9;.15" dur="{d*.7:.1f}s" repeatCount="indefinite"/></circle>')
    return s


def mix(c1, c2, t):
    a = [int(c1[i:i+2], 16) for i in (1, 3, 5)]; b = [int(c2[i:i+2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def shade(c, f):
    a = [int(c[i:i+2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(max(0, min(255, int(v * f))) for v in a)


def typing(phrases, x, y, fs=22, cw=13.2, type_s=.07, del_s=.035, hold=1.6, gap=.4, color='#e2e8f0'):
    t = 0; ev = []
    for idx, p in enumerate(phrases):
        n = len(p)
        for k in range(1, n + 1):
            ev.append((t, idx, k)); t += type_s
        t += hold - type_s
        for k in range(n - 1, -1, -1):
            ev.append((t, idx, k)); t += del_s
        t += gap
    total = t
    kt = ';'.join(f'{e[0]/total:.4f}' for e in ev)
    defs = ''; body = ''
    for i, p in enumerate(phrases):
        vals = ';'.join(f'{(e[2]*cw if e[1]==i else 0):.1f}' for e in ev)
        defs += (f'<clipPath id="tc{i}"><rect x="{x}" y="{y-fs}" width="0" height="{fs*1.5:.0f}">'
                 f'<animate attributeName="width" calcMode="discrete" dur="{total:.2f}s" repeatCount="indefinite" keyTimes="{kt}" values="{vals}"/></rect></clipPath>')
        body += T(x, y, p, fs, color, 600, font=MONO, extra=f'clip-path="url(#tc{i})" textLength="{len(p)*cw:.1f}" lengthAdjust="spacingAndGlyphs"')
    cur = ';'.join(f'{x + e[2]*cw + 3:.1f}' for e in ev)
    body += (f'<g><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>'
             f'<rect x="{x}" y="{y-fs+2}" width="3" height="{fs+2}" fill="{CY}" filter="url(#glow)">'
             f'<animate attributeName="x" calcMode="discrete" dur="{total:.2f}s" repeatCount="indefinite" keyTimes="{kt}" values="{cur}"/></rect></g>')
    return defs, body


def cube(x, y, s, label, c, dur=5, dy=12, delay=0):
    w = s * .87; fs = int(s * .6)
    return (f'<g transform="translate({x},{y})"><animateTransform attributeName="transform" type="translate" values="{x},{y};{x},{y-dy};{x},{y}" dur="{dur}s" begin="{-delay}s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".4 0 .6 1;.4 0 .6 1"/>'
            f'<ellipse cx="0" cy="{s*1.6:.0f}" rx="{s*.9:.0f}" ry="{s*.22:.0f}" fill="{c}" opacity=".35" filter="url(#soft)"/>'
            f'<polygon points="0,{-s} {w:.1f},{-s/2} 0,0 {-w:.1f},{-s/2}" fill="{c}" stroke="#fff" stroke-opacity=".55"/>'
            f'<polygon points="{-w:.1f},{-s/2} 0,0 0,{s} {-w:.1f},{s/2}" fill="{c}" fill-opacity=".6" stroke="#fff" stroke-opacity=".3"/>'
            f'<polygon points="{w:.1f},{-s/2} 0,0 0,{s} {w:.1f},{s/2}" fill="{c}" fill-opacity=".32" stroke="#fff" stroke-opacity=".3"/>'
            + T(0, f'{-s/2 + fs*.34:.1f}', label, fs, '#0b0820', 800, 'middle', MONO) + '</g>')


def atom(x, y, r, dur=5, dy=10, delay=1):
    el = ''.join(f'<ellipse rx="{r}" ry="{r*.38:.1f}" fill="none" stroke="{CY}" stroke-width="2.2" transform="rotate({a})"/>' for a in (0, 60, 120))
    return (f'<g transform="translate({x},{y})"><animateTransform attributeName="transform" type="translate" values="{x},{y};{x},{y-dy};{x},{y}" dur="{dur}s" begin="{-delay}s" repeatCount="indefinite"/>'
            f'<g filter="url(#glow)"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/>{el}<circle r="4" fill="{CY}"/></g>'
            + T(0, r + 22, 'React', 13, CY, 700, 'middle', MONO) + '</g>')


# ---------------------------------------------------------------- HERO
def hero():
    W, H = 1200, 470
    phrases = ['MERN Stack Developer', 'Frontend Enthusiast', 'AI & LLM Explorer', 'Turning ideas into reality']
    td, tb = typing(phrases, 132, 390, 22, 13.2)
    b = bg(W, H) + particles(W, H, 45)
    # drifting code tokens
    toks = [('=>', 330, 70), ('const', 520, 56), ('git push', 640, 440), ('npm run dev', 90, 448), ('async/await', 700, 96), ('useState()', 1000, 430), ('</div>', 1160, 190)]
    for i, (t, x, y) in enumerate(toks):
        b += (f'<g opacity=".35">{T(x, y, t, 14, "#a5b4fc", 400, "start", MONO)}'
              f'<animateTransform attributeName="transform" type="translate" values="0,0;0,-14;0,0" dur="{6+i}s" repeatCount="indefinite"/></g>')
    # glass panel
    b += f'<rect x="40" y="40" width="700" height="390" rx="28" fill="url(#glass)" stroke="#fff" stroke-opacity=".16"/>'
    b += (f'<circle cx="72" cy="72" r="6" fill="#fb7185"/><circle cx="92" cy="72" r="6" fill="{AM}"/><circle cx="112" cy="72" r="6" fill="{GR}"/>'
          + T(136, 77, '~/jayameenakshi/portfolio', 14, '#94a3b8', 400, font=MONO))
    b += T(80, 190, 'Jayameenakshi', 72, 'url(#shine)', 800, extra='textLength="590" lengthAdjust="spacingAndGlyphs" filter="url(#glow)"')
    b += T(82, 232, 'FULL STACK WEB DEVELOPER', 22, '#c4b5fd', 700, extra='textLength="520" lengthAdjust="spacing"')
    b += (f'<rect x="82" y="246" width="60" height="4" rx="2" fill="url(#neon)"><animate attributeName="width" values="60;260;60" dur="5s" repeatCount="indefinite"/></rect>')
    b += T(82, 288, 'Building modern web experiences, learning continuously,', 18, '#cbd5e1')
    b += T(82, 314, 'and turning ideas into reality.', 18, '#cbd5e1')
    b += f'<rect x="80" y="346" width="620" height="56" rx="14" fill="#06041a" fill-opacity=".8" stroke="url(#neon)" stroke-opacity=".6"/>'
    b += T(100, 382, '>', 24, CY, 700, font=MONO)
    b += tb
    # --- scene (right)
    s = '<g transform="translate(0,25)">'
    s += f'<ellipse cx="930" cy="372" rx="200" ry="26" fill="{PU}" opacity=".5" filter="url(#soft)"/>'
    # developer behind laptop
    s += (f'<path d="M858 290 Q858 190 930 184 Q1002 190 1002 290 Z" fill="#4c1d95"/>'
          f'<circle cx="930" cy="142" r="33" fill="#fcd9b6"/>'
          f'<path d="M896 138 Q898 100 930 100 Q962 100 964 138 Q950 120 930 120 Q910 120 896 138 Z" fill="#1e1b4b"/>'
          f'<path d="M893 142 Q893 96 930 96 Q967 96 967 142" fill="none" stroke="{CY}" stroke-width="5" stroke-linecap="round"/>'
          f'<rect x="886" y="136" width="13" height="26" rx="6" fill="{PK}"/><rect x="961" y="136" width="13" height="26" rx="6" fill="{PK}"/>'
          f'<circle cx="918" cy="146" r="3" fill="#1e1b4b"><animate attributeName="ry" values="3;0.4;3" dur="4s" repeatCount="indefinite"/></circle>'
          f'<circle cx="942" cy="146" r="3" fill="#1e1b4b"/>'
          f'<path d="M921 158 Q930 165 939 158" fill="none" stroke="#9a3412" stroke-width="2" stroke-linecap="round"/>')
    # laptop
    s += (f'<rect x="815" y="205" width="230" height="140" rx="12" fill="#0f0b2e" stroke="{PU}" stroke-width="2" filter="url(#glow)"/>'
          f'<rect x="825" y="215" width="210" height="120" rx="6" fill="#070516"/>')
    lines = [(.5, CY, 0), (.7, '#a78bfa', 16), (.55, PK, 16), (.85, CY, 0), (.4, AM, 16), (.65, '#a78bfa', 32), (.5, GR, 16)]
    for i, (f, c, ind) in enumerate(lines):
        wmax = 170 * f - ind * .5
        s += (f'<rect x="{840+ind}" y="{228+i*15}" height="6" rx="3" fill="{c}" width="0">'
              f'<animate attributeName="width" values="0;{wmax:.0f};{wmax:.0f};0" keyTimes="0;.35;.9;1" dur="7s" begin="{i*.45:.2f}s" repeatCount="indefinite"/></rect>')
    s += (f'<rect x="1004" y="228" width="3" height="10" fill="{CY}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    s += (f'<path d="M795 345 H1065 L1085 363 Q1085 369 1077 369 H783 Q775 369 775 363 Z" fill="#1e1b4b" stroke="{PU}" stroke-opacity=".7"/>'
          f'<rect x="900" y="352" width="60" height="5" rx="2.5" fill="{PU}" opacity=".6"/></g>')
    b += s
    b += cube(760, 120, 30, '</>', CY, 5, 12, 0) + cube(1085, 125, 28, '{}', '#a78bfa', 6, 14, 2)
    b += cube(1125, 300, 26, '()', PK, 5.5, 10, 1) + cube(742, 300, 28, 'JS', AM, 6.5, 12, 3)
    b += atom(1140, 55, 22)
    save('hero.svg', W, H, 'Jayameenakshi - Full Stack Web Developer. Animated hero with typing effect, floating code cubes and a developer at a laptop', b, td)


# ---------------------------------------------------------------- SECTION HEADERS
def header(fname, title, sub):
    W, H = 1200, 96
    b = bg(W, H, 20) + particles(W, H, 12)
    b += T(44, 62, '</', 44, PU, 800, font=MONO, extra='opacity=".7" filter="url(#glow)"')
    b += T(1156, 62, '>', 44, CY, 800, 'end', MONO, 'opacity=".7" filter="url(#glow)"')
    b += T(600, 52, title, 36, 'url(#shine)', 800, 'middle', extra='letter-spacing="3" filter="url(#glow)"')
    b += T(600, 76, sub, 15, '#94a3b8', 400, 'middle', MONO, 'letter-spacing="2"')
    b += (f'<rect x="20" y="90" width="1160" height="2" fill="url(#neon)" opacity=".35"/>'
          f'<rect x="0" y="89" width="260" height="4" rx="2" fill="url(#neon)" filter="url(#glow)"><animate attributeName="x" values="-260;1200" dur="4s" repeatCount="indefinite"/></rect>')
    save(fname, W, H, title, b)


# ---------------------------------------------------------------- ORBIT
def orbit():
    W, H = 1200, 570; cx, cy = 600, 290; rx, ry = 430, 150
    path = f'M{cx-rx},{cy} a{rx},{ry} 0 1,1 {2*rx},0 a{rx},{ry} 0 1,1 {-2*rx},0'
    b = bg(W, H) + particles(W, H, 40)
    b += f'<ellipse cx="{cx}" cy="{cy+30}" rx="{rx+20}" ry="{ry+30}" fill="{PU}" opacity=".12" filter="url(#soft)"/>'
    b += (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#neon)" stroke-width="2" stroke-dasharray="3 9" opacity=".8">'
          f'<animate attributeName="stroke-dashoffset" values="0;-48" dur="3s" repeatCount="indefinite"/></ellipse>')
    b += f'<ellipse cx="{cx}" cy="{cy}" rx="300" ry="100" fill="none" stroke="#a78bfa" stroke-opacity=".25" stroke-dasharray="2 8"/>'
    p2 = f'M{cx+300},{cy} a300,100 0 1,1 -600,0 a300,100 0 1,1 600,0'
    for i, c in enumerate((CY, PK, AM)):
        b += (f'<circle r="5" fill="{c}" filter="url(#glow)"><animateMotion dur="14s" begin="{-i*4.6:.1f}s" repeatCount="indefinite" path="{p2}"/></circle>')
    # core
    b += (f'<defs><radialGradient id="core" cx=".35" cy=".3"><stop offset="0" stop-color="#c4b5fd"/><stop offset=".5" stop-color="#7c3aed"/><stop offset="1" stop-color="#1e1b4b"/></radialGradient></defs>'
          f'<circle cx="{cx}" cy="{cy}" r="74" fill="{PU}" opacity=".5" filter="url(#soft)"/>'
          f'<circle cx="{cx}" cy="{cy}" r="68" fill="url(#core)" stroke="#fff" stroke-opacity=".4"/>'
          f'<circle cx="{cx}" cy="{cy}" r="92" fill="none" stroke="{CY}" stroke-width="2" stroke-dasharray="10 14" opacity=".8"><animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="24s" repeatCount="indefinite"/></circle>'
          f'<circle cx="{cx}" cy="{cy}" r="106" fill="none" stroke="{PK}" stroke-width="1.5" stroke-dasharray="4 18" opacity=".7"><animateTransform attributeName="transform" type="rotate" from="360 {cx} {cy}" to="0 {cx} {cy}" dur="36s" repeatCount="indefinite"/></circle>'
          + T(cx, cy - 4, 'FULL', 24, '#fff', 800, 'middle', extra='letter-spacing="3"')
          + T(cx, cy + 24, 'STACK', 24, '#fff', 800, 'middle', extra='letter-spacing="3"'))
    cards = [('Frontend', 'HTML · CSS · JS · React', CY, '</>'), ('Backend', 'Node.js · Express', GR, 'JS'),
             ('Database', 'MongoDB · NoSQL', '#4ade80', 'DB'), ('AI', 'LLMs · RAG · Python', PK, 'AI'),
             ('Git / GitHub', 'Version control', AM, 'Git')]
    dur = 30
    for i, (t, sub, c, ic) in enumerate(cards):
        card = (f'<rect x="-120" y="-40" width="240" height="80" rx="20" fill="#0d0a2a" fill-opacity=".85" stroke="{c}" stroke-opacity=".8" stroke-width="1.5" filter="url(#glow)"/>'
                f'<rect x="-120" y="-40" width="240" height="80" rx="20" fill="url(#glass)"/>'
                f'<rect x="-104" y="-24" width="48" height="48" rx="14" fill="{c}" fill-opacity=".2" stroke="{c}"/>'
                + T(-80, 8, ic, 20, c, 800, 'middle', MONO) + T(-42, -3, t, 22, '#fff', 700) + T(-42, 22, sub, 13, '#a5b4fc'))
        b += (f'<g><animateMotion dur="{dur}s" begin="{-i*dur/5:.1f}s" repeatCount="indefinite" path="{path}"/>'
              f'<g><animateTransform attributeName="transform" type="scale" values=".95;.7;.95;1.12;.95" keyTimes="0;.25;.5;.75;1" dur="{dur}s" begin="{-i*dur/5:.1f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values=".9;.55;.9;1;.9" keyTimes="0;.25;.5;.75;1" dur="{dur}s" begin="{-i*dur/5:.1f}s" repeatCount="indefinite"/>{card}</g></g>')
    save('orbit.svg', W, H, '3D developer intro: Frontend, Backend, Database, AI and Git/GitHub cards orbiting a Full Stack core', b)


# ---------------------------------------------------------------- ABOUT terminal
def about():
    W, H = 1000, 330
    b = bg(W, H) + particles(W, H, 18)
    b += f'<rect x="30" y="30" width="940" height="270" rx="22" fill="#05030f" fill-opacity=".75" stroke="url(#neon)" stroke-opacity=".6"/>'
    b += (f'<circle cx="62" cy="58" r="6" fill="#fb7185"/><circle cx="82" cy="58" r="6" fill="{AM}"/><circle cx="102" cy="58" r="6" fill="{GR}"/>'
          + T(500, 63, 'about.sh', 14, '#64748b', 400, 'middle', MONO))
    L = [('$ whoami', CY), ('> Jayameenakshi · Aspiring Full Stack Web Developer', '#e2e8f0'), ('$ cat focus.txt', CY),
         ('> MERN Stack · Frontend · AI · Modern Web Apps', '#e2e8f0'), ('$ git status', CY),
         ('> Computer Science Graduate · Fresher · Learning daily', '#e2e8f0')]
    T_ = 14; cw = 14.4; defs = ''
    for i, (txt, c) in enumerate(L):
        y = 108 + i * 34; st = .12 + i * .13; en = st + .1
        defs += (f'<clipPath id="ab{i}"><rect x="60" y="{y-22}" width="0" height="30"><animate attributeName="width" values="0;0;{len(txt)*cw+4:.0f};{len(txt)*cw+4:.0f}" keyTimes="0;{st:.2f};{en:.2f};1" dur="{T_}s" repeatCount="indefinite"/></rect></clipPath>')
        b += T(60, y, txt, 24, c, 600 if c == CY else 400, font=MONO, extra=f'clip-path="url(#ab{i})"')
    # spinning ring decoration
    rx_, ry_ = 850, 190
    b += (f'<circle cx="{rx_}" cy="{ry_}" r="70" fill="{PU}" opacity=".25" filter="url(#soft)"/>'
          f'<circle cx="{rx_}" cy="{ry_}" r="64" fill="none" stroke="{CY}" stroke-width="2" stroke-dasharray="8 10"><animateTransform attributeName="transform" type="rotate" from="0 {rx_} {ry_}" to="360 {rx_} {ry_}" dur="20s" repeatCount="indefinite"/></circle>'
          f'<circle cx="{rx_}" cy="{ry_}" r="46" fill="none" stroke="{PK}" stroke-width="2" stroke-dasharray="3 9"><animateTransform attributeName="transform" type="rotate" from="360 {rx_} {ry_}" to="0 {rx_} {ry_}" dur="14s" repeatCount="indefinite"/></circle>'
          + T(rx_, ry_ + 12, '</>', 34, '#fff', 800, 'middle', MONO, 'filter="url(#glow)"'))
    b += T(850, 285, '{ }', 40, PU, 800, 'middle', MONO, 'opacity=".5"') + T(930, 100, '( )', 30, PK, 800, 'middle', MONO, 'opacity=".5"')
    save('about.svg', W, H, 'Terminal card: Jayameenakshi, Aspiring Full Stack Web Developer focused on MERN, frontend, AI and modern web apps', b, defs)


# ---------------------------------------------------------------- TECH CARDS
def tech():
    W, H = 1000, 520
    items = [('HTML5', 'H5', '#e34f26'), ('CSS3', 'C3', '#1572b6'), ('JavaScript', 'JS', '#f7df1e'), ('React', 'Rx', '#61dafb'), ('Bootstrap', 'B', '#a78bfa'),
             ('Node.js', 'No', '#68a063'), ('Express.js', 'Ex', '#e2e8f0'), ('MongoDB', 'Mg', '#47a248'), ('Python', 'Py', '#4b8bbe'), ('Git', 'Git', '#f05032'),
             ('GitHub', 'GH', '#c9d1d9'), ('VS Code', 'VS', '#2f9cf0'), ('Figma', 'Fg', '#f24e1e')]
    b = bg(W, H) + particles(W, H, 25)
    cw_, ch_ = 168, 140; gap = 14
    rows = [items[0:5], items[5:10], items[10:13]]
    for r, row in enumerate(rows):
        total = len(row) * cw_ + (len(row) - 1) * gap; x0 = (W - total) / 2
        for k, (name, ab, c) in enumerate(row):
            x = x0 + k * (cw_ + gap); y = 36 + r * (ch_ + 16)
            d = 4 + (r * 5 + k) % 4; dl = (r * 5 + k) * .5
            b += (f'<g transform="translate({x:.0f},{y})"><animateTransform attributeName="transform" type="translate" values="{x:.0f},{y};{x:.0f},{y-7};{x:.0f},{y}" dur="{d}s" begin="{-dl}s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".4 0 .6 1;.4 0 .6 1"/>'
                  f'<rect width="{cw_}" height="{ch_}" rx="22" fill="#0d0a2a" fill-opacity=".85" stroke="{c}" stroke-opacity=".55"/>'
                  f'<rect width="{cw_}" height="{ch_}" rx="22" fill="url(#glass)"/>'
                  f'<circle cx="{cw_/2}" cy="52" r="34" fill="{c}" opacity=".18" filter="url(#soft)"/>'
                  f'<rect x="{cw_/2-30}" y="22" width="60" height="60" rx="18" fill="{c}" fill-opacity=".16" stroke="{c}" stroke-opacity=".9"/>'
                  + T(cw_ / 2, 62, ab, 24, c, 800, 'middle', MONO) + T(cw_ / 2, 116, name, 20, '#e2e8f0', 700, 'middle')
                  + f'<rect x="{cw_/2-24}" y="{ch_-10}" width="48" height="3" rx="1.5" fill="{c}" opacity=".7"/></g>')
    save('tech-cards.svg', W, H, 'Technology cards: HTML, CSS, JavaScript, React, Bootstrap, Node.js, Express.js, MongoDB, Python, Git, GitHub, VS Code, Figma', b)


# ---------------------------------------------------------------- 3D DASHBOARD
def dashboard():
    W, H = 1200, 540
    b = bg(W, H) + particles(W, H, 30)
    b += T(600, 40, 'DEV ACTIVITY CORE', 16, CY, 700, 'middle', MONO, 'letter-spacing="6" opacity=".9"')
    cx0, cy0 = 600, 150; n = 6; sx, sy = 44, 25; hw, hd = 40, 22.5
    cols = ''
    for s_ in range(0, 2 * n - 1):
        for i in range(n):
            j = s_ - i
            if j < 0 or j >= n: continue
            x = cx0 + (i - j) * sx; y = cy0 + (i + j) * sy
            h = 12 + 56 * abs(math.sin(i * .9 + .4) * math.cos(j * .7 + .2)) + random.uniform(0, 10)
            t = min(1, h / 70); base = mix('#6d28d9', '#22d3ee', t)
            top = mix(base, '#ffffff', .3); left = base; right = shade(base, .55)
            d = random.uniform(3, 6.5); dl = random.uniform(0, 6); lo = random.uniform(.5, .75)
            cols += (f'<g transform="translate({x:.0f},{y:.0f})"><g><animateTransform attributeName="transform" type="scale" values="1 {lo:.2f};1 1;1 {lo:.2f}" dur="{d:.1f}s" begin="{-dl:.1f}s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>'
                     f'<polygon points="{-hw},0 0,{hd} 0,{hd-h:.0f} {-hw},{-h:.0f}" fill="{left}"/>'
                     f'<polygon points="{hw},0 0,{hd} 0,{hd-h:.0f} {hw},{-h:.0f}" fill="{right}"/>'
                     f'<polygon points="0,{-hd-h:.0f} {hw},{-h:.0f} 0,{hd-h:.0f} {-hw},{-h:.0f}" fill="{top}" stroke="#fff" stroke-opacity=".25"/></g></g>')
    b += f'<ellipse cx="{cx0}" cy="{cy0+n*sy*1+10}" rx="330" ry="130" fill="{PU}" opacity=".25" filter="url(#soft)"/>'
    b += cols
    b += (f'<rect x="300" y="60" width="600" height="6" rx="3" fill="url(#neon)" opacity=".0" filter="url(#glow)"><animate attributeName="opacity" values="0;.8;0" dur="4s" repeatCount="indefinite"/><animate attributeName="y" values="70;450;70" dur="4s" repeatCount="indefinite"/></rect>')

    def tile(x, y, title, cap, c, deco):
        s = (f'<rect x="{x}" y="{y}" width="250" height="150" rx="20" fill="#0d0a2a" fill-opacity=".85" stroke="{c}" stroke-opacity=".5"/>'
             f'<rect x="{x}" y="{y}" width="250" height="150" rx="20" fill="url(#glass)"/>'
             + T(x + 20, y + 32, title, 15, c, 700, font=MONO, extra='letter-spacing="1"') + T(x + 20, y + 132, cap, 17, '#e2e8f0', 600))
        return s + deco(x, y, c)

    def spark(x, y, c):
        return (f'<path d="M{x+20},{y+100} L{x+60},{y+78} L{x+95},{y+88} L{x+130},{y+56} L{x+165},{y+68} L{x+200},{y+46} L{x+230},{y+55}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="320" filter="url(#glow)">'
                f'<animate attributeName="stroke-dashoffset" values="320;0;0;320" keyTimes="0;.5;.85;1" dur="5s" repeatCount="indefinite"/></path>')

    def bars(x, y, c):
        o = ''
        for k in range(12):
            h = random.randint(14, 56)
            o += (f'<rect x="{x+22+k*17}" y="{y+100-h}" width="10" height="{h}" rx="3" fill="{c}" opacity=".85"><animate attributeName="height" values="{h};{max(8,h-18)};{h}" dur="{random.uniform(2,4):.1f}s" repeatCount="indefinite"/>'
                  f'<animate attributeName="y" values="{y+100-h};{y+100-max(8,h-18)};{y+100-h}" dur="{random.uniform(2,4):.1f}s" repeatCount="indefinite"/></rect>')
        return o

    def dots(x, y, c):
        o = ''
        for k in range(6):
            o += (f'<circle cx="{x+36+k*34}" cy="{y+78}" r="11" fill="{c}" opacity=".3"><animate attributeName="opacity" values=".25;1;.25" dur="3s" begin="{k*.4:.1f}s" repeatCount="indefinite"/>'
                  f'<animate attributeName="r" values="9;13;9" dur="3s" begin="{k*.4:.1f}s" repeatCount="indefinite"/></circle>')
        return o

    def ring(x, y, c):
        return (f'<circle cx="{x+125}" cy="{y+80}" r="30" fill="none" stroke="#fff" stroke-opacity=".1" stroke-width="8"/>'
                f'<circle cx="{x+125}" cy="{y+80}" r="30" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round" stroke-dasharray="60 130" filter="url(#glow)"><animateTransform attributeName="transform" type="rotate" from="0 {x+125} {y+80}" to="360 {x+125} {y+80}" dur="5s" repeatCount="indefinite"/></circle>'
                + T(x + 125, y + 89, '∞', 26, '#fff', 700, 'middle'))
    b += tile(40, 70, 'CODING ACTIVITY', 'Always building', CY, spark)
    b += tile(40, 250, 'COMMITS', 'See contribution graph above', PU, bars)
    b += tile(910, 70, 'PROJECTS', '6 showcased', PK, dots)
    b += tile(910, 250, 'LEARNING', '8 topics in progress', AM, ring)
    b += T(600, 500, 'Illustrative visualization - decorative only, not real GitHub data. Live stats are in the sections above.', 14, '#64748b', 400, 'middle', MONO)
    save('dashboard-3d.svg', W, H, 'Futuristic 3D dashboard visualization representing coding activity, commits, projects and learning progress. Decorative, not real data', b)


# ---------------------------------------------------------------- SKILLS CHART
def skills():
    W, H = 1000, 560
    data = [('Frontend', 85, CY), ('JavaScript', 80, AM), ('React', 75, '#61dafb'), ('Backend', 65, GR), ('MongoDB', 65, '#4ade80'), ('Python', 60, BL), ('AI', 55, PK)]
    b = bg(W, H) + particles(W, H, 20)
    b += T(50, 52, 'SKILL PROFICIENCY', 18, '#c4b5fd', 700, font=MONO, extra='letter-spacing="4"')
    b += T(950, 52, 'approximate · personal self-assessment', 14, '#94a3b8', 400, 'end', MONO)
    tx, tw = 230, 640
    for i, (n, v, c) in enumerate(data):
        y = 100 + i * 56; w = tw * v / 100
        b += T(50, y + 26, n, 22, '#e2e8f0', 700)
        b += f'<rect x="{tx}" y="{y}" width="{tw}" height="34" rx="17" fill="#fff" fill-opacity=".06" stroke="#fff" stroke-opacity=".1"/>'
        b += (f'<linearGradient id="sg{i}" x1="0" x2="1"><stop offset="0" stop-color="{c}" stop-opacity=".55"/><stop offset="1" stop-color="{c}"/></linearGradient>'
              f'<rect x="{tx}" y="{y}" height="34" rx="17" fill="url(#sg{i})" filter="url(#glow)" width="0"><animate attributeName="width" from="0" to="{w:.0f}" dur="1.4s" begin="{i*.2:.1f}s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .2 1"/></rect>'
              f'<rect x="{tx+14}" y="{y+6}" width="0" height="6" rx="3" fill="#fff" opacity=".35"><animate attributeName="width" from="0" to="{max(w-40,10):.0f}" dur="1.4s" begin="{i*.2:.1f}s" fill="freeze"/></rect>'
              f'<circle cx="{tx}" cy="{y+17}" r="9" fill="#fff" opacity="0"><animate attributeName="cx" values="{tx+12};{tx+w-12:.0f}" dur="1.4s" begin="{i*.2:.1f}s" fill="freeze"/><animate attributeName="opacity" values="0;.9;0" keyTimes="0;.9;1" dur="1.4s" begin="{i*.2:.1f}s" fill="freeze"/></circle>')
        b += T(900, y + 26, f'{v}%', 22, c, 800, font=MONO)
    b += T(500, 515, 'Self-assessed estimates for fun and goal tracking - not GitHub statistics.', 14, '#64748b', 400, 'middle', MONO)
    save('skills-chart.svg', W, H, 'Skill proficiency chart (approximate self-assessment): Frontend 85, JavaScript 80, React 75, Backend 65, MongoDB 65, Python 60, AI 55 percent', b)


# ---------------------------------------------------------------- PROJECT CARDS
def card(fname, w, abbr, name_lines, chips, c1, c2, label):
    h = 250
    b = f'<defs><linearGradient id="hue" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient><radialGradient id="hg"><stop offset="0" stop-color="{c1}" stop-opacity=".45"/><stop offset="1" stop-color="{c1}" stop-opacity="0"/></radialGradient></defs>'
    b += f'<rect width="{w}" height="{h}" rx="24" fill="url(#bg)"/><ellipse cx="{w-60}" cy="30" rx="{w*.45:.0f}" ry="130" fill="url(#hg)"/><rect width="{w}" height="{h}" rx="24" fill="url(#grid)"/>'
    b += f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="24" fill="url(#glass)" stroke="#fff" stroke-opacity=".14"/>'
    b += (f'<rect x="2" y="2" width="{w-4}" height="{h-4}" rx="23" fill="none" stroke="url(#hue)" stroke-width="2.5" pathLength="100" stroke-dasharray="14 86"><animate attributeName="stroke-dashoffset" values="0;-100" dur="7s" repeatCount="indefinite"/></rect>')
    b += (f'<rect x="30" y="30" width="64" height="64" rx="18" fill="url(#hue)" filter="url(#glow)"/>' + T(62, 72, abbr, 26, '#fff', 800, 'middle', MONO))
    b += T(w - 30, 54, label, 14, '#94a3b8', 400, 'end', MONO)
    for k in range(4):
        hh = 10 + (k * 7) % 22
        b += f'<rect x="{w-30-k*12-8}" y="{90-hh}" width="8" height="{hh}" rx="3" fill="{c1}" opacity=".8"><animate attributeName="height" values="{hh};{hh+12};{hh}" dur="{2+k*.6:.1f}s" repeatCount="indefinite"/><animate attributeName="y" values="{90-hh};{90-hh-12};{90-hh}" dur="{2+k*.6:.1f}s" repeatCount="indefinite"/></rect>'
    y = 138
    for ln in name_lines:
        b += T(30, y, ln, 29, '#fff', 800); y += 34
    x = 30; cy_ = h - 46
    for ch in chips:
        wd = len(ch) * 9.2 + 26
        b += (f'<rect x="{x:.0f}" y="{cy_}" width="{wd:.0f}" height="30" rx="15" fill="{c1}" fill-opacity=".14" stroke="{c1}" stroke-opacity=".7"/>' + T(x + wd / 2, cy_ + 20, ch, 14, '#e2e8f0', 600, 'middle', MONO))
        x += wd + 10
    save(fname, w, h, f"{' '.join(name_lines)} project card: {', '.join(chips)}", b)


# ---------------------------------------------------------------- FEATURED
def featured():
    W, H = 1200, 440
    b = bg(W, H) + particles(W, H, 40)
    b += (f'<rect x="60" y="42" width="236" height="36" rx="18" fill="{AM}" fill-opacity=".16" stroke="{AM}"/>'
          f'<polygon points="86,50 90,60 101,60 92,66 96,76 86,70 76,76 80,66 71,60 82,60" fill="{AM}"><animateTransform attributeName="transform" type="rotate" values="0 86 63;360 86 63" dur="8s" repeatCount="indefinite"/></polygon>'
          + T(114, 66, 'FEATURED PROJECT', 15, AM, 800, font=MONO, extra='letter-spacing="2"'))
    b += T(58, 160, 'AI Career', 80, 'url(#shine)', 800, extra='filter="url(#glow)"') + T(58, 240, 'Advisor', 80, 'url(#shine)', 800, extra='filter="url(#glow)"')
    x = 60
    for ch in ['React', 'Node.js', 'MongoDB', 'LLM']:
        wd = len(ch) * 10 + 30
        b += f'<rect x="{x}" y="276" width="{wd:.0f}" height="34" rx="17" fill="{CY}" fill-opacity=".12" stroke="{CY}" stroke-opacity=".7"/>' + T(x + wd / 2, 299, ch, 16, '#e2e8f0', 600, 'middle', MONO)
        x += wd + 12
    for k, (lab, c) in enumerate([('Skills', CY), ('Courses', '#a78bfa'), ('Roadmap', PK)]):
        xx = 60 + k * 170
        b += (f'<rect x="{xx}" y="338" width="150" height="40" rx="12" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-opacity=".6"/>' + T(xx + 75, 364, lab, 18, c, 700, 'middle'))
        if k < 2:
            b += f'<path d="M{xx+154},358 h12 m-5,-5 l5,5 l-5,5" fill="none" stroke="#fff" stroke-opacity=".7" stroke-width="2"><animate attributeName="opacity" values=".2;1;.2" dur="1.8s" begin="{k*.5}s" repeatCount="indefinite"/></path>'
    cx, cy = 900, 195
    nodes = [(cx + 150 * math.cos(a), cy + 150 * math.sin(a)) for a in [i * math.pi / 6 + .3 for i in range(12)]]
    for k, (nx, ny) in enumerate(nodes):
        b += (f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="{CY}" stroke-opacity=".18"/><circle cx="{nx:.0f}" cy="{ny:.0f}" r="4" fill="{CY}"><animate attributeName="opacity" values=".2;1;.2" dur="{2+k%4}s" begin="{k*.25}s" repeatCount="indefinite"/></circle>')
    for r, c, d, rev in [(170, CY, 40, 0), (125, PK, 28, 1), (82, '#a78bfa', 18, 0)]:
        f_, t_ = (f'360 {cx} {cy}', f'0 {cx} {cy}') if rev else (f'0 {cx} {cy}', f'360 {cx} {cy}')
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-opacity=".7" stroke-width="2" stroke-dasharray="6 10"><animateTransform attributeName="transform" type="rotate" from="{f_}" to="{t_}" dur="{d}s" repeatCount="indefinite"/></circle>'
    hexp = ' '.join(f'{cx+52*math.cos(math.pi/3*i+math.pi/6):.1f},{cy+52*math.sin(math.pi/3*i+math.pi/6):.1f}' for i in range(6))
    b += (f'<circle cx="{cx}" cy="{cy}" r="70" fill="{PU}" opacity=".5" filter="url(#soft)"/>'
          f'<polygon points="{hexp}" fill="#1e1b4b" stroke="url(#neon)" stroke-width="3" filter="url(#glow)"><animate attributeName="stroke-opacity" values=".6;1;.6" dur="2.5s" repeatCount="indefinite"/></polygon>'
          + T(cx, cy + 15, 'AI', 44, '#fff', 800, 'middle', MONO, 'filter="url(#glow)"'))
    for lab, r, dur, c, off in [('Skills', 170, 18, CY, 0), ('Courses', 125, 14, '#a78bfa', 4), ('Roadmap', 170, 18, PK, 9)]:
        p = f'M{cx-r},{cy} a{r},{r} 0 1,1 {2*r},0 a{r},{r} 0 1,1 {-2*r},0'
        b += (f'<g><animateMotion dur="{dur}s" begin="{-off}s" repeatCount="indefinite" path="{p}"/>'
              f'<circle r="10" fill="{c}" filter="url(#glow)"/><rect x="14" y="-12" width="{len(lab)*11+14}" height="24" rx="12" fill="#07051a" fill-opacity=".85" stroke="{c}"/>' + T(21, 5, lab, 14, '#fff', 700) + '</g>')
    b += (f'<path d="M660,412 C740,372 800,430 880,400 S1030,370 1140,405" fill="none" stroke="url(#neon)" stroke-width="3" stroke-dasharray="8 8" opacity=".8"><animate attributeName="stroke-dashoffset" values="0;-64" dur="2.5s" repeatCount="indefinite"/></path>')
    for (px, py) in [(660, 412), (770, 396), (880, 400), (1000, 388), (1140, 405)]:
        b += f'<circle cx="{px}" cy="{py}" r="6" fill="#07051a" stroke="{CY}" stroke-width="2"><animate attributeName="r" values="5;8;5" dur="3s" begin="{(px%7)*.3:.1f}s" repeatCount="indefinite"/></circle>'
    save('featured-ai-career-advisor.svg', W, H, 'Featured project: AI Career Advisor, an animated futuristic AI core connecting skills, courses and roadmaps', b)


# ---------------------------------------------------------------- TIMELINES
def vtimeline(fname, items, label, color=CY, with_sub=True, icons=None):
    W = 700; rowh = 88; H = 50 + rowh * len(items) + 10
    b = bg(W, H, 22) + particles(W, H, 14)
    x0 = 78; y0 = 52; y1 = 50 + rowh * (len(items) - 1) + 38
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="url(#neon)" stroke-width="3" stroke-opacity=".5"/>'
    b += (f'<circle r="6" fill="#fff" filter="url(#glow)"><animate attributeName="cx" values="{x0};{x0}" dur="1s" repeatCount="indefinite"/><animate attributeName="cy" values="{y0};{y1}" dur="6s" repeatCount="indefinite"/></circle>')
    for i, it in enumerate(items):
        y = 50 + i * rowh + 38; c = [CY, '#a78bfa', PK, AM, GR, BL][i % 6]
        title, sub = it if isinstance(it, tuple) else (it, '')
        b += (f'<rect x="130" y="{y-32}" width="530" height="64" rx="18" fill="#0d0a2a" fill-opacity=".85" stroke="{c}" stroke-opacity=".5"/>'
              f'<rect x="130" y="{y-32}" width="530" height="64" rx="18" fill="url(#glass)"/>'
              f'<rect x="130" y="{y-32}" width="530" height="64" rx="18" fill="none" stroke="{c}" stroke-width="2" opacity="0"><animate attributeName="opacity" values="0;.9;0" dur="6s" begin="{i*.7:.1f}s" repeatCount="indefinite"/></rect>'
              f'<line x1="{x0+30}" y1="{y}" x2="130" y2="{y}" stroke="{c}" stroke-opacity=".6" stroke-dasharray="3 4"/>'
              f'<circle cx="{x0}" cy="{y}" r="22" fill="{c}" opacity=".2" filter="url(#soft)"/>'
              f'<circle cx="{x0}" cy="{y}" r="22" fill="#07051a" stroke="{c}" stroke-width="2"><animate attributeName="stroke-opacity" values=".5;1;.5" dur="3s" begin="{i*.4:.1f}s" repeatCount="indefinite"/></circle>')
        if icons:
            b += f'<g transform="translate({x0},{y})" stroke="{c}" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icons[i]}</g>'
        else:
            b += T(x0, y + 7, f'{i+1}', 20, c, 800, 'middle', MONO)
        if sub:
            b += T(156, y - 3, title, 26, '#fff', 700) + T(156, y + 22, sub, 15, '#a5b4fc', 400, font=MONO)
        else:
            b += T(156, y + 9, title, 26, '#fff', 700)
    save(fname, W, H, label, b)


def icons_set():
    return [
        '<polygon points="-15,-3 0,-11 15,-3 0,5"/><path d="M-9,1 V8 Q0,14 9,8 V1"/>',
        '<path d="M-6,-8 L-14,0 L-6,8 M6,-8 L14,0 L6,8 M3,-10 L-3,10"/>',
        '<ellipse rx="14" ry="5.5"/><ellipse rx="14" ry="5.5" transform="rotate(60)"/><ellipse rx="14" ry="5.5" transform="rotate(120)"/><circle r="2" fill="currentColor"/>',
        '<path d="M0,-15 C8,-8 8,3 5,10 H-5 C-8,3 -8,-8 0,-15 Z"/><circle cy="-4" r="3"/><path d="M-5,6 L-11,12 L-5,11 M5,6 L11,12 L5,11"/>',
        '<rect x="-9" y="-9" width="18" height="18" rx="3"/><path d="M-9,-3 H-14 M-9,3 H-14 M9,-3 H14 M9,3 H14 M-3,-9 V-14 M3,-9 V-14 M-3,9 V14 M3,9 V14"/>',
        '<circle r="14"/><ellipse rx="6" ry="14"/><path d="M-14,0 H14"/>']


# ---------------------------------------------------------------- QUOTE FRAMES
def quote_frames():
    W, H = 1000, 70
    for name, top in (('quote-top.svg', True), ('quote-bottom.svg', False)):
        yl = 16 if top else H - 16
        ys = H if top else 0
        b = (f'<path d="M20,{ys-(14 if top else -14)} V{yl+(8 if top else -8)} Q20,{yl} 28,{yl} H430" fill="none" stroke="url(#neon)" stroke-width="2.5" stroke-linecap="round"/>'
             f'<path d="M980,{ys-(14 if top else -14)} V{yl+(8 if top else -8)} Q980,{yl} 972,{yl} H570" fill="none" stroke="url(#neon)" stroke-width="2.5" stroke-linecap="round"/>'
             f'<line x1="28" y1="{yl}" x2="972" y2="{yl}" stroke="url(#neon)" stroke-width="2" stroke-dasharray="2 10" opacity=".5"><animate attributeName="stroke-dashoffset" values="0;-24" dur="2s" repeatCount="indefinite"/></line>'
             f'<circle r="5" fill="#fff" filter="url(#glow)"><animate attributeName="cx" values="28;972;28" dur="7s" repeatCount="indefinite"/><animate attributeName="cy" values="{yl};{yl};{yl}" dur="7s" repeatCount="indefinite"/></circle>'
             f'<circle cx="500" cy="{yl}" r="24" fill="#0d0a2a" stroke="url(#neon)" stroke-width="2" filter="url(#glow)"/>'
             + T(500, yl + (18 if top else 20), '“' if top else '”', 52, 'url(#neon)', 800, 'middle', 'Georgia,serif'))
        save(name, W, H, 'Animated quote frame', b)


# ---------------------------------------------------------------- FOOTER
def footer():
    W, H = 1200, 320
    b = bg(W, H) + particles(W, H, 40)
    waves = [(CY, .22, 190, 9, 0), (PU, .3, 215, 12, 2), (PK, .25, 240, 15, 4)]
    for c, o, yb, d, dl in waves:
        p1 = f'M0,{yb} C150,{yb-40} 300,{yb+40} 450,{yb} S750,{yb-40} 900,{yb} S1050,{yb+40} 1200,{yb} V{H} H0 Z'
        p2 = f'M0,{yb} C150,{yb+40} 300,{yb-40} 450,{yb} S750,{yb+40} 900,{yb} S1050,{yb-40} 1200,{yb} V{H} H0 Z'
        b += f'<path d="{p1}" fill="{c}" fill-opacity="{o}"><animate attributeName="d" values="{p1};{p2};{p1}" dur="{d}s" begin="{-dl}s" repeatCount="indefinite"/></path>'
    star = '600,40 608,62 632,62 613,76 620,99 600,85 580,99 587,76 568,62 592,62'
    b += f'<polygon points="{star}" fill="{AM}" filter="url(#glow)"><animateTransform attributeName="transform" type="rotate" values="0 600 68;360 600 68" dur="12s" repeatCount="indefinite"/></polygon>'
    b += T(600, 150, 'Thanks for visiting my profile!', 46, 'url(#shine)', 800, 'middle', extra='filter="url(#glow)"')
    b += T(600, 192, "Let's build something amazing together.", 24, '#cbd5e1', 400, 'middle')
    save('footer.svg', W, H, "Thanks for visiting my profile! Let's build something amazing together.", b)


if __name__ == '__main__':
    hero(); orbit(); about(); tech(); dashboard(); skills(); featured(); quote_frames(); footer()
    for f, t, s in [('hdr-orbit.svg', 'THE FULL STACK UNIVERSE', 'frontend · backend · database · ai · git'),
                    ('hdr-about.svg', 'ABOUT ME', 'whoami'),
                    ('hdr-tech.svg', 'TECH STACK', 'tools i build with'),
                    ('hdr-stats.svg', 'GITHUB STATISTICS', 'live data from github'),
                    ('hdr-journey.svg', 'MY CODING JOURNEY', 'contribution graph'),
                    ('hdr-dashboard.svg', 'DEVELOPER DASHBOARD', 'activity core'),
                    ('hdr-skills.svg', 'SKILLS', 'self-assessed proficiency'),
                    ('hdr-projects.svg', 'PROJECT SHOWCASE', 'things i have built'),
                    ('hdr-learning.svg', 'CURRENTLY LEARNING', 'always leveling up'),
                    ('hdr-timeline.svg', 'CODING JOURNEY', 'from graduate to builder'),
                    ('hdr-trophies.svg', 'GITHUB TROPHIES', 'achievements'),
                    ('hdr-quote.svg', 'DEVELOPER QUOTE', 'words to code by'),
                    ('hdr-connect.svg', 'CONNECT WITH ME', "let's talk")]:
        header(f, t, s)
    card('card-newsify.svg', 480, 'NW', ['Newsify'], ['React', 'News API', 'Bootstrap'], CY, BL, 'PROJECT')
    card('card-banking.svg', 480, 'BK', ['Banking Management', 'System'], ['React', 'Node.js', 'MongoDB'], GR, CY, 'PROJECT')
    card('card-portfolio.svg', 480, 'PF', ['Personal Portfolio'], ['React', 'Vite', 'Tailwind'], PU, PK, 'PROJECT')
    card('card-ecommerce.svg', 480, 'EC', ['E-Commerce Website'], ['React', 'FastAPI', 'MongoDB'], AM, PK, 'PROJECT')
    card('card-phishing.svg', 980, 'XAI', ['Explainable AI-Based Phishing', 'Website Detection System'], ['Python', 'Machine Learning', 'Explainable AI'], PK, PU, 'AI / SECURITY')
    vtimeline('timeline-learning.svg', [('Advanced React', 'Hooks · Patterns · Performance'), ('Node.js & Express', 'REST APIs · Middleware · Auth'),
                                        ('MongoDB', 'Schemas · Queries · Aggregation'), ('Next.js', 'Routing · SSR · Full-stack React'),
                                        ('FastAPI', 'Async Python APIs'), ('AI / LLM', 'Prompting · Integrations'),
                                        ('RAG', 'Embeddings · Vector search'), ('DSA', 'Problem solving · Algorithms')],
              'Currently learning timeline: Advanced React, Node.js and Express, MongoDB, Next.js, FastAPI, AI and LLM, RAG, DSA')
    vtimeline('timeline-journey.svg', ['Computer Science Graduate', 'Web Development', 'React', 'Full Stack Development', 'AI & LLM', 'Building Real-World Projects'],
              'Coding journey: Computer Science Graduate, Web Development, React, Full Stack Development, AI and LLM, Building Real-World Projects', icons=icons_set())
    print(sorted(os.listdir(OUT)))

