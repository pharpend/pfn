all: setup build clean

setup:
	mkdir -p .build
	cp -rv pfs.bib pfs.tex chapters code images listings .build

build:
	cd .build && \
	  latexmk -pdf pfs.tex && \
	  cp pfs.pdf ..

clean:
	rm -rf .build
