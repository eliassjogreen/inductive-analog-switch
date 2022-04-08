import os
from math import pi
from sys import argv
from typing import Literal
from KicadModTree.KicadFileHandler import KicadFileHandler
from nodes.inductor import Inductor
from nodes.switch_inductive import SwitchInductive
from nodes.switch import (
    SwitchAlpsMatias,
    SwitchCherryMX,
    SwitchCherryMXAlpsMatias,
)
import argparse


def str2leds(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    elif v.lower() in ("both", "b"):
        return "Both"
    else:
        raise argparse.ArgumentTypeError("Boolean or both value expected.")


parser = argparse.ArgumentParser(description="Generate footprints")

parser.add_argument(
    "path",
    type=str,
    nargs="?",
    default="footprints/Button_Switch_Keyboard_Inductive.pretty",
    help="target path of the footprints",
)
parser.add_argument(
    "--leds", type=str2leds, choices=[True, False, "Both"], nargs="?", default="Both"
)
parser.add_argument(
    "--switch-types",
    type=str,
    nargs="?",
    default="Both",
)

args = parser.parse_args()


def generate(
    path: str,
    leds: bool | Literal["Both"] = "Both",
    switch_types: Literal["PCB"] | Literal["Plate"] | Literal["Both"] = "Both",
):
    switches = []

    if not os.path.isdir(path):
        os.mkdir(path)

    for led in [True, False] if leds == "Both" else [leds]:
        for switch_type in (
            ["PCB", "Plate"] if switch_types == "Both" else [switch_types]
        ):
            switches.append(
                SwitchInductive(
                    SwitchCherryMX(switch_type=switch_type),
                    Inductor(4.5, 3, pi / 4 if led else pi / 2, (0.1, 0.1)),
                    led,
                )
            )
            switches.append(
                SwitchInductive(
                    SwitchCherryMXAlpsMatias(switch_type=switch_type),
                    Inductor(4.5, 3, pi / 4 if led else pi / 2, (0.1, 0.1)),
                    led,
                )
            )

    switches.append(SwitchInductive(SwitchAlpsMatias(), Inductor(4.5, 3, pi / 2)))

    for switch in switches:
        file_handler = KicadFileHandler(switch)
        file_handler.writeFile(os.path.join(path, f"{switch.name}.kicad_mod"))


if __name__ == "__main__":
    generate(args.path, args.leds, args.switch_types)
