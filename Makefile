all: release

release: footprints
	zip -r ./release.zip ./footprints ./resources ./symbols ./metadata.json

footprints:
	mkdir footprints
	python scripts/generator.py
