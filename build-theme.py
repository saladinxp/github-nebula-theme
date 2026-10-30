#!/usr/bin/env python3
"""Build an offline, CSS-only GitHub UserCSS from Nebula source colors."""
from pathlib import Path
import base64
import hashlib
import json
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
VERSION = (ROOT / 'RELEASE_VERSION').read_text(encoding='ascii').strip()
if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', VERSION):
    raise SystemExit('Invalid RELEASE_VERSION')
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
palettes = json.loads((ROOT / 'src/palettes.json').read_text(encoding='utf-8'))

ALIASES = {
    'bgColor-default':'surface', 'bgColor-muted':'muted', 'bgColor-inset':'inset',
    'bgColor-emphasis':'emphasis', 'bgColor-inverse':'inverse', 'bgColor-disabled':'control-disabled',
    'bgColor-accent-emphasis':'accent-solid', 'bgColor-accent-muted':'accent-muted',
    'fgColor-default':'text', 'fgColor-muted':'subtle', 'fgColor-disabled':'disabled',
    'fgColor-accent':'accent', 'fgColor-link':'accent', 'fgColor-onInverse':'on-inverse',
    'borderColor-default':'border', 'borderColor-muted':'border-muted', 'borderColor-emphasis':'border-strong',
    'borderColor-accent-emphasis':'accent-solid', 'borderColor-accent-muted':'selected',
    'borderColor-disabled':'border-muted',
    'control-bgColor-rest':'control', 'control-bgColor-hover':'control-hover',
    'control-bgColor-active':'control-active', 'control-bgColor-selected':'selected',
    'control-bgColor-disabled':'control-disabled', 'control-fgColor-rest':'text',
    'control-fgColor-placeholder':'subtle', 'control-fgColor-disabled':'disabled',
    'control-borderColor-rest':'border', 'control-borderColor-emphasis':'border-strong',
    'control-iconColor-rest':'subtle',
    'control-transparent-bgColor-hover':'hover', 'control-transparent-bgColor-active':'selected',
    'control-transparent-bgColor-selected':'selected',
    'control-checked-bgColor-rest':'accent-solid', 'control-checked-bgColor-hover':'primary-hover',
    'control-checked-bgColor-active':'primary-active',
    'button-default-bgColor-rest':'control', 'button-default-bgColor-hover':'control-hover',
    'button-default-bgColor-active':'control-active', 'button-default-bgColor-selected':'selected',
    'button-default-fgColor-rest':'text', 'button-default-borderColor-rest':'border',
    'button-default-borderColor-hover':'border-strong',
    'button-invisible-fgColor-rest':'text', 'button-invisible-fgColor-hover':'strong',
    'button-invisible-bgColor-hover':'hover', 'button-invisible-bgColor-active':'selected',
    'button-outline-fgColor-rest':'accent', 'button-outline-bgColor-hover':'accent-solid',
    'button-outline-bgColor-active':'primary-active',
    'button-primary-bgColor-rest':'primary', 'button-primary-bgColor-hover':'primary-hover',
    'button-primary-bgColor-active':'primary-active', 'button-primary-bgColor-disabled':'primary-disabled',
    'button-primary-borderColor-rest':'primary', 'button-primary-borderColor-hover':'primary-hover',
    'button-primary-borderColor-active':'primary-active', 'button-primary-borderColor-disabled':'primary-disabled',
    'buttonCounter-outline-fgColor-rest':'accent', 'buttonCounter-outline-bgColor-rest':'accent-muted',
    'overlay-bgColor':'overlay', 'overlay-borderColor':'border', 'overlay-backdrop-bgColor':'backdrop',
    'header-bgColor':'nav', 'header-fgColor-default':'text', 'header-fgColor-logo':'accent',
    'header-borderColor-divider':'border', 'headerSearch-bgColor':'inset', 'headerSearch-borderColor':'border',
    'underlineNav-borderColor-active':'accent', 'underlineNav-borderColor-hover':'border',
    'underlineNav-iconColor-rest':'subtle', 'focus-outline-color':'accent', 'focus-outlineColor':'accent',
    # Compatibility aliases for still-deployed GitHub CSS components.
    'color-canvas-default':'surface', 'color-canvas-subtle':'muted', 'color-canvas-inset':'inset',
    'color-canvas-overlay':'overlay', 'color-fg-default':'text', 'color-fg-muted':'subtle',
    'color-fg-subtle':'subtle', 'color-accent-fg':'accent', 'color-accent-emphasis':'accent-solid',
    'color-accent-muted':'selected', 'color-accent-subtle':'accent-muted',
    'color-border-default':'border', 'color-border-muted':'border-muted',
    'color-btn-text':'text', 'color-btn-bg':'control', 'color-btn-border':'border',
    'color-btn-hover-bg':'control-hover', 'color-btn-hover-border':'border-strong',
    'color-btn-active-bg':'control-active',
    'color-btn-primary-bg':'primary', 'color-btn-primary-hover-bg':'primary-hover',
    'color-btn-primary-selected-bg':'primary-active', 'color-btn-primary-border':'primary',
    'color-btn-primary-hover-border':'primary-hover', 'color-btn-primary-disabled-bg':'primary-disabled',
    'color-header-bg':'nav', 'color-header-text':'text', 'color-header-logo':'accent',
    'color-input-bg':'surface', 'color-input-border':'border', 'color-input-contrast-bg':'inset',
    'color-neutral-subtle':'hover', 'color-prettylights-syntax-comment':'comment',
}

def palette_block(selectors, mode):
    values=palettes[mode]
    lines=[f'{selectors} {{']
    lines += [f'  --nb-{k}: {v} !important;' for k,v in values.items()]
    lines += [f'  --{k}: var(--nb-{v}) !important;' for k,v in ALIASES.items()]
    lines += [
        '  --button-primary-fgColor-rest: #ffffff !important;',
        '  --button-primary-fgColor-disabled: #ffffffcc !important;',
        '  --button-primary-iconColor-rest: #ffffffed !important;',
        '  --color-btn-primary-text: #ffffff !important;',
        '  --color-btn-primary-disabled-text: #ffffffcc !important;',
        '  --color-btn-outline-text: var(--nb-accent) !important;',
        '  --shadow-resting-xsmall: 0 1px 2px var(--nb-shadow) !important;',
        '  --shadow-resting-small: 0 2px 7px var(--nb-shadow) !important;',
        '  --shadow-floating-small: 0 8px 28px var(--nb-shadow), 0 0 0 1px var(--nb-border) !important;',
        '  --shadow-floating-medium: 0 16px 48px var(--nb-shadow), 0 0 0 1px var(--nb-border) !important;',
        '  --color-shadow-small: 0 2px 7px var(--nb-shadow) !important;',
        '  --color-shadow-large: 0 16px 48px var(--nb-shadow) !important;',
        f'  color-scheme: {mode};',
        '}'
    ]
    return '\n'.join(lines)

font_sources=[('Sora','sora-latin-wght-400-700.woff2'),('Oxanium','oxanium-latin-wght-400-700.woff2'),('JetBrains Mono','jetbrains-mono-latin-wght-400-700.woff2')]
fonts=[]
for family,filename in font_sources:
    data=base64.b64encode((ROOT/'fonts'/filename).read_bytes()).decode()
    fonts.append('@font-face {\n'+f'  font-family: "{family}";\n  font-style: normal;\n  font-weight: 400 700;\n  font-display: swap;\n  src: url("data:font/woff2;base64,{data}") format("woff2");\n'+'}\n')

body='/* Uses installed local fonts with a system fallback. No remote or data font requests. */\n@media (forced-colors: none) {\n'
body+=palette_block('html, [data-color-mode="light"], [data-color-mode="auto"]','light')+'\n'
body+=palette_block('[data-color-mode="dark"], [data-color-mode="light"][data-light-theme^="dark"], [data-color-mode="auto"][data-light-theme^="dark"]','dark')+'\n'
body+=palette_block('[data-color-mode="dark"][data-dark-theme^="light"]','light')+'\n'
body+='@media (prefers-color-scheme: dark) {\n'+palette_block('html:not([data-color-mode]), [data-color-mode="auto"]','dark')+'\n'
body+=palette_block('[data-color-mode="auto"][data-dark-theme^="light"]','light')+'\n}\n'
body+=(ROOT/'src/interface.css').read_text(encoding='utf-8')+'\n'
geometry=(ROOT/'src/geometry.css').read_text(encoding='utf-8')
for side in ('left', 'right'):
    svg=(ROOT/f'src/geometry-{side}.svg').read_text(encoding='utf-8')
    geometry=geometry.replace(f'__NEBULA_GEOMETRY_{side.upper()}__',
                              'data:image/svg+xml,'+quote(svg, safe=''))
body+=geometry+'\n}\n'

meta='''/* ==UserStyle==
@name         Nebula for GitHub · 日夜双主题
@namespace    arcdex.nebula.github
@version      __NEBULA_VERSION__
@description  Blue-violet Nebula for GitHub. Choose light, dark, or follow GitHub in Stylus. Optional grid, floating geometry, local fonts and motion. CSS only.
@author       saladinxp
@homepageURL  https://github.com/saladinxp/github-nebula-theme
@supportURL   https://github.com/saladinxp/github-nebula-theme/issues
@updateURL    https://raw.githubusercontent.com/saladinxp/github-nebula-theme/main/dist/nebula-github.user.css
@preprocessor uso
@var select nebula-color-mode "配色模式 / Color mode" __NEBULA_COLOR_OPTIONS__
@var checkbox nebula-grid "细网格背景" 1
@var checkbox nebula-geometry "漂浮几何背景" 1
@var select nebula-motion "背景与顶栏动效" {"开启*":"running","关闭":"paused"}
==/UserStyle== */
'''
force_selector = ':root:root:root, :root:root:root [data-color-mode]'
color_options = {'auto:跟随 GitHub / Follow GitHub*': ':root {}'}
for mode, label in [('light', '浅色 / Light'), ('dark', '深色 / Dark')]:
    forced = palette_block(force_selector, mode)
    forced = forced.replace(f'color-scheme: {mode};', f'color-scheme: {mode} !important;')
    color_options[f'{mode}:{label}'] = forced
meta=meta.replace('__NEBULA_VERSION__', VERSION)
meta=meta.replace('__NEBULA_COLOR_OPTIONS__', json.dumps(color_options, ensure_ascii=False))
# USO substitutions retain the existing grid, geometry and motion options.
controls = ':root {\n  --nebula-grid: /*[[nebula-grid]]*/;\n  --nebula-geometry: /*[[nebula-geometry]]*/;\n  --nebula-motion: /*[[nebula-motion]]*/;\n}\n'
assert body.endswith('}\n')
user_body = controls + body[:-2] + '\n/*[[nebula-color-mode]]*/\n}\n'

usercss=meta+'\n@-moz-document url-prefix("https://github.com/") {\n'+user_body+'\n}\n'
(DIST/'nebula-github.user.css').write_text(usercss, encoding='utf-8')
(DIST/'nebula-github.css').write_text('/* Plain CSS: apply ONLY to https://github.com/ using your style manager. */\n'+body, encoding='utf-8')
for template_name, output_name in [
    ('preview-template.html', 'nebula-github-preview.html'),
    ('dashboard-template.html', 'nebula-github-dashboard-preview.html'),
    ('search-template.html', 'nebula-github-search-preview.html'),
]:
    template=ROOT/'preview'/template_name
    if template.exists():
        preview=template.read_text(encoding='utf-8').replace('__NEBULA_CSS__','\n'.join(fonts)+'\n'+body)
        (ROOT/'preview'/output_name).write_text(preview, encoding='utf-8')
manifest={'name':'Nebula for GitHub','version':VERSION,'date':'2026-10-30','scope':['https://github.com/'],'mode':'Stylus: follow GitHub (default), force light, or force dark. Plain CSS follows GitHub.','networkRequestsAdded':[],'embeddedAssets':['geometry-left.svg','geometry-right.svg'],'semanticColors':'Native GitHub status, danger, success, warning and diff colors are not overridden.','files':{p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(DIST.glob('*.css'))}}
(ROOT/'build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
for name,info in manifest['files'].items(): print(f'{name}: {info["bytes"]:,} bytes')
