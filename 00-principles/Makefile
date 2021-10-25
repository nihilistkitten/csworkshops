all: outline.pdf

outline.pdf: outline.md *-fib-*.py
	pandoc --filter pandoc-include-code outline.md -o outline.pdf


.PHONY: clean
clean:
	-rm -f outline.pdf
