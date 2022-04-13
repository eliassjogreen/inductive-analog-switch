all: package

package: footprints
	python scripts/package.py

footprints:
	python scripts/footprints.py

clean:
	rm -rf output/

fmt:
	python -m yapf --style="{based_on_style: pep8, indent_width: 2}" --in-place --recursive scripts/
