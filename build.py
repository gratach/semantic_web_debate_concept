#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen
p = Path(__file__).resolve().parent
bilder = p / "images"
pdfs = p /"images_pdf"
if not pdfs.is_dir():
	pdfs.mkdir()
for x in bilder.iterdir():
	if x.name.endswith(".svg"):
		Popen(["inkscape", "-o", str(pdfs / (x.name[:-4] + ".pdf")), str(x)]).wait()
