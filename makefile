run: compile

compile:
	python test.py

build: remove bdist twineupload
bdist:
	python -m build

twineupload:
	python -m twine upload -r pypi dist/*

remove:
	@echo Remove Dist
	@rd /s /q test