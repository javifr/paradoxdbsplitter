# Install

- clone this repo
- instalar pip ( https://pip.pypa.io/en/stable/installing/ )
- pip install pypxlib

# Use


## Split file

```python paradoxdbsplitter.py -i /your/cool.db -o ./dump/test -c "header1,header2,header3"```

- inputfile : paradobx db file
- outputfile : namespace for the splitted files
- headers : headers for the incoming db

## Get headers help

```python paradboxdbsplitter.py -i /your/cool.DB -x``
