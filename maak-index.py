"""Gebruik: python3 maak-index.py <pad-naar-gepubliceerde-html>
Zet de app om naar een volledige pagina (doctype, charset, viewport, zoekinfo) in index.html."""
import sys
URL = "https://juliettedmt.github.io/Bucket-Ghent/"
HEAD = (
    '<!doctype html><html lang="nl"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<title>Bucket Ghent – Gentse Bucketlist voor studenten</title>'
    '<meta name="description" content="Bucket Ghent: alle studentenactiviteiten in Gent op één plek. Kalender, deadlines, bedrijfsevents, runclubs, eten, food deals, sport, shopping, matches en politiek. Elke dag bijgewerkt.">'
    '<meta name="keywords" content="Bucket Ghent, Gentse Bucketlist, studenten Gent, UGent, HOGENT, Artevelde, studentenactiviteiten Gent, events Gent, bucketlist Gent">'
    '<meta name="author" content="Juliette Dumont">'
    f'<link rel="canonical" href="{URL}">'
    '<meta property="og:type" content="website">'
    '<meta property="og:title" content="Bucket Ghent – Gentse Bucketlist">'
    '<meta property="og:description" content="Alle studentenactiviteiten in Gent op één plek, elke dag bijgewerkt.">'
    f'<meta property="og:url" content="{URL}">'
    ''
    '<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}</style></head><body>\n'
)
s = open(sys.argv[1], encoding="utf-8").read()
if s.lstrip().lower().startswith("<!doctype"):
    s = s[s.lower().index("<body>") + 6:]
    s = s[:s.lower().rindex("</body>")]
s = s.replace('', '')
open("index.html", "w", encoding="utf-8").write(HEAD + s.strip() + '\n</body></html>\n')
print("index.html bijgewerkt")
