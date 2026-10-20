#!/usr/bin/env python3
"""Genera el HTML imprimible: python3 print_cards.py deck.json carpeta_con_img/ salida.html [neae]
Después: node pdf.js salida.html salida.pdf  (Playwright)."""
import json, sys, os
deck=json.load(open(sys.argv[1])); base=sys.argv[2]; out=sys.argv[3]
NEAE=len(sys.argv)>4 and sys.argv[4]=='neae'
m=deck['meta']; M2=m['modo2']; here=os.path.dirname(os.path.abspath(__file__))
COLS=2; ROWS=3 if NEAE else 4
BCOL=['#2E7D32','#1F4E8C','#6A1B9A','#00838F','#C62828','#AD6800','#455A64','#5D4037','#00695C']
SVG="<svg width='{w}' height='{w}' viewBox='0 0 24 24'><circle cx='12' cy='12' r='11' fill='{bg}'/><g fill='none' stroke='{fg}' stroke-width='1.4'><ellipse cx='12' cy='12' rx='9' ry='3.6'/><ellipse cx='12' cy='12' rx='9' ry='3.6' transform='rotate(60 12 12)'/><ellipse cx='12' cy='12' rx='9' ry='3.6' transform='rotate(120 12 12)'/></g><circle cx='12' cy='12' r='1.8' fill='{fg}'/></svg>"
LOGO="<div class='logo'>"+SVG.format(w=12,bg='#1B5E20',fg='#fff')+"<span>Aprende Química con Profesor Iván PB-IA</span></div>"
cards=[]
for c in deck['cards']:
    if NEAE and not c['e']: continue
    cards.append(dict(kind='c',col=BCOL[c['b']%len(BCOL)],tag=f"{c['b']+1}. {deck['blocks'][c['b']]}",ex=c['ex'],front=f"<div class='q'>{c['q']}</div>",back=f"<div class='a'>{c['a']}</div>"))
for it in deck['items']:
    if NEAE and not it['e']: continue
    fr=f"<div class='mf'>{it['title']}</div><div class='mn'>{it.get('sub','')}</div><div class='mz'>{it.get('info','')}</div><div class='mt'>{M2['print_hint']}</div>"
    img=next((s['img'] for s in it['steps'] if s.get('img')),None)
    lis=''.join(f"<li>{s['h']}</li>" for s in it['steps'])
    imgtag=("<img src='"+base+"/img/"+img+".jpg'>") if img else ''
    bk=f"<div class='mb'>{imgtag}<ol>{lis}</ol></div>"
    cards.append(dict(kind='m',col='#1B5E20',tag=f"{M2['titulo']} · tipo PAU",ex=1,front=fr,back=bk))
for e in deck['errs']:
    if NEAE and not e['e']: continue
    cards.append(dict(kind='e',col='#B71C1C',tag='Error típico · ¿V o F?',ex=0,front=f"<div class='vf'>«{e['s']}»</div><div class='mt'>¿Verdadero o falso?</div>",back=f"<div class='a'><b class='vv'>{'VERDADERO' if e['v'] else 'FALSO'}</b><br>{e['w']}</div>"))
per=COLS*ROWS; pages=[]
for i in range(0,len(cards),per):
    ch=cards[i:i+per]; fr=bk=''
    for r in range(ROWS):
        for c in range(COLS):
            k=r*COLS+c; x=ch[k] if k<len(ch) else None
            if x:
                star="<span class='st'>★ Pregunta de examen</span>" if x['ex'] and x['kind']=='c' else ''
                fr+=f"<div class='cell' style='grid-row:{r+1};grid-column:{c+1}'><div class='band' style='background:{x['col']}'>{x['tag']}</div>{star}<div class='body front'>{x['front']}</div><div class='num'>{i+k+1}</div>{LOGO}</div>"
                bk+=f"<div class='cell' style='grid-row:{r+1};grid-column:{COLS-c}'><div class='band' style='background:{x['col']}'>Respuesta</div><div class='body'>{x['back']}</div><div class='num'>{i+k+1}</div>{LOGO}</div>"
            else:
                fr+=f"<div class='cell empty' style='grid-row:{r+1};grid-column:{c+1}'></div>"
                bk+=f"<div class='cell empty' style='grid-row:{r+1};grid-column:{COLS-c}'></div>"
    pages.append(f"<section class='page'>{fr}</section><section class='page'>{bk}</section>")
fs='12.6pt' if NEAE else '9.2pt'; font="'Lexend Deca'" if NEAE else 'Inter'; lh='1.5' if NEAE else '1.32'
title=f"Tarjetas Unidad {m['unidad']} · {m['titulo']}"+(' · Lectura fácil' if NEAE else '')
fd=os.path.join(here,'fonts')
css=f"""@font-face{{font-family:'Lexend Deca';src:url('file://{fd}/LexendDeca-regular.ttf');font-weight:400}}
@font-face{{font-family:'Lexend Deca';src:url('file://{fd}/LexendDeca-bold.ttf');font-weight:700}}
@page{{size:A4;margin:0}} *{{box-sizing:border-box}} body{{margin:0;font-family:{font},sans-serif;color:#1d2321}}
.page{{width:210mm;height:297mm;padding:8mm;display:grid;grid-template-columns:repeat({COLS},1fr);grid-template-rows:repeat({ROWS},1fr);page-break-after:always}}
.cell{{border:0.4mm dashed #9aa79d;padding:3mm 4mm;position:relative;display:flex;flex-direction:column;overflow:hidden}} .cell.empty{{border-color:#eee}}
.band{{color:#fff;font-weight:700;font-size:{'10pt' if NEAE else '7.5pt'};border-radius:2mm;padding:0.8mm 2.5mm;align-self:flex-start;max-width:100%}}
.st{{align-self:flex-start;margin-top:1mm;font-size:{'8.5pt' if NEAE else '7pt'};font-weight:700;color:#7a5a00;background:#FFF3CD;border:0.3mm solid #E0B33A;border-radius:2mm;padding:0.3mm 1.6mm}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center;font-size:{fs};line-height:{lh}}} .front{{text-align:center}}
.q{{font-weight:700;font-size:1.12em;line-height:1.3}} .vf{{font-weight:700;font-size:1.08em}}
.mf{{font-size:2.3em;font-weight:800;color:#1B5E20;line-height:1.1}} .mn{{color:#5d6b63}} .mz{{font-size:.85em;color:#5d6b63}}
.mt{{margin-top:2mm;font-size:.82em;color:#5d6b63;font-style:italic}} .vv{{color:#B71C1C;font-size:1.05em}}
.mb{{display:flex;gap:2mm;align-items:center;font-size:{'.78em' if NEAE else '.82em'};line-height:1.25}} .mb img{{width:{'30mm' if NEAE else '26mm'};flex:none}}
.mb ol{{margin:0;padding-left:4mm}} .mb li{{margin:0.3mm 0}}
.logo{{display:flex;align-items:center;gap:1.2mm;margin-top:1mm;font-size:{'7pt' if NEAE else '6pt'};font-weight:700;color:#1B5E20}} .logo svg{{width:{'4mm' if NEAE else '3.4mm'};height:auto;flex:none}}
.num{{position:absolute;bottom:1.5mm;right:3mm;font-size:6.5pt;color:#9aa79d}}
.cover{{width:210mm;height:297mm;padding:22mm 20mm;page-break-after:always}} .cover h1{{color:#1B5E20;font-size:26pt;margin:0 0 4mm}} .cover p,.cover li{{font-size:12pt;line-height:1.5}}
.badge{{display:inline-flex;align-items:center;gap:3mm;background:#1B5E20;color:#fff;border-radius:99px;padding:2mm 5mm;font-weight:700;font-size:11pt;margin-bottom:10mm}}"""
cover=f"""<section class='cover'><div class='badge'>{SVG.format(w=30,bg='#fff',fg='#1B5E20')}<span>Aprende Química con Profesor Iván PB-IA</span></div><h1>{title}</h1>
<p>{m['curso']} · {len(cards)} tarjetas para recortar.</p>
<ul><li><b>Cómo imprimir:</b> a doble cara, girando por el <b>borde largo</b>. Cada respuesta queda detrás de su pregunta.</li>
<li><b>Cómo recortar:</b> por las líneas discontinuas. El número de la esquina te ayuda a emparejar pregunta y respuesta.</li>
<li><b>Cómo estudiar:</b> lee la pregunta, responde en voz alta y después mira la respuesta. Haz tres montones: «lo sé», «dudo» y «no lo sé». Repasa más a menudo los dos últimos.</li>
<li><b>★ Pregunta de examen:</b> son las que suelen caer en el examen y en la PAU.</li>
<li>Colores: cada bloque del tema tiene su color; las tarjetas «{M2['titulo'].lower()}», en verde, y los errores típicos, en rojo.</li></ul>
<p style='margin-top:12mm;color:#5d6b63'>Versión web con repaso automático: <b>{m['url'].replace('https://','')}</b></p></section><section class='cover' style='padding:0'></section>"""
open(out,'w').write(f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><title>{title}</title><style>{css}</style></head><body>{cover}{''.join(pages)}</body></html>")
print(out,len(cards),'tarjetas',len(pages)*2+2,'páginas')
