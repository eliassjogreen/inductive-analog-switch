import argparse
import json
import os
import hashlib
from zipfile import ZipFile

parser = argparse.ArgumentParser(description="Package the KiCad package")

parser.add_argument(
    "metadata",
    type=str,
    nargs="?",
    default="metadata.json",
    help="the metadata json file",
)
parser.add_argument(
    "path",
    type=str,
    nargs="?",
    default="output",
    help="target path of the package",
)
parser.add_argument(
    "content",
    type=str,
    nargs="*",
    default=["footprints/", "resources/", "symbols/", "metadata.json"],
    help="the content of the packaged archive",
)

args = parser.parse_args()

if __name__ == "__main__":
  with open(args.metadata, "r+") as metadata_file:
    metadata = json.load(metadata_file)

    name = metadata["name"].replace(" ", "_")
    version = metadata["versions"][0]["version"]
    github = metadata["resources"]["github"]

    archive_file = f"{name}-{version}.zip"
    archive_path = os.path.join(args.path, archive_file)
    download_url = f"{github}/releases/download/{version}/{archive_file}"

    if not os.path.isdir(args.path):
      os.mkdir(args.path)

    install_size = 0

    # Write archive
    with ZipFile(archive_path, "w") as archive:
      for entry in args.content:
        install_size += os.path.getsize(entry)

        if os.path.isdir(entry):
          for root, dirs, files in os.walk(entry):
            for file in files:
              archive.write(os.path.join(root, file))
        elif os.path.isfile(entry):
          archive.write(entry)

    # Write metadata
    download_sha256 = hashlib.sha256()
    with open(archive_path, "rb") as archive:
      for byte_block in iter(lambda: archive.read(4096), b""):
        download_sha256.update(byte_block)
      download_sha256 = download_sha256.hexdigest()

    download_size = os.path.getsize(archive_path)

    metadata["versions"][0]["download_sha256"] = download_sha256
    metadata["versions"][0]["download_size"] = download_size
    metadata["versions"][0]["install_size"] = install_size

    metadata_file.seek(0)
    metadata_file.truncate()
    json.dump(metadata, metadata_file, ensure_ascii=False, indent=2)
