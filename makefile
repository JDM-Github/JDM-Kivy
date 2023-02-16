build: bdist twineupload

bdist:
	python -m build

twineupload:
	python -m twine upload -r pypi dist/*

