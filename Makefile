name := $(shell (jq -r ".name" < ./metadata.json) | tr -s " " "_")
version := $(shell jq -r ".versions[0].version" < ./metadata.json)
github := $(shell jq -r ".resources.github" < ./metadata.json)
content := ./footprints ./resources ./symbols ./metadata.json
directory := ./release/
package_name := $(name)-${version}.zip
package := $(directory)$(package_name)
metadata := $(directory)metadata.json
download_url := $(github)/releases/download/$(version)/$(package_name)

all: release

release: footprints
	mkdir release
	zip -r $(package) $(content)
	(jq ".versions[0].download_sha256 = \"$$(shasum --algorithm 256 $(package) | xargs | cut -d" " -f1)\" | .versions[0].download_size = $$(wc -c < $(package)) | .versions[0].install_size = $$(unzip -l $(package) | tail -1 | xargs | cut -d" " -f1) | .versions[0].download_url = \"$(download_url)\"" < ./metadata.json) > $(metadata)

footprints:
	mkdir footprints
	python scripts/generator.py

clean:
	rm -rf "$(directory)"
