all: package

package: footprints
	python scripts/package.py

footprints:
	python scripts/footprints.py

clean:
	rm -rf release/
