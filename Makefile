
help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "build - package"

all: default

default: clean dev_deps deps test lint build

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr dist/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

deps:
	pip install -U -r requirements.txt -t ./src/libs

dev_deps:
	pip install -U -r dev_requirements.txt

lint:
	pylint -r n src/main.py src/shared src/jobs tests

test:
	nosetests ./tests/* --config=.noserc

build: clean
	mkdir ./dist
	cp ./src/main.py ./dist
	cp -r ./src/resources ./dist/resources
	cd ./src && zip -x main.py -x \*libs\* -x \*resources\* -r ../dist/jobs.zip .
	cd ./src/libs && zip -r ../../dist/libs.zip .
