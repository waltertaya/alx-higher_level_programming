#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all arguments."""
    import hidden_4
    
    text = dir(hidden_4)
    for i in range(len(text)):
        if text[i][0] != '__':
            print(text[i])
    