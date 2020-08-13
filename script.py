import os
import argparse

parser = argparse.ArgumentParser(
    description="Cleans up directories and puts files into according folders."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of where you want to clean"
)

args = parser.parse_args()
path = args.path

print(f"Clearning up directory {path}")