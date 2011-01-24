# define TEX as pdflatex
TEX=pdflatex

.PHONY: default
default: paper.pdf

paper.pdf: paper.tex references.bib
	cp ../uva-seas-thesis.sty .
	$(TEX) paper.tex
	bibtex paper
	$(TEX) paper.tex
	$(TEX) paper.tex
	$(RM) uva-seas-thesis.sty

.PHONY: clean
clean:
	$(RM) *.aux *.bbl *.blg *.log *.lof *.lot *.out *.toc uva-seas-thesis.sty
	find . -name "*.aux" -print0 | xargs -0 $(RM)

# targets
.PHONY: draft
draft: paper.tex references.bib
	./change-options.py --class draft,openany,twoside --package hidefront
	$(MAKE)

.PHONY: print
print: paper.tex references.bib
	./change-options.py --class final,oneside,openany --package print
	$(MAKE)

.PHONY: electronic
electronic: paper.tex references.bib
	./change-options.py --class final,openany --package electronic
	$(MAKE)

.PHONY: compliant
compliant: paper.tex references.bib
	./change-options.py --class final,oneside,openany --package bind,compliant
	$(MAKE)

