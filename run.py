import os
from os.path import basename

# use python3 structure.py

def list_files(startpath):
    currentBasePath = ""
    for path, subdirs, files in os.walk(startpath):
        for name in files:
            filePath = path.replace(startpath, '')
            if filePath.startswith(".git") or filePath.startswith("/.git"):
                continue
            level = path.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            basePath = os.path.basename(path)
            if basePath.startswith("screen"):
                continue
            if basePath.startswith("images"):
                continue
            if currentBasePath != basePath:
                currentBasePath = basePath
                print('{}- {}'.format(indent, os.path.basename(path)))
            if name.startswith(".DS_Store"):
                continue
            subindent = ' ' * 4 * (level + 1)
            pathName = filePath.replace(" ", "%20")
            fileName = name.replace(" ", "%20")
            print('{}- [{}](.{}/{})'.format(subindent, name[:-3], pathName, fileName))

list_files(".")