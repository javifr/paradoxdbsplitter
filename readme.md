# Install

- clone this repo
- cd to it
- install pip ( https://pip.pypa.io/en/stable/installing/ )
- install pypxlib ```pip install pypxlib```

# Use

## Get a row of your paradox db in order to retrieve headers

```python paradboxdbsplitter.py -i /your/cool.DB -x```

## Split file

```python paradoxdbsplitter.py -i /your/cool.db -o ./dump/test -c "header1,header2,header3"```

- (h) help
- (i) inputfile : paradobx db file
- (o) outputfile : namespace for the splitted files
- (c) headers : headers for the incoming db
- (x) headers help
