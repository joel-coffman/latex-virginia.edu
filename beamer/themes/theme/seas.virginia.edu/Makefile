.PHONY: default
default: beamerthemeseas.virginia.edu.sty example.pdf beamerthemeseas.virginia.edu.pdf

minted:
	if ! [ -d $@ ]; then mkdir --parents $@; fi

beamerthemeseas.virginia.edu.sty: | beamercolorthemewahoo.sty
beamerthemeseas.virginia.edu.pdf: beamerthemeseas.virginia.edu.sty example.pdf | minted

example.pdf: beamerthemeseas.virginia.edu.sty

.PHONY: minted
minted:
	if ! [ -d $@ ]; then mkdir --parents $@; fi

include $(shell git rev-parse --show-toplevel)/Makefile.mk

# fall-back for Beamer themes
beamercolorthemewahoo.sty:
	$(MAKE) --directory=../../color/wahoo $@
