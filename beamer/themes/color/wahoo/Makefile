.PHONY: default
default: beamercolorthemewahoo.sty beamercolorthemewahoo.pdf

beamercolorthemewahoo.sty:
beamercolorthemewahoo.pdf: beamercolorthemewahoo.sty example.pdf

example.pdf: beamercolorthemewahoo.sty

include $(shell git rev-parse --show-toplevel)/Makefile.mk
