.PHONY: default
default: beamerthemeseas.virginia.edu.sty beamerthemeseas.virginia.edu.pdf

minted:
	if ! [ -d $@ ]; then mkdir --parents $@; fi

beamerthemeseas.virginia.edu.sty:
beamerthemeseas.virginia.edu.pdf: beamercolorthemewahoo.sty beamerthemeseas.virginia.edu.sty example.pdf | minted

example.pdf: beamerthemeseas.virginia.edu.sty

include $(shell git rev-parse --show-toplevel)/Makefile.mk
