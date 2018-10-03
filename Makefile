SHELL:=/bin/sh 

all: run_test

run_test:
	@python -m unittest discover -s algorithms