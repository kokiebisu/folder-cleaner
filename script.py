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

# gets the list of all the files and folders inside of that directory
content = os.listdir(path)

# creates a relative path from the path to the file and the document name
path_content = [os.path.join(path, doc) for doc in content]

# filters out only the files and assigns it to the docs variable
docs = [doc for doc in path_content if os.path.isfile(doc)]
folders = [folder for folder in path_content if os.path.isdir(doc)]

moved = 0
created_folder = []


print(f"Clearning up directory {docs}")