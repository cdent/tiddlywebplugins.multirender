
# Simple Makefile for some common tasks. This will get 
# fleshed out with time to make things easier on developer
# and tester types.
.PHONY: test dist upload

clean:
	find . -name "*.pyc" |xargs rm || true
	rm -r dist || true
	rm -r build || true

test: 
	py.test -x test

dist: test
	python setup.py sdist

upload: clean pypi

pypi:
	python setup.py sdist upload
