.PHONY: default
default: $(patsubst %.tex,%.pdf,$(wildcard *.tex))

uva-seas-thesis.pdf: uva-seas-thesis.sty

package = \
        $(wildcard *.sty) \
        $(patsubst %.tex,%.pdf,$(wildcard *.tex)) \
        $(wildcard README)

archive = uva-seas-thesis.zip

include $(shell git rev-parse --show-toplevel)/Makefile.mk

.PHONY: distcheck
distcheck: dist
	unzip -l $(archive) | grep '$(basename $(archive))/$$'  # package directory
	unzip -l $(archive) | grep '\.sty$$'  # style file
	unzip -l $(archive) | grep '\.pdf$$'  # documentation
