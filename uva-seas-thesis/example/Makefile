.PHONY: default
default: $(patsubst %.tex,%.pdf,$(wildcard *.tex))

TEXINPUTS := ../:${TEXINPUTS}

include $(shell git rev-parse --show-toplevel)/Makefile.mk


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
