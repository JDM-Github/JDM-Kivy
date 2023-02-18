run: compile

compile:
	python test.py

build: remove bdist twineupload remove_egg
bdist:
	python -m build

twineupload:
	python -m twine upload -r pypi dist/*

remove:
	@echo Remove dist
	@rd /s /q dist

remove_egg:
	@echo Remove Egg
	@rd /s /q "src/JDM_kivy.egg-info"
