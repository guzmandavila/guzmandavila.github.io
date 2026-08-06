# Ronald Guzmán Dávila — Sitio personal
## Propuesta de arquitectura de información + sistema de diseño
*(Fase 0 — antes de escribir código)*

---

## 1. Arquitectura de la información

### 1.1 Mapa del sitio

```
/ (hub) ──────────────► Portfolio: hero + reel, experiencia, casos de estudio, colaboraciones, contacto
├── /work/<slug>/  ───► Páginas individuales de caso de estudio (SEO, OG, JSON-LD por proyecto)
├── /periplo/      ───► Landing Periplo Studio (identidad propia)
├── /clowder/      ───► Landing Clowder (identidad propia)
├── /tools/        ───► Calculadora de tarifas de grading, checklist de entrega, (espacio para más utilidades)
├── /dashboard/    ───► Tracker personal: metas, hábitos, proyectos (localStorage/IndexedDB, sin backend, noindex)
└── /assets/       ───► Fuentes de verdad compartidas: tokens CSS, base CSS, fuentes, JS de utilidades, iconos
```

`index.html` (el hub) **es** el portafolio — no hace falta duplicar contenido. Vistazo de la home, siguiendo tu bio de referencia:

1. Hero — nombre, roles (Producer · Shooter · Editor · Colorist · Audio Post), ubicación, disponibilidad remota
2. Reel destacado (embed liviano, sin autoplay pesado — thumbnail + play-on-click para no penalizar LCP)
3. Pipeline (roles de producción + herramientas de post)
4. Experiencia (Vistazo, UCSG)
5. Casos de estudio seleccionados → cada uno enlaza a `/work/<slug>/` con su propia página (mejor SEO/OG que anclas en una sola página)
6. Colaboraciones (Canoa Suites, NYU, ICHE, Cervecería Nacional, Veolia/Gadere, Interagua, Ecotec, Ministerio de Turismo)
7. Contacto + enlaces a Periplo / Clowder / Tools

### 1.2 Estructura de repositorio (GitHub Pages)

```
/
├── index.html
├── /work/
│   └── <slug>/index.html          (una carpeta por caso de estudio)
├── /periplo/
│   ├── index.html
│   └── /css/theme.css             (overrides de identidad Periplo)
├── /clowder/
│   ├── index.html
│   └── /css/theme.css             (overrides de identidad Clowder)
├── /tools/
│   ├── index.html
│   ├── tarifas.html
│   └── checklist.html
├── /dashboard/
│   └── index.html                 (meta robots: noindex)
├── /assets/
│   ├── /css/  tokens.css · base.css · utilities.css
│   ├── /js/   módulos ES nativos (uno por feature)
│   ├── /fonts/
│   └── /img/  (WebP/AVIF, con srcset)
├── manifest.json
├── sitemap.xml
├── robots.txt
├── /.github/workflows/  deploy.yml · lighthouse-ci.yml
└── README.md
```

`tokens.css` define variables compartidas (escalas de espaciado/tipografía, radios, timing de animación). Cada landing (`/periplo`, `/clowder`) sobreescribe solo las variables de color/tipografía de marca — así no se duplica layout ni lógica.

---

## 2. Sistema de diseño — Núcleo (Hub / Portfolio / Periplo Studio)

Referencia estética: Lynch, Gaspar Noé, *OK Computer* de Radiohead, estética Nothing (transparencia técnica, tipografía dot-matrix/mono, un solo acento). Resultado buscado: **cinematográfico, de alto contraste, contenido — no genérico "creative dark mode"**. Tiene que verse profesional para clientes, con un toque de inquietud controlada, no ruidoso.

**Paleta**
| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#0A0A0B` | fondo base (negro casi puro, no OLED-crush) |
| `--fg` | `#F2F0EA` | texto principal (pergamino/off-white, como tu firma de email) |
| `--fg-muted` | `#9A9A96` | texto secundario, metadatos |
| `--accent` | `#E8402C` | un solo acento rojo-cine — CTAs, focus states, enlaces activos |
| `--border` | `#232323` | líneas, divisores, grid |
| Modo claro | `#F7F6F2` / `#141311` | invertido, mismo acento — real vía `prefers-color-scheme`, no cosmético |

**Tipografía**
- Display/hero: sans geométrica de alto contraste (ej. Neue Montreal / Inter Display autoalojada) — tamaños fluidos con `clamp()`
- Cuerpo: la misma familia sans, peso regular, buena legibilidad en párrafos largos de casos de estudio
- Monoespaciada de acento (ej. JetBrains Mono / Space Mono): metadatos, timecodes, labels de navegación, roles de producción — el guiño "Nothing/timecode" que separa metadata de contenido
- Escala fluida tipo Utopia: `--step--1` a `--step-5`, todo en `clamp()`, sin breakpoints de tamaño de fuente

**Espaciado y forma**
- Escala base 8px: 4/8/16/24/32/48/64/96/128
- Mucho espacio negativo, imágenes recortadas en formatos cinematográficos (2.39:1 / 21:9) para thumbnails de proyectos
- Bordes cuadrados o radio mínimo (2–4px) — nada "friendly rounded" aquí, eso es Clowder

**Textura y movimiento (con moderación)**
- Grano de película sutil vía SVG noise (opacidad ~3–4%), nunca GIF/PNG pesado
- Microinteracción tipo glitch/scanline solo en hover de elementos clave (no en scroll general)
- Transiciones lentas y deliberadas (fade/dissolve, como un corte de edición), `prefers-reduced-motion` respetado siempre

---

## 3. Sistema de diseño — Clowder (identidad propia)

Clowder necesita romper completamente con el negro cinematográfico: es café de especialidad + comida consciente, con naming juguetón (Catpuccino, Cozy Claws). Cálido, artesanal, no genérico "coffee shop brown".

**Paleta**
| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#F7F1E7` | crema/avena |
| `--fg` | `#2B2620` | carbón cálido (no negro puro) |
| `--accent-terracotta` | `#C1653B` | CTAs, precios, acentos |
| `--accent-sage` | `#6B7A5E` | detalles secundarios, badges "conscious food" |
| Modo oscuro | `#1C1410` base espresso, mismo acento terracota | cálido, no cinematográfico |

**Tipografía**
- Cuerpo: sans humanista redondeada (ej. Nunito/Poppins-like), cálida y legible
- Display/logo lockups: serif suave o display con carácter para nombres de bebidas — mantiene el toque artesanal sin sacrificar WCAG AA
- Nada de mono/timecode aquí — ese lenguaje es exclusivo del núcleo audiovisual

**Espaciado y forma**
- Radios generosos (12–20px), sombras suaves tipo "papel"
- Fotografía de producto en primer plano, grid de menú con imagen+precio+badges dietéticos (sin gluten, sin azúcar refinada, etc.)

---

## 4. Tools y Dashboard

Usan los tokens del núcleo pero en variante utilitaria: densidad de datos > mood, tablas/tarjetas, sin grano ni glitch — son para uso funcional diario tuyo, no para impresionar clientes. El dashboard lleva `<meta name="robots" content="noindex">` y persistencia 100% local (localStorage/IndexedDB), coherente con el requisito "sin backend".

---

## 5. Siguiente paso

Con esto definido, el siguiente paso es empezar a escribir código. Te pregunto por dónde arrancamos.
