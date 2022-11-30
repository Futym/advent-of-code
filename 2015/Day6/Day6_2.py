import numpy
import math
import os
import pathlib

def readfile(filename):
    with open(filename, "r") as file:
        return file.readlines()


if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.resolve()
    instructions = readfile(os.path.join(path, "input.txt")) 
    roof = numpy.zeros((1000, 1000))
    for instruction in instructions:
        splitted_instruction = instruction.split(" ")
        type_of_instruction = splitted_instruction[0]
        if (type_of_instruction == "turn"):
            for i in range(int(splitted_instruction[2].split(",")[0]), int(splitted_instruction[4].split(",")[0])+1):
                for j in range(int(splitted_instruction[2].split(",")[1]), int(splitted_instruction[4].split(",")[1])+1):
                    if splitted_instruction[1] == "off":
                        roof[i][j] = max(0, roof[i,j] -1)
                    else:
                        roof[i][j] += 1
        else:
            for i in range(int(splitted_instruction[1].split(",")[0]), int(splitted_instruction[3].split(",")[0])+1):
                for j in range(int(splitted_instruction[1].split(",")[1]), int(splitted_instruction[3].split(",")[1])+1):
                    roof[i][j] += 2
    print(roof)
    print(roof.sum())
