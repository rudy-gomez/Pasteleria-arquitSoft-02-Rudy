"""Genera una lámina SVG blanca para Markdown desde el HTML de Archify."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

folder = Path(__file__).resolve().parent
html = (folder / 'pasteleria-saas.html').read_text(encoding='utf-8')
svg = re.search(r'<svg\s+viewBox="0 0 1380 740".*?</svg>', html, re.S).group()
inner = svg[svg.index('>') + 1:svg.rfind('</svg>')]
variables = re.search(r'\[data-theme="light"\]\s*\{([^}]+)\}', html).group(1)
rules = re.findall(r'\.(?:c|t|a|m)-[\w-]+\s*\{[^}]+\}', html)
css = ':root {' + variables + '}\n' + '\n'.join(rules)
css += '\ntext { font-family: Arial, Helvetica, sans-serif; }'
css += '\n.semantic-sigil { fill: none; stroke: currentColor; stroke-width: 1.35; stroke-linecap: round; stroke-linejoin: round; }'
for kind in ('frontend', 'backend', 'database', 'external'):
    css += f'\n.semantic-sigil-{kind} {{ color: var(--{kind}-stroke); }}'
output = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1420" height="840" viewBox="0 0 1420 840" role="img" aria-labelledby="sheet-title sheet-desc">
<title id="sheet-title">Arquitectura del SaaS de gestión de pastelerías</title>
<desc id="sheet-desc">Actores, presentación, lógica de negocio y datos. Los seis módulos acceden a Redis y PgBouncer; Reportes consulta directamente la réplica de lectura.</desc>
<style>{css}</style>
<rect width="1420" height="840" fill="#ffffff"/>
<rect x="1" y="1" width="1418" height="838" rx="18" fill="#ffffff" stroke="#d9e2ec" stroke-width="2"/>
<rect x="25" y="25" width="5" height="28" rx="2.5" fill="#0891b2"/>
<text x="43" y="43" font-size="21" font-weight="700" fill="#0f172a">SaaS de gestión de pastelerías</text>
<text x="1394" y="41" text-anchor="end" font-size="11" letter-spacing="1.2" fill="#64748b">ARQUITECTURA DEL SISTEMA</text>
<path d="M 25 66 H 1395" stroke="#e2e8f0"/>
<g transform="translate(20 80)">{inner}</g>
</svg>'''
ET.fromstring(output)
(folder / 'pasteleria-saas-blanco.svg').write_text(output, encoding='utf-8')
print('SVG generado y XML verificado.')
