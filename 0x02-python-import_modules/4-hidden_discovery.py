#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names hidden in the compiled module hidden_4.pyc."""
    import hidden_4
    
    text = dir(hidden_4)
    for i in range(0, len(text)):
        if text[i][0] != '_':
            print(text[i])
