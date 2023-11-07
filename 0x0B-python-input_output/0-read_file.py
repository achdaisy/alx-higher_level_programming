#!/usr/bin/python3
"""read a text file."""


def read_file(filename=""):
    """prints the read file content to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
