import argparse
from json import load
from re import match

parser = argparse.ArgumentParser(
    description="Get KiCad package metadata variables")

parser.add_argument(
    "metadata",
    type=str,
    nargs="?",
    default="metadata.json",
    help="the metadata json file",
)
parser.add_argument("selector", type=str, help="json selector")
parser.add_argument(
    "--replace",
    type=str,
    nargs=2,
    help="replaces the first string with the second in the value",
)

args = parser.parse_args()

if __name__ == "__main__":
  with open(args.metadata) as file:
    item = load(file)

    selector = []
    for part in args.selector.split("."):
      indexed = match("(.+)\[(\d+)\]\Z", part)

      if indexed != None:
        selector.append(indexed[1])
        selector.append(int(indexed[2]))
      else:
        selector.append(part)

    for key in selector:
      item = item[key]

    if args.replace != None:
      item = item.replace(args.replace[0], args.replace.pop())

    print(item, end="")
