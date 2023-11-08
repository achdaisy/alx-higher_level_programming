#!/usr/bin/python3
"""wites a string to  atext file"""


def write_file(filename="", text=""):
    """appends text to a file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
