# Kit de tarjetas de memorización · Profesor Iván PB-IA

Kit para generar, para cualquier unidad, la app web de tarjetas (GitHub Pages) y las tarjetas para imprimir (normal y lectura fácil). Lo usa la skill `tarjetas-memorizacion-unidad`.

## Archivos
- `template.html` — la app (3 modos + ayuda, repaso por cajas, sesión corta, lectura fácil, insignia del profesor).
- `build_site.py deck.json carpeta_img salida/` — crea `salida/index.html` y copia `img/`.
- `print_cards.py deck.json carpeta_con_img salida.html [neae]` — HTML imprimible A4 (8 por hoja, o 6 en lectura fácil, a doble cara por el borde largo).
- `pdf.js entrada.html salida.pdf` — pasa el HTML a PDF con Playwright (`NODE_PATH=$(npm root -g) node pdf.js ...`).
- `fonts/` — Lexend Deca (OFL) para la versión de lectura fácil.
- `ejemplo/deck_u3.json` — mazo completo de la Unidad 3 como modelo.
- `ejemplo/figuras/` — scripts que dibujan Lewis y geometrías 3D (Unidad 3).

## Formato de `deck.json`
```json
{
 "meta": {"curso":"Química 2.º Bachillerato","unidad":2,"titulo":"Sistema periódico","clave":"u2",
          "repo":"Q2-Tarjetas-Sistema-periodico","url":"https://ivanpb26.github.io/Q2-Tarjetas-Sistema-periodico/",
          "modo2":{"tab":"Elementos","titulo":"Elemento sorpresa","chip":"★ Tipo PAU",
                   "tarea":"Hazlo tú primero: ... Después destapa cada paso.",
                   "ayuda":"texto para la pestaña Ayuda",
                   "print_hint":"pasos resumidos para la cara delantera impresa"}},
 "blocks": ["Bloque 1", "Bloque 2"],
 "cards": [{"id":"c0_0","b":0,"q":"Pregunta","a":"Respuesta (HTML corto)","img":"nombre_sin_ext_o_null","ex":1,"e":1}],
 "items": [{"id":"Br","title":"Z = 35","sub":"","info":"","e":1,"nota":"",
            "steps":[{"t":"Configuración","h":"HTML","img":null}]}],
 "errs":  [{"id":"e0","s":"Afirmación","v":0,"w":"Explicación","e":1}]
}
```
- `ex` = 1 muestra «★ Pregunta de examen». `e` = 1 entra en «Lectura fácil» y en el PDF de lectura fácil.
- `clave` distinta por unidad (guarda el progreso de cada alumno por separado).
- Imágenes en `img/` como `.jpg` (≈1000 px de ancho), referenciadas sin extensión.
