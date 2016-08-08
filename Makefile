all: setup build clean

setup:
	mkdir -p .build
	cp -rv pfs.bib pfs.tex chapters code images listings tex/latex-solarized/*.sty .build

build:
	cd .build && \
	  latexmk -pdf pfs.tex && \
	  cp pfs.pdf ..

clean:
	rm -rf .build
