# define TEX as pdflatex
TEX=pdflatex

.PHONY: default
default: uva-seas-thesis.tex glossary.tex references.bib
	$(TEX) uva-seas-thesis
	bibtex uva-seas-thesis
	$(TEX) uva-seas-thesis
	$(TEX) uva-seas-thesis

.PHONY: clean
clean:
	$(RM) *.aux *.bbl *.blg *.log *.lof *.lot *.out *.toc

