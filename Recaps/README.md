# 0x0B. Python - Input/Output

## Reading and Writing Files
- open() returns a file object, and is most commonly used with two positional arguments and one keyword: `open(filename, mode, encoding=None)`
```
>>> f = open('workfile', 'w', encoding="utf-8")
```
- Modes: 
	1. w - write
	2. r - read
	3. a - append
	4. r+ - read and write
	N/B: r will be assumed if its ommited.
	4. b - opens the file in binary mode
	5. rb+
	
	
- Example
```
>>> with open('workfile', encoding="utf-8") as f:
...    	read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

### Methods of File Objects
1. f.read()
2. f.readline()    reads a single line from the file.
3. f.write("contents to add")
4. f.tell() returns an integer giving the file object's current position in the file represented
5. f.seek(offset, whence)   To change the file object position

## Saving structured data with json 
- Serializing - Using json standard module that can take Python data hierarchies, and convert them to strings representations.
- Reconstructing the data from the string representation is called deserializing.
- Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.
- If you have an object x, you can view its JSON string representation with a simple line of code:
```
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

- Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:
```
json.dump(x, f)
```
- To decode the object again, if f is a binary file or text file object which has been opened for reading:
```
x = json.load(f)
```

```
import json
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
```


