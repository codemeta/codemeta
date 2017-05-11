#!/bin/bash
cd assets/files
cp ../../vita.md .
#pandoc vita.md --template cv-template.tex -f markdown-startnum -o cv.tex
pandoc vita.md --template cv-template.tex -f markdown-startnum -o cv.pdf
rm vita.md
cd
