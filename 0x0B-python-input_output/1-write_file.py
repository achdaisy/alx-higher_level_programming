#!/usr/bin/python3
"""wites a string to  atext file"""


def write_file(filename="", text=""):
    """writes to  afile."""
    with open(filename, 'w') as file:
        return file.write(text)
