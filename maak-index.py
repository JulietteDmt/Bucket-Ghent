"""Gebruik: python3 maak-index.py <pad-naar-gepubliceerde-html>
Zet de app om naar een volledige pagina (doctype, charset, viewport) in index.html."""
import sys
s = open(sys.argv[1], encoding="utf-8").read()
if not s.lstrip().lower().startswith("<!doctype"):
    s = ('<!doctype html><html lang="nl"><head><meta charset="utf-8">'
         '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
         '<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}</style></head><body>\n'
         + s + '\n</body></html>\n')
open("index.html", "w", encoding="utf-8").write(s)
print("index.html bijgewerkt")
