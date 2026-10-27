#!/usr/bin/env python3
"""Build a release ZIP from an explicit public file list."""
from pathlib import Path
import hashlib
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(ROOT / "build-theme.py")], check=True)
paths = [
    ".gitattributes", ".gitignore",
    "README.md", "README.zh-CN.md", "NOTICE.txt", "LICENSING.md", "CHANGELOG.md",
    "build-theme.py", "package-theme.py", "build-manifest.json",
    "RELEASE_VERSION", "RELEASE_NOTES.md",
    "dist/nebula-github.css", "dist/nebula-github.user.css",
    "src/interface.css", "src/palettes.json", "src/geometry.css",
    "src/geometry-left.svg", "src/geometry-right.svg",
    "fonts/Sora-Variable.ttf", "fonts/Oxanium-Variable.ttf", "fonts/JetBrainsMono-Variable.ttf",
    "fonts/sora-latin-wght-400-700.woff2", "fonts/oxanium-latin-wght-400-700.woff2",
    "fonts/jetbrains-mono-latin-wght-400-700.woff2",
    "fonts/LICENSE-Sora.txt", "fonts/LICENSE-Oxanium.txt", "fonts/LICENSE-JetBrains-Mono.txt",
    "fonts/ttf-sources.json", "fonts/woff2-sources.json",
    "preview/preview-template.html", "preview/dashboard-template.html", "preview/search-template.html",
    "preview/nebula-github-preview.html", "preview/nebula-github-dashboard-preview.html",
    "preview/nebula-github-search-preview.html",
    "preview/nebula-github-geometry-light.png", "preview/nebula-github-geometry-dark.png",
    "preview/nebula-github-dashboard-light.png", "preview/nebula-github-dashboard-dark.png",
    "preview/nebula-github-search-light.png", "preview/nebula-github-search-dark.png",
]
paths = sorted(paths)
missing = [p for p in paths if not (ROOT / p).is_file()]
if missing:
    raise SystemExit("Missing release files: " + ", ".join(missing))
checksums = "".join(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() + "  " + p + "\n"
                    for p in paths)
(ROOT / "SHA256SUMS").write_text(checksums, encoding="utf-8")
paths.append("SHA256SUMS")
out_dir = ROOT / "release"
out_dir.mkdir(exist_ok=True)
target = out_dir / "nebula-github-1.2.1.zip"
with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for p in paths:
        archive.write(ROOT / p, "github-nebula-theme/" + p)
with zipfile.ZipFile(target) as archive:
    bad = archive.testzip()
    if bad:
        raise SystemExit("ZIP checksum failure: " + bad)
print(f"{target.name}: {target.stat().st_size:,} bytes, {len(paths)} files")

