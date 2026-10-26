#!/usr/bin/env python3
"""Builds index.html for treatfamily.org (inlines the arms SVG)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
shield = (ROOT / "assets" / "shield.svg").read_text(encoding="utf-8").replace(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 120"',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 120" class="arms"', 1)

PEOPLE = [
    ("The founders", "Within one generation of landing, the family was named in Connecticut's royal charter, had founded Newark, and held the colony's governorship.", [
        ("Richard Treat", "1584–1669/70", "https://en.wikipedia.org/wiki/Richard_Treat", "The immigrant. Baptised Richard Trott at Pitminster, married Alice Gaylord there in 1615, settled at Wethersfield by 1641; deputy and magistrate of the Connecticut General Court, and one of the nineteen patentees named in the 1662 Royal Charter."),
        ("Governor Robert Treat", "1624/5–1710", "https://en.wikipedia.org/wiki/Robert_Treat", "Richard's son. Helped lay out Milford as a teenager, led the Milford Puritans who founded Newark in 1666, commanded Connecticut's troops in King Philip's War, and was governor of the colony through the Charter Oak affair of 1687."),
        ("Lt. James Treat", "1634–1708/9", "https://archive.org/details/treatfamilyagen00treagoog", "Richard's youngest son; the Wethersfield line, from which the Revolutionary soldier Charles Treat descends."),
    ]),
    ("Preachers and the Revolutionary generation", "", [
        ("The Revd Samuel Treat", "1648–1716/17", "https://easthamthefirstencounter.org/from-nauset-to-eastham/the-reverend-samuel-treat/", "Governor Robert's son; minister at Eastham on Cape Cod for forty-five years and a missionary to the Nauset people."),
        ("Robert Treat Paine", "1731–1814", "https://en.wikipedia.org/wiki/Robert_Treat_Paine", "Rev. Samuel's grandson through his daughter Eunice. Prosecutor at the Boston Massacre trials, signer of the Declaration of Independence, first attorney general of Massachusetts."),
        ("Dr. Malachi Treat", "1735/6–1795", "https://collections.nlm.nih.gov/ocr/nlm:nlmuid-2571027R-bk", "Governor Robert's great-grandson; physician in the Revolutionary army and New York's health officer."),
        ("Joseph Treat", "1690–1756", None, "Rev. Samuel's son and the first Treat in Boston, a gunsmith licensed to the province; father of the Maine line."),
    ]),
    ("The Maine Treats", "Lt. Joshua Treat came up the Penobscot in 1759 as armourer at Fort Pownall, and the family stayed.", [
        ("Lt. Joshua Treat", "1729–1802", "https://en.wikipedia.org/wiki/Fort_Pownall", "Joseph the gunsmith's son; armourer and interpreter at Fort Pownall, and by tradition the first settler on the Penobscot above the fort. Frankfort, Prospect and Winterport descend from his household."),
        ("Maj. Robert Treat", "1752–1824", "https://archives.mainegenealogy.net/2011/04/names-from-major-robert-treats-day-book.html", "Joshua's half-brother, the family's man at Bangor; his day book is a record of the early river trade."),
        ("Gen. Joseph Treat", "1775–1853", "https://shop.mainehistory.org/products/wabanaki-homeland", "Maj. Robert's son; surveyed the Penobscot country for Massachusetts in 1820, with Penobscot guides, and was on the first recorded ascent of Katahdin."),
        ("Nathaniel Treat", "1798–1894", "https://en.wikipedia.org/wiki/Nathaniel_Treat", "Lt. Joshua's grandson, of Orono; lumberman, state senator and railroad man on the Penobscot."),
        ("Upham Stowers Treat", "1808–1883", "http://www.downeastfisheriestrail.org/fisheries-then/lobster/", "Lt. Joshua's grandson, of Eastport; among the first to can lobster, and the name on Treat Island at the mouth of the Bay of Fundy."),
        ("Charles Henry Treat", "1841–1910", "https://en.wikipedia.org/wiki/Charles_H._Treat", "Of Frankfort and New York; Treasurer of the United States under Theodore Roosevelt, 1905–09."),
        ("George Treat", "1817/19–1907", "https://en.wikipedia.org/wiki/George_Treat", "Of Frankfort; reached San Francisco in 1849, raced horses, fought slavery, and left his name on Treat Avenue in the Mission."),
    ]),
    ("Nineteenth century", "", [
        ("Judge Samuel Treat", "1815–1902", "https://www.fjc.gov/history/judges/treat-samuel", "Born Portsmouth, New Hampshire; United States district judge at St. Louis for thirty years, and a founder of what became the Washington University law school."),
        ("Judge Samuel Hubbel Treat", "1811–1887", "https://www.fjc.gov/history/judges/treat-samuel-hubbel-jr", "Of the Matthias line; Illinois Supreme Court justice and United States district judge, a colleague and friend of Abraham Lincoln on the circuit."),
        ("Howell B. Treat", "1833–1912", "https://en.wikipedia.org/wiki/Treat_(name)", "Private, 52nd Ohio Infantry; Medal of Honor for Buzzard's Roost, Georgia, 1864."),
        ("John Harvey Treat", "1839–1908", "https://www.findagrave.com/memorial/220519443/john-harvey-treat", "Of Lawrence, Massachusetts; the family historian. His 1893 genealogy is the book the family still keeps, and in 1902 he placed the brass to Richard and Robert in the church at Pitminster."),
        ("Amos Sherman Treat", "1816–1886", None, "Bridgeport lawyer; Connecticut's delegate to the 1861 Peace Conference and later Speaker of the state House."),
    ]),
    ("Twentieth century", "", [
        ("Judge William W. Treat", "1918–2010", "https://carsey.unh.edu/new-hampshire-listens/about/treat-fellowship", "Born Winterport, Maine. Chairman of the New Hampshire Republican party, national committeeman, probate judge for twenty-five years, founder of Bank Meridian, and a member of the UN sub-commission on minorities in Geneva. The Judge William W. Treat Fellowship at the University of New Hampshire carries his name."),
        ("Maj. Gen. Charles Gould Treat", "1859–1941", "https://en.wikipedia.org/wiki/Charles_Treat", "Born Orono; commandant of cadets at West Point and chief of the American military mission to Italy in 1918."),
        ("Payson Jackson Treat", "1879–1972", "https://searchworks.stanford.edu/view/4085699", "Stanford historian; held the first chair of Far Eastern history in the United States."),
        ("Roger Treat", "1905–1969", "https://en.wikipedia.org/wiki/Roger_Treat", "Sportswriter; compiled the Official Encyclopedia of Football and campaigned against the colour line in the pro game."),
        ("Herb Treat", "1900–1947", "https://en.wikipedia.org/wiki/Herb_Treat", "Princeton tackle, consensus All-American in 1922."),
        ("Asher E. Treat", "1907–2004", "https://u.osu.edu/biomuseum/2016/08/08/mites-and-moths/", "Biologist at City College of New York who discovered the mites that live in moths' ears."),
    ]),
]

LINE = [
    ("Richard Trott", "of Pitminster, who never left Somerset"),
    ("Richard Treat", "1584–1669, baptised and married at Pitminster; settler of Wethersfield; patentee of the 1662 Charter"),
    ("Robert Treat", "1624–1710, founder of Newark, Governor of Connecticut"),
    ("The Revd Samuel Treat", "1648–1717, minister at Eastham on Cape Cod"),
    ("Joseph Treat", "1690–1756, gunsmith of Boston"),
    ("Lt. Joshua Treat", "1729–1802, armourer at Fort Pownall, settler on the Penobscot"),
    ("Joshua Treat Jr.", "1756–1826, who built Frankfort's first log house and mill"),
    ("Col. William Treat", "1813–1879, of Winterport, of Treat & Co."),
    ("Joshua Treat", "1841–1926, of Winterport"),
    ("Joshua A. Treat II", "born 1881"),
    ("Judge William W. Treat", "1918–2010, born Winterport, of New Hampshire"),
]


def people_html():
    out = []
    for title, lede, entries in PEOPLE:
        out.append('<div class="era">')
        out.append(f'<div class="era-head"><h3>{title}</h3>' + (f'<p>{lede}</p>' if lede else '') + '</div>')
        out.append('<div class="era-people">')
        for name, dates, url, blurb in entries:
            nm = f'<a href="{url}">{name}</a>' if url else name
            out.append(f'<article class="person"><h4>{nm}</h4><p class="dates">{dates}</p><p>{blurb}</p></article>')
        out.append('</div></div>')
    return "\n".join(out)


def line_html():
    return "\n".join(f'<li><span class="gen" aria-hidden="true">{i}</span><div><b>{n}</b><span>{d}</span></div></li>'
                     for i, (n, d) in enumerate(LINE, 1))


HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>The Treat Family</title>
<meta name="description" content="The Treat family of America: descendants of Richard Trott of Pitminster, Somerset, who settled Wethersfield, Connecticut, in 1637. The family's games, its notable members, and the village it came from.">
<link rel="canonical" href="https://treatfamily.org/">
<meta property="og:title" content="The Treat Family">
<meta property="og:description" content="Descendants of Richard Trott of Pitminster, who settled Wethersfield, Connecticut, in 1637.">
<meta property="og:image" content="https://treatfamily.org/assets/pitminster-church.jpg">
<meta name="theme-color" content="#14213D">
<link rel="icon" href="assets/shield.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Public+Sans:wght@400;500;600&display=swap">
<style>
/* A family record set like an institution's: EB Garamond, a seventeenth-century face, for everything read;
   Public Sans for the things you press. The arms' colours: navy ground, gold, and the red kept to the shield.
   The one bold piece is the line, gold generation numerals running down a navy page. */
:root {{
  --navy: #14213D; --navy-2: #22355E; --gold: #D6A740; --gold-ink: #8A6516; --red: #B01E2D;
  --ink: #1A1D24; --slate: #4F5866; --mist: #EEF1F5; --rule: #D8DEE6; --white: #FFFFFF;
  --serif: "EB Garamond", Garamond, Georgia, serif; --sans: "Public Sans", "Helvetica Neue", Arial, sans-serif;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 4.5rem; }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
body {{ margin: 0; background: var(--white); color: var(--ink); font-family: var(--serif); font-size: 1.2rem; line-height: 1.6; -webkit-font-smoothing: antialiased; font-variant-numeric: oldstyle-nums; }}
a {{ color: var(--navy-2); text-decoration-thickness: 1px; text-underline-offset: 3px; }}
a:hover {{ color: var(--gold-ink); }}
:focus-visible {{ outline: 3px solid var(--gold); outline-offset: 3px; }}
.wrap {{ max-width: 72rem; margin: 0 auto; padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }}
.skip {{ position: absolute; left: -999px; top: 0; background: var(--gold); color: var(--navy); padding: .5rem 1rem; z-index: 10; font-family: var(--sans); }}
.skip:focus {{ left: 1rem; }}

/* Top bar */
.top {{ position: sticky; top: 0; z-index: 5; background: rgba(20,33,61,.97); border-bottom: 1px solid rgba(214,167,64,.35); font-family: var(--sans); }}
.top .wrap {{ display: flex; align-items: center; gap: 1.5rem; min-height: 3.75rem; }}
.brand {{ display: flex; align-items: center; gap: .65rem; color: var(--white); text-decoration: none; font-family: var(--serif); font-size: 1.3rem; font-weight: 500; white-space: nowrap; }}
.brand img {{ width: 1.5rem; height: auto; display: block; }}
.brand:hover {{ color: var(--white); }}
.top nav {{ margin-left: auto; display: flex; gap: 1.5rem; }}
.top nav a {{ color: #C9D2E0; text-decoration: none; font-size: .95rem; font-weight: 500; white-space: nowrap; }}
.top nav a:hover {{ color: var(--white); }}
@media (max-width: 48rem) {{
  .top .wrap {{ flex-wrap: wrap; gap: 0; min-height: 0; padding-top: .6rem; }}
  .top nav {{ margin: 0 -20px; padding: .55rem 20px .6rem; width: calc(100% + 40px); overflow-x: auto; gap: 1.3rem; scrollbar-width: none; }}
  .top nav::-webkit-scrollbar {{ display: none; }}
}}

/* Hero: the church the family left */
.hero {{ position: relative; color: var(--white); background: var(--navy); overflow: hidden; }}
.hero img.bg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; }}
.hero::before {{ content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(20,33,61,.94) 0%, rgba(20,33,61,.78) 45%, rgba(20,33,61,.25) 100%); z-index: 1; }}
@media (max-width: 48rem) {{ .hero::before {{ background: linear-gradient(180deg, rgba(20,33,61,.55) 0%, rgba(20,33,61,.92) 55%); }} }}
.hero::after {{ content: ""; position: absolute; inset: auto 0 0 0; height: 4px; background: var(--gold); z-index: 2; }}
.hero .wrap {{ position: relative; z-index: 2; padding-block: clamp(4rem, 2rem + 9vw, 9rem); }}
.hero .arms {{ width: 4.5rem; height: auto; display: block; margin-bottom: 1.6rem; filter: drop-shadow(0 4px 14px rgba(0,0,0,.45)); }}
.hero h1 {{ font-weight: 500; font-size: clamp(3.2rem, 2rem + 6vw, 6rem); line-height: .98; margin: 0 0 1.2rem; letter-spacing: -0.01em; }}
.hero p {{ font-size: clamp(1.25rem, 1.1rem + .6vw, 1.55rem); line-height: 1.45; color: #E6EAF1; max-width: 30ch; margin: 0 0 2.2rem; }}
@media (max-width: 48rem) {{ .hero .wrap {{ padding-top: 12rem; }} }}
.actions {{ display: flex; flex-wrap: wrap; gap: .75rem; }}
.btn {{ display: inline-flex; align-items: center; font-family: var(--sans); font-weight: 600; font-size: 1rem; line-height: 1.2; text-decoration: none; padding: .85rem 1.3rem; border-radius: 3px; border: 1px solid transparent; }}
.btn-gold {{ background: var(--gold); color: var(--navy); }}
.btn-gold:hover {{ background: #E4BC62; color: var(--navy); }}
.btn-line {{ color: var(--white); border-color: rgba(255,255,255,.5); }}
.btn-line:hover {{ color: var(--white); border-color: var(--white); background: rgba(255,255,255,.07); }}
.btn-navy {{ background: var(--navy); color: var(--white); }}
.btn-navy:hover {{ background: var(--navy-2); color: var(--white); }}

/* Sections */
section {{ padding-block: clamp(3.5rem, 2.5rem + 3.5vw, 6rem); }}
section.alt {{ background: var(--mist); }}
.sec-head {{ max-width: 44rem; margin-bottom: 2.4rem; }}
h2 {{ font-weight: 500; font-size: clamp(2.2rem, 1.6rem + 2.2vw, 3.2rem); line-height: 1.08; margin: 0 0 .7rem; color: var(--navy); letter-spacing: -0.005em; }}
.sec-head p {{ margin: 0; color: var(--slate); }}
p {{ margin: 0 0 1em; }}

/* Introduction */
.intro {{ display: grid; gap: 2.5rem 4.5rem; align-items: center; }}
@media (min-width: 52rem) {{ .intro {{ grid-template-columns: minmax(0, 1fr) 19rem; }} }}
.intro .lede {{ font-size: clamp(1.35rem, 1.2rem + .7vw, 1.7rem); line-height: 1.5; color: var(--navy); max-width: 36ch; margin: 0; }}
.intro .lede::first-letter {{ float: left; font-size: 4.1em; line-height: .82; padding: .06em .08em 0 0; color: var(--red); font-weight: 500; }}
figure {{ margin: 0; }}
figure img {{ width: 100%; height: auto; display: block; }}
figcaption {{ font-size: 1rem; color: var(--slate); margin-top: .6rem; line-height: 1.45; }}
.intro figure img {{ box-shadow: 0 18px 40px -18px rgba(20,33,61,.55); }}
@media (max-width: 51.99rem) {{ .intro figure {{ max-width: 15rem; }} }}

/* Games */
.games {{ display: grid; gap: 1.75rem; }}
@media (min-width: 46rem) {{ .games {{ grid-template-columns: 1fr 1fr; }} }}
.game {{ background: var(--white); border: 1px solid var(--rule); display: flex; flex-direction: column; min-width: 0; }}
.game img {{ width: 100%; height: auto; display: block; aspect-ratio: 8 / 5; object-fit: cover; border-bottom: 1px solid var(--rule); }}
.game .body {{ padding: 1.5rem 1.6rem 1.7rem; display: flex; flex-direction: column; flex: 1; }}
.game h3 {{ font-weight: 600; font-size: 1.65rem; line-height: 1.15; margin: 0 0 .5rem; color: var(--navy); }}
.game p {{ flex: 1; }}
.game .btn {{ align-self: flex-start; }}

/* Notable Treats */
.era {{ display: grid; gap: 1rem 3.5rem; padding: 2.2rem 0; border-top: 2px solid var(--navy); }}
.era:first-of-type {{ padding-top: 1.6rem; }}
@media (min-width: 56rem) {{ .era {{ grid-template-columns: 15rem minmax(0, 1fr); }} }}
.era-head h3 {{ font-weight: 500; font-size: 1.6rem; line-height: 1.15; margin: 0 0 .5rem; color: var(--navy); }}
.era-head p {{ color: var(--slate); font-size: 1.08rem; margin: 0; }}
.era-people {{ display: grid; gap: 0 2.5rem; }}
@media (min-width: 40rem) {{ .era-people {{ grid-template-columns: 1fr 1fr; }} }}
.person {{ padding: 1rem 0 1.1rem; border-bottom: 1px solid var(--rule); min-width: 0; }}
.person h4 {{ font-weight: 600; font-size: 1.25rem; line-height: 1.25; margin: 0; }}
.person h4 a {{ color: var(--navy); text-decoration: none; background-image: linear-gradient(var(--gold), var(--gold)); background-size: 100% 1px; background-position: 0 100%; background-repeat: no-repeat; }}
.person h4 a:hover {{ color: var(--gold-ink); }}
.person .dates {{ font-family: var(--sans); font-size: .85rem; color: var(--gold-ink); font-weight: 600; margin: .2rem 0 .45rem; font-variant-numeric: lining-nums tabular-nums; }}
.person p:last-child {{ margin: 0; font-size: 1.1rem; line-height: 1.55; }}

/* The line: the one bold piece */
.line-sec {{ background: var(--navy); color: #E6EAF1; position: relative; }}
.line-sec h2 {{ color: var(--white); }}
.line-sec .sec-head p {{ color: #B9C4D6; }}
ol.line {{ list-style: none; margin: 0; padding: 0; max-width: 50rem; }}
ol.line li {{ display: grid; grid-template-columns: 4.5rem minmax(0, 1fr); gap: 1.2rem; position: relative; padding-bottom: 1.6rem; }}
ol.line li::after {{ content: ""; position: absolute; left: 2.25rem; top: 3.6rem; bottom: .4rem; width: 1px; background: rgba(214,167,64,.45); }}
ol.line li:last-child::after {{ display: none; }}
ol.line .gen {{ font-size: 3rem; line-height: 1; color: var(--gold); text-align: center; font-variant-numeric: oldstyle-nums; padding-top: .1rem; }}
ol.line b {{ display: block; font-weight: 500; font-size: 1.5rem; line-height: 1.2; color: var(--white); }}
ol.line span {{ display: block; color: #B9C4D6; font-size: 1.12rem; margin-top: .2rem; }}
ol.line li.more {{ padding-bottom: 0; }}
ol.line li.more .gen {{ color: rgba(214,167,64,.6); }}

/* Pitminster */
.pit {{ display: grid; gap: 2.5rem 4rem; }}
@media (min-width: 56rem) {{ .pit {{ grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); align-items: start; }} }}
.pit .photos {{ display: grid; gap: 1.5rem; }}

/* Reading */
ul.reading {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 0 3rem; }}
@media (min-width: 48rem) {{ ul.reading {{ grid-template-columns: 1fr 1fr; }} }}
ul.reading li {{ padding: 1rem 0; border-top: 1px solid var(--rule); font-size: 1.12rem; }}

footer {{ background: #0F1A31; color: #A9B5C8; font-size: 1.05rem; }}
footer .wrap {{ display: grid; gap: 1.5rem 3rem; padding-block: 2.6rem 3rem; }}
@media (min-width: 52rem) {{ footer .wrap {{ grid-template-columns: auto minmax(0, 1fr); align-items: start; }} }}
footer .brand {{ font-size: 1.4rem; }}
footer p {{ margin: 0 0 .7rem; max-width: 62ch; }}
footer a {{ color: var(--gold); }}
footer .credit {{ font-size: .95rem; color: #8D9AB0; }}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="top"><div class="wrap">
<a class="brand" href="#top"><img src="assets/shield.svg" alt="" width="24" height="29">The Treat Family</a>
<nav aria-label="Sections">
<a href="#games">Games</a>
<a href="#people">Notable Treats</a>
<a href="#line">The line</a>
<a href="#pitminster">Pitminster</a>
<a href="#reading">Further reading</a>
</nav>
</div></header>

<div class="hero" id="top">
<img class="bg" src="assets/pitminster-church.jpg" width="1400" height="1050" alt="">
<div class="wrap">
{shield}
<h1>The Treat Family</h1>
<p>Descendants of Richard Trott of Pitminster, Somerset, who settled Wethersfield, Connecticut, in 1637.</p>
<div class="actions">
<a class="btn btn-gold" href="#games">Play the family games</a>
<a class="btn btn-line" href="#line">Follow the line</a>
</div>
</div>
</div>

<main id="main">
<section id="about"><div class="wrap intro">
<p class="lede">Nearly every Treat in America descends from one man, Richard Trott, baptised in the church at Pitminster in 1584, who crossed the Atlantic with his family in the 1630s and became Richard Treat of Wethersfield. His son Robert founded Newark and governed Connecticut; a grandson preached on Cape Cod; a great-great-grandson carried the name up the Penobscot, where the Maine Treats have been ever since.</p>
<figure>
<img src="assets/treat-arms.jpg" width="900" height="1127" alt="The Treat arms, painted: a shield of gold and red vertical stripes with a black bear in a silver canton, a helmet and crest above, and the name Treat beneath" loading="lazy">
<figcaption>The Treat arms, from a painting in the family. The bear in the corner is the one in this site's shield.</figcaption>
</figure>
</div></section>

<section id="games" class="alt"><div class="wrap">
<div class="sec-head">
<h2>The family games</h2>
<p>Two games built by the family, for the family. Both run in the browser on a phone or a laptop, and every square and every stop carries a line of the real history.</p>
</div>
<div class="games">
<article class="game">
<img src="assets/treatopoly-cover.jpg" width="800" height="500" alt="The Treatopoly title screen, with the Treat shield and options to play against the ancestors, pass and play, or host an online game" loading="lazy">
<div class="body">
<h3>Treatopoly</h3>
<p>The family's board game: forty spaces in order from Set Sail 1637 to Return to Pitminster, the Charter Oak and the Family Bible for the two decks, a lobster bake for free parking. Play online with family in other houses, or against bots named for the ancestors.</p>
<a class="btn btn-navy" href="games/treatopoly.html">Play Treatopoly</a>
</div>
</article>
<article class="game">
<img src="assets/treat-trail-cover.jpg" width="800" height="500" alt="The Treat Trail title screen, with the Treat arms and the route from Pitminster to Connecticut, Cape Cod, Maine and back" loading="lazy">
<div class="body">
<h3>The Treat Trail</h3>
<p>Three hundred and eighty-nine years from Pitminster in the style of the Oregon Trail: the crossing, Wethersfield, Newark, the Penobscot and on. Buy provisions, mind the rations and the weather, and get the family through.</p>
<a class="btn btn-navy" href="games/treat-trail.html">Play the Treat Trail</a>
</div>
</article>
</div>
</div></section>

<section id="people"><div class="wrap">
<div class="sec-head">
<h2>Notable Treats</h2>
<p>Checked against the 1893 genealogy and the published record. Most of these are cousins; the family's direct Maine line is set out below.</p>
</div>
{people_html()}
</div></section>

<section id="line" class="line-sec"><div class="wrap">
<div class="sec-head">
<h2>From Pitminster to the Penobscot</h2>
<p>The documented male line, generation by generation, as kept on the family tree and checked against the 1893 genealogy. The living generations are left off a public page.</p>
</div>
<ol class="line">
{line_html()}
</ol>
</div></section>

<section id="pitminster" class="alt"><div class="wrap pit">
<div>
<h2>Pitminster</h2>
<p>The church of St Andrew and St Mary, where Richard was baptised in 1584 and married in 1615, still stands four miles south of Taunton, with the brass that John Harvey Treat placed there in 1902.</p>
<p>The family keeps a separate site about the church, the village and the families who sailed from it, with a family wall where cousins can leave a note.</p>
<p><a class="btn btn-navy" href="https://pitminsterchurchonline.org">Visit Friends of Pitminster</a></p>
</div>
<div class="photos">
<figure>
<img src="assets/treat-brass.jpg" width="1400" height="791" alt="The brass of 1902 in the church at Pitminster, in memory of Richard Treat, alias Trott, baptised there in 1584, and his son Robert, Governor of Connecticut, erected by their descendant John Harvey Treat of America" loading="lazy">
<figcaption>The brass John Harvey Treat placed in the church in 1902, photographed on the family's visit in June 2026.</figcaption>
</figure>
</div>
</div></section>

<section id="reading"><div class="wrap">
<div class="sec-head"><h2>Further reading</h2></div>
<ul class="reading">
<li><a href="https://archive.org/details/treatfamilyagen00treagoog">The Treat Family: A Genealogy of Trott, Tratt, and Treat</a>, John Harvey Treat, 1893. The full book on the Internet Archive.</li>
<li><a href="https://portal.ct.gov/museumofcthistory/knowledge-base/articles/resources/governor-biographies/robert-treat">Governor Robert Treat</a>, from the Museum of Connecticut History.</li>
<li><a href="https://en.wikipedia.org/wiki/Richard_Treat">Richard Treat</a> and <a href="https://en.wikipedia.org/wiki/Robert_Treat">Robert Treat</a> on Wikipedia, and the <a href="https://en.wikipedia.org/wiki/Treat_(name)">list of people named Treat</a>.</li>
<li><a href="https://en.wikipedia.org/wiki/Church_of_St_Andrew_%26_St_Mary,_Pitminster">The church at Pitminster</a> and <a href="https://en.wikipedia.org/wiki/Pitminster">the village</a> on Wikipedia.</li>
<li><a href="https://en.wikipedia.org/wiki/Treat_Island">Treat Island</a>, Maine, named for Upham Treat.</li>
<li><a href="https://www.loc.gov/item/2011589602/">The 1859 Chace map of Waldo County</a>, with Treatville on it.</li>
</ul>
</div></section>
</main>

<footer><div class="wrap">
<a class="brand" href="#top"><img src="assets/shield.svg" alt="" width="24" height="29">The Treat Family</a>
<div>
<p>A family site, kept by Treat descendants in Maine. To add a name, correct a date, or reach the family, use the <a href="https://pitminsterchurchonline.org/contact.html">contact page at Friends of Pitminster</a>.</p>
<p class="credit">The bear in the arms is adapted from an illustration by Rinaldum on Wikimedia Commons (CC BY-SA 3.0). Photographs of Pitminster by the family, June 2026.</p>
</div>
</div></footer>
</body>
</html>
"""

(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print("wrote index.html", len(HTML))
