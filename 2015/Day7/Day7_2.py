import numpy
import math
import os
import pathlib


def readfile(filename):
    with open(filename, "r") as file:
        return file.readlines()


class Instruction:
    def __init__(self, instr):
        self.instr = instr
        self.arg1: str = None
        self.arg2: str = None
        self.shift = None
        self.done = False
        if (instr[0] == "NOT"):
            self.gate = lambda x: ~x
            self.arg1 = instr[1]
        elif (instr[1] == "AND"):
            self.gate = lambda x, y: x & y
            self.arg1 = instr[0]
            self.arg2 = instr[2]
        elif (instr[1] == "OR"):
            self.gate = lambda x, y: x | y
            self.arg1 = instr[0]
            self.arg2 = instr[2]
        elif (instr[1] == "RSHIFT"):
            self.shift = int(instr[2])
            self.gate = lambda x: x >> self.shift
            self.arg1 = instr[0]
        elif (instr[1] == "LSHIFT"):
            self.shift = int(instr[2])
            self.gate = lambda x: x << self.shift
            self.arg1 = instr[0]
        else:
            self.gate = None
            self.arg1 = instr[0]

        self.target = instr[-1]

    def try_execute(self, dict):
        is_arg1 = (self.arg1.isnumeric() or dict[self.arg1] != None)
        is_arg2 = (self.arg2 == None or self.arg2.isnumeric()
                   or dict[self.arg2] != None)
        if is_arg1 and is_arg2:
            if (self.instr[0] == "NOT"):
                dict[self.target] = self.gate(dict[self.arg1])
                self.done = True
            elif (self.instr[1] == "AND" or self.instr[1] == "OR"):
                dict[self.target] = self.gate(int(self.arg1) if self.arg1.isnumeric() else dict[self.arg1], int(
                    self.arg2) if self.arg2.isnumeric() else dict[self.arg2])
                self.done = True

            elif (self.instr[1] == "LSHIFT" or self.instr[1] == "RSHIFT"):
                dict[self.target] = self.gate(dict[self.arg1])
                self.done = True
            else:
                dict[self.target] = int(
                    self.arg1) if self.arg1.isnumeric() else dict[self.arg1]
                self.done = True


if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.resolve()
    instructions = readfile(os.path.join(path, "input.txt"))
    iter = 0
    instructions.sort()
    instructions_splitted = [instruction.split()
                             for instruction in instructions]
    dict = {wire[-1]: None for wire in instructions_splitted}
    instructions_obj_list = [Instruction(
        instr) for instr in instructions_splitted]
    while (instructions_obj_list != []):
        for i, instr in enumerate(instructions_obj_list):
            instr.try_execute(dict)

        instructions_obj_list = [
            elem for elem in instructions_obj_list if elem.done == False]

    a = (dict["a"])
    dict = {wire[-1]: None for wire in instructions_splitted}
    dict["b"] = a

    instructions_obj_list = [Instruction(
        instr) for instr in instructions_splitted if instr[-1] != "b"]

    while (instructions_obj_list != []):
        for i, instr in enumerate(instructions_obj_list):
            instr.try_execute(dict)

        instructions_obj_list = [
            elem for elem in instructions_obj_list if elem.done == False]
    
    print(dict["a"])
