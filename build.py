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
        out.append(f'<h3>{title}</h3>')
        if lede:
            out.append(f'<p class="lede-s">{lede}</p>')
        out.append('<dl class="people">')
        for name, dates, url, blurb in entries:
            nm = f'<a href="{url}">{name}</a>' if url else name
            out.append(f'<dt>{nm} <span>{dates}</span></dt><dd>{blurb}</dd>')
        out.append('</dl>')
    return "\n".join(out)


def line_html():
    return "\n".join(f'<li><b>{n}</b> <span>{d}</span></li>' for n, d in LINE)


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
<link rel="icon" href="assets/shield.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap">
<style>
/* Layout: a family record. One column of Garamond, Cinzel for the names that matter,
   the arms' colours used sparingly: navy ground, gold rule, red only on the shield. */
:root {{
  --navy: #14213D; --navy-2: #1E2F55; --cream: #F3EFE6; --cream-2: #E9E3D5; --ink: #1B1B1B;
  --mute: #5C5A55; --gold: #B8902E; --gold-2: #D6A740; --line: #D9D2C2;
  --display: "Cinzel", Georgia, serif; --body: "EB Garamond", Georgia, "Times New Roman", serif;
  color-scheme: light;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --cream: #15192A; --cream-2: #1C2236; --ink: #E8E2D2; --mute: #A9A396; --line: #2F3A55; --gold: #D6A740; --gold-2: #E6C062; color-scheme: dark; }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--cream); color: var(--ink); font-family: var(--body); font-size: 1.125rem; line-height: 1.55; }}
a {{ color: var(--gold); text-decoration-thickness: 1px; text-underline-offset: 3px; }}
a:hover {{ color: var(--ink); }}
:focus-visible {{ outline: 2px solid var(--gold-2); outline-offset: 3px; }}
.wrap {{ max-width: 46rem; margin: 0 auto; padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }}
header.top {{ background: var(--navy); color: var(--cream); }}
header.top .wrap {{ display: grid; grid-template-columns: 6.5rem 1fr; gap: 1.5rem; align-items: center; padding-block: 2.2rem; }}
.arms {{ width: 100%; height: auto; display: block; filter: drop-shadow(0 2px 6px rgba(0,0,0,.4)); }}
header.top h1 {{ font-family: var(--display); font-weight: 600; font-size: clamp(1.7rem, 1.1rem + 2.6vw, 2.7rem); letter-spacing: .06em; margin: 0 0 .35rem; line-height: 1.1; color: #F3EFE6; }}
header.top p {{ margin: 0; color: #D7D2C4; font-size: 1.05rem; max-width: 40ch; }}
nav.jump {{ border-bottom: 1px solid var(--line); }}
nav.jump ul {{ list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 0 1.4rem; }}
nav.jump a {{ display: inline-block; padding: .7rem 0; text-decoration: none; color: var(--ink); font-family: var(--display); font-size: .82rem; letter-spacing: .12em; }}
nav.jump a:hover {{ color: var(--gold); }}
section {{ padding-block: 2.4rem; border-bottom: 1px solid var(--line); }}
section:last-of-type {{ border-bottom: 0; }}
h2 {{ font-family: var(--display); font-weight: 400; font-size: 1.5rem; letter-spacing: .08em; margin: 0 0 1rem; }}
h2::after {{ content: ""; display: block; width: 3rem; border-top: 2px solid var(--gold); margin-top: .6rem; }}
h3 {{ font-family: var(--display); font-weight: 400; font-size: 1.05rem; letter-spacing: .08em; margin: 2rem 0 .5rem; color: var(--mute); }}
p {{ margin: 0 0 1em; }}
.lede {{ font-size: 1.25rem; }}
.lede-s {{ color: var(--mute); margin-bottom: .6rem; }}
.games {{ display: grid; gap: 1.5rem; }}
@media (min-width: 40rem) {{ .games {{ grid-template-columns: 1fr 1fr; }} }}
.game {{ border-top: 2px solid var(--gold); padding-top: .8rem; min-width: 0; }}
.game h3 {{ margin: 0 0 .4rem; color: var(--ink); font-size: 1.15rem; }}
.btn {{ display: inline-block; font-family: var(--display); font-size: .85rem; letter-spacing: .1em; color: var(--cream); background: var(--navy); text-decoration: none; padding: .65rem 1.1rem; border: 1px solid var(--navy); }}
.btn:hover {{ background: var(--gold); border-color: var(--gold); color: #14213D; }}
@media (prefers-color-scheme: dark) {{ .btn {{ background: var(--gold); border-color: var(--gold); color: #14213D; }} .btn:hover {{ background: var(--cream); border-color: var(--cream); }} }}
dl.people {{ margin: 0; }}
dl.people dt {{ font-weight: 500; margin-top: .9rem; }}
dl.people dt span {{ color: var(--mute); font-weight: 400; font-variant-numeric: tabular-nums; margin-left: .35rem; }}
dl.people dd {{ margin: .1rem 0 0; }}
ol.line {{ list-style: none; padding: 0; margin: 0; counter-reset: g; }}
ol.line li {{ counter-increment: g; position: relative; padding: .5rem 0 .5rem 2.4rem; border-top: 1px solid var(--line); }}
ol.line li::before {{ content: counter(g); position: absolute; left: 0; top: .55rem; font-family: var(--display); color: var(--gold); font-variant-numeric: tabular-nums; }}
ol.line li:last-child {{ border-bottom: 1px solid var(--line); }}
ol.line b {{ font-weight: 500; }}
ol.line span {{ color: var(--mute); display: block; }}
figure {{ margin: 1.2rem 0 0; }}
figure.arms {{ margin: 0 0 1rem; max-width: 14rem; }}
@media (min-width: 44rem) {{ figure.arms {{ float: right; margin: .2rem 0 1rem 2rem; }} #about::after {{ content: ""; display: block; clear: both; }} }}
figure img {{ width: 100%; height: auto; display: block; }}
figcaption {{ font-size: .95rem; color: var(--mute); margin-top: .4rem; }}
ul.links {{ padding-left: 1.2rem; }}
ul.links li {{ margin: .35rem 0; }}
footer {{ background: var(--navy); color: #D7D2C4; font-size: .95rem; }}
footer .wrap {{ padding-block: 1.6rem 2.2rem; }}
footer a {{ color: var(--gold-2); }}
@media (max-width: 36rem) {{ header.top .wrap {{ grid-template-columns: 4.5rem 1fr; gap: 1rem; }} }}
</style>
</head>
<body>
<header class="top"><div class="wrap">
{shield}
<div>
<h1>The Treat Family</h1>
<p>Descendants of Richard Trott of Pitminster, Somerset, who settled Wethersfield, Connecticut, in 1637.</p>
</div>
</div></header>
<nav class="jump"><div class="wrap"><ul>
<li><a href="#games">GAMES</a></li>
<li><a href="#people">NOTABLE TREATS</a></li>
<li><a href="#line">THE LINE</a></li>
<li><a href="#pitminster">PITMINSTER</a></li>
<li><a href="#links">LINKS</a></li>
</ul></div></nav>

<main class="wrap">
<section id="about">
<figure class="arms">
<img src="assets/treat-arms.jpg" width="900" height="1127" alt="The Treat arms, painted: a shield of gold and red vertical stripes with a black bear in a silver canton, a helmet and crest above, and the name Treat beneath" loading="lazy">
<figcaption>The Treat arms, from a painting in the family. The bear in the corner is the one on this page.</figcaption>
</figure>
<p class="lede">Nearly every Treat in America descends from one man, Richard Trott, baptised in the church at Pitminster in 1584, who crossed the Atlantic with his family in the 1630s and became Richard Treat of Wethersfield. His son Robert founded Newark and governed Connecticut; a grandson preached on Cape Cod; a great-great-grandson carried the name up the Penobscot, where the Maine Treats have been ever since. This page is the family's own: its games, its notable members, and the village it came from.</p>
</section>

<section id="games">
<h2>Games</h2>
<p>Two games built by the family, for the family. Both run in the browser on a phone or a laptop; every square and every stop carries a line of the real history.</p>
<div class="games">
<div class="game">
<h3>Treatopoly</h3>
<p>The family's board game: forty spaces in order from Set Sail 1637 to Return to Pitminster, the Charter Oak and the Family Bible for the two decks, a lobster bake for free parking. Play online with family in other houses, or against bots named for the ancestors.</p>
<a class="btn" href="games/treatopoly.html">PLAY TREATOPOLY</a>
</div>
<div class="game">
<h3>The Treat Trail</h3>
<p>Three hundred and eighty-nine years from Pitminster in the style of the Oregon Trail: the crossing, Wethersfield, Newark, the Penobscot and on. Buy provisions, mind the rations and the weather, and get the family through.</p>
<a class="btn" href="games/treat-trail.html">PLAY THE TREAT TRAIL</a>
</div>
</div>
</section>

<section id="people">
<h2>Notable Treats</h2>
<p>Checked against the 1893 genealogy and the published record. Most of these are cousins; the ones in the family's direct Maine line are marked on the line below.</p>
{people_html()}
</section>

<section id="line">
<h2>The Line</h2>
<p>The documented male line from Pitminster to the Maine Treats of today, as kept on the family tree and checked against the 1893 genealogy. The living generations are left off a public page.</p>
<ol class="line">
{line_html()}
</ol>
</section>

<section id="pitminster">
<h2>Pitminster</h2>
<p>The church of St Andrew and St Mary, where Richard was baptised in 1584 and married in 1615, still stands four miles south of Taunton, with the brass that John Harvey Treat placed there in 1902. The family keeps a separate site about the church, the village and the families who sailed from it, with a family wall where cousins can leave a note.</p>
<p><a class="btn" href="https://pitminsterchurchonline.org">FRIENDS OF PITMINSTER</a></p>
<figure>
<img src="assets/treat-brass.jpg" width="1400" height="791" alt="The brass of 1902 in the church at Pitminster, in memory of Richard Treat, alias Trott, baptised there in 1584, and his son Robert, Governor of Connecticut, erected by their descendant John Harvey Treat of America" loading="lazy">
<figcaption>The brass John Harvey Treat placed in the church in 1902, photographed on the family's visit in June 2026.</figcaption>
</figure>
<figure>
<img src="assets/pitminster-church.jpg" width="1400" height="1050" alt="The church of St Andrew and St Mary at Pitminster at dusk, seen across the churchyard" loading="lazy">
<figcaption>St Andrew &amp; St Mary from the churchyard, June 2026.</figcaption>
</figure>
</section>

<section id="links">
<h2>Links</h2>
<ul class="links">
<li><a href="https://archive.org/details/treatfamilyagen00treagoog">The Treat Family: A Genealogy of Trott, Tratt, and Treat</a>, John Harvey Treat, 1893, the full book on the Internet Archive.</li>
<li><a href="https://en.wikipedia.org/wiki/Richard_Treat">Richard Treat</a> and <a href="https://en.wikipedia.org/wiki/Robert_Treat">Robert Treat</a> on Wikipedia, and the <a href="https://en.wikipedia.org/wiki/Treat_(name)">list of people named Treat</a>.</li>
<li><a href="https://portal.ct.gov/museumofcthistory/knowledge-base/articles/resources/governor-biographies/robert-treat">Governor Robert Treat</a>, from the Museum of Connecticut History.</li>
<li><a href="https://en.wikipedia.org/wiki/Church_of_St_Andrew_%26_St_Mary,_Pitminster">The church at Pitminster</a> and <a href="https://en.wikipedia.org/wiki/Pitminster">the village</a> on Wikipedia.</li>
<li><a href="https://en.wikipedia.org/wiki/Treat_Island">Treat Island</a>, Maine, named for Upham Treat.</li>
<li><a href="https://www.loc.gov/item/2011589602/">The 1859 Chace map of Waldo County</a>, with Treatville on it.</li>
</ul>
</section>
</main>

<footer><div class="wrap">
<p>A family site, kept by Treat descendants in Maine. To add a name, correct a date, or reach the family, use the <a href="https://pitminsterchurchonline.org/contact.html">contact page at Friends of Pitminster</a>. The bear in the arms is adapted from an illustration by Rinaldum on Wikimedia Commons (CC BY-SA 3.0).</p>
</div></footer>
</body>
</html>
"""

(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print("wrote index.html", len(HTML))
