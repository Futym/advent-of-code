import itertools
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
    cities = {instr.strip().split()[0] for instr in instructions} | {
        instr.strip().split()[2] for instr in instructions}
    cities = list(cities)
    distances_grid = numpy.zeros((len(cities), len(cities)))
    for i, instr in enumerate(instructions):
        distances_grid[cities.index(instr.strip().split()[0]), cities.index(
            instr.strip().split()[2])] = int(instr.strip().split()[4])
        distances_grid[cities.index(instr.strip().split()[2]), cities.index(
            instr.strip().split()[0])] = int(instr.strip().split()[4])

    min_dist = -1
    for subset in itertools.permutations(cities, len(cities)):
        temp_dist = 0
        for i in range(len(subset)-1):
            temp_dist += distances_grid[cities.index(
                subset[i]), cities.index(subset[i+1])]
        if (min_dist > temp_dist or min_dist == -1):
            min_dist = temp_dist
    print(cities)
    print(distances_grid)
    print(min_dist)
