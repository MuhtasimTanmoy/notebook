# Parser
Used this to parse large database dump to extract relevant information.


- Extracts `data` from this pattern `<url> data </url>` and saves it.

```py
from re import compile, findall

def parse(fileName):
    exp = compile(r"<url>(.*?)</url>")
    infile = open(fileName, 'r', encoding="utf-8")
    text = infile.read().lower()  # Notice, no .split()
    text_exclusive = ''.join([''.join(block + "\n") for block in findall(exp, text)])
    with open('output','w',encoding = 'utf-8') as f:
        f.write(text_exclusive)

parse("testData")
```

- Converts list of url into link in markdown file for visualization.

```py
def format(pathName):
    file1 = open(pathName, 'r')
    Lines = file1.readlines()
    output = ''.join([''.join("![]({})\n".format(line.strip())) for line in Lines ])
    with open('output','w',encoding = 'utf-8') as f:
        f.write(output)

format("Data.txt")
```

- Structures a tree from folder of markdown files to use as summary

```py
import os
from os.path import basename

def list_files(startpath):
    currentBasePath = ""
    for path, subdirs, files in os.walk(startpath):
        for name in files:
            filePath = path.replace(startpath, '')
            if filePath.startswith("/.git"):
                continue
            level = path.replace(startpath, '').count(os.sep)
            # indent = ' ' * 4 * (level)
            basePath = os.path.basename(path)
            if basePath.startswith("Screen"):
                continue
            if currentBasePath != basePath:
                currentBasePath = basePath
                print('- ### {}'.format(os.path.basename(path)))
            # subindent = ' ' * 4 * (level + 1)
            pathName = os.path.basename(path).replace(" ", "%20")
            fileName = name.replace(" ", "%20")
            print('{}- [{}](./{}/{})'.format("    ", name[:-3], pathName, fileName))

list_files("Notebook")
```