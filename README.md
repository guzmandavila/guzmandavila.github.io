# ronaldguzman — sitio personal

Sitio personal de Ronald Guzmán Dávila: portafolio audiovisual + landings
de Periplo Studio y Clowder + dashboard personal + utilidades. HTML5/CSS3/JS
vanilla, sin frameworks, alojado en GitHub Pages.

## Estructura del repo

```
/
├── index.html          Hub principal = portafolio (reel, experiencia, casos de estudio, contacto)
├── /work/<slug>/        Páginas individuales de cada caso de estudio
├── /periplo/             Landing Periplo Studio (identidad = núcleo cinematográfico)
├── /clowder/             Landing Clowder (identidad propia, cálida)
├── /tools/               Utilidades: calculadora de tarifas, checklist de entrega
├── /dashboard/           Tracker personal — noindex, persistencia 100% local
├── /assets/
│   ├── /css/  tokens.css (design tokens compartidos) · base.css (reset + tipografía + a11y) · utilities.css (layout)
│   ├── /js/   módulos ES nativos, uno por feature
│   ├── /img/  imágenes e iconos (WebP/AVIF cuando aplique)
│   └── /fonts/
├── manifest.json / favicon.svg / favicon.ico  → PWA
├── sitemap.xml / robots.txt                   → SEO técnico
└── .github/workflows/  deploy.yml (GitHub Pages) · lighthouse-ci.yml
```

## Sistema de diseño

Documentado en detalle en `arquitectura-sistema-diseno.md` (entregado aparte). Resumen:

- **Núcleo (hub / portfolio / Periplo)**: cinematográfico, alto contraste, fondo
  casi negro `#0a0a0b`, texto pergamino `#f2f0ea`, un solo acento rojo-cine
  `#e8402c`. Sans geométrica + monoespaciada para metadatos/timecodes. Definido
  en `assets/css/tokens.css`.
- **Clowder**: identidad separada y cálida (crema/terracota/sage), definida en
  `clowder/css/theme.css`, que sobreescribe los tokens de color/tipografía/radio
  del núcleo sin tocar el layout compartido.
- Cada módulo carga: `tokens.css` → `base.css` → `theme.css` propio (si aplica) → `utilities.css`.

## Desarrollo local

No hay build step: es HTML/CSS/JS estático. Basta un servidor estático simple:

```bash
python3 -m http.server 8000
# o
npx serve .
```

Abrir `http://localhost:8000`.

## Regenerar los iconos

```bash
cd assets/img/icons
pip install Pillow --break-system-packages
python3 generate_icons.py
```

## CI/CD

- `deploy.yml`: publica a GitHub Pages en cada push a `main` (requiere
  habilitar Pages → Source: GitHub Actions en la configuración del repo).
- `lighthouse-ci.yml`: corre Lighthouse contra `/`, `/periplo/`, `/clowder/`
  y `/tools/` en cada push/PR a `main`, con umbrales mínimos definidos en
  `.lighthouserc.json` (performance/SEO/best-practices ≥ 0.9, accesibilidad ≥ 0.95).

## GitHub Pages

Repo de usuario: `guzmandavila.github.io` (se publica directo en la raíz del
dominio, por eso el código usa rutas absolutas como `/assets/...`). En
Settings → Pages, Source = **GitHub Actions**. El workflow `deploy.yml` hace
el resto en cada push a `main`.

## Pendiente antes de producción

- [ ] Si más adelante se compra un dominio propio, actualizar
      `sitemap.xml`, `robots.txt` y los `<meta property="og:url">` / `canonical`
      de cada página, y añadir un archivo `CNAME`.
- [ ] Autoalojar las fuentes definitivas (actualmente `tokens.css` usa stacks
      de sistema como fallback honesto).
- [ ] Construir el contenido real del hub principal (reel, casos de estudio,
      experiencia) — hoy `index.html` es un placeholder semántico y válido.
- [ ] Construir Periplo, Clowder, Tools y Dashboard como módulos completos.
- [ ] Validar cada página contra el W3C Validator y auditar consola sin errores.

## Próximo módulo a construir

Con la base lista, el siguiente paso natural es el hub principal (contenido
real del portafolio) o un módulo específico — a definir.
