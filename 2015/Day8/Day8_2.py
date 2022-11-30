import numpy
import math
import os
import pathlib
import re


def readfile(filename):
    with open(filename, "r") as file:
        return file.readlines()


if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.resolve()
    instructions = readfile(os.path.join(path, "input.txt"))
    code_chars = 0
    memory_chars = 0
    for instruction in instructions:
        instruction = instruction.strip()
        code_chars -= len(instruction)
        instruction = instruction.replace('\\', "\\\\")
        instruction = instruction.replace('\"', "\\\"")
        instruction = f"\"{instruction}\""
        code_chars += len(instruction)
        print(instruction)
    print(code_chars)
