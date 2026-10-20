#!/usr/bin/env python3
"""Genera la web de tarjetas: python3 build_site.py deck.json carpeta_img salida/
Crea salida/index.html y copia las imágenes a salida/img/."""
import json, sys, os, shutil
here=os.path.dirname(os.path.abspath(__file__))
deck=json.load(open(sys.argv[1])); imgdir=sys.argv[2]; out=sys.argv[3]
m=deck['meta']
os.makedirs(out,exist_ok=True)
html=open(os.path.join(here,'template.html')).read()
for k,v in {'__TITULO__':m['titulo'],'__UNIDAD__':str(m['unidad']),'__CURSO__':m['curso'],'__TAB2__':m['modo2']['tab']}.items():
    html=html.replace(k,v)
html=html.replace('/*DATA*/',json.dumps(deck,ensure_ascii=False))
open(os.path.join(out,'index.html'),'w').write(html)
if os.path.isdir(imgdir):
    shutil.copytree(imgdir,os.path.join(out,'img'),dirs_exist_ok=True)
# comprobación: todas las imágenes citadas existen
used={c.get('img') for c in deck['cards'] if c.get('img')}|{s.get('img') for it in deck['items'] for s in it['steps'] if s.get('img')}
miss=[u for u in used if not os.path.exists(os.path.join(out,'img',u+'.jpg'))]
print(f"OK: {len(deck['cards'])} conceptos · {len(deck['items'])} {m['modo2']['tab'].lower()} · {len(deck['errs'])} errores · imágenes que faltan: {miss}")
