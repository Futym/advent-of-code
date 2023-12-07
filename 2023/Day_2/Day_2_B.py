import numpy


def calculate_power(sets):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    sets = sets.split(";")
    for single_set in sets:
        for cube_type in single_set.strip().split(","):
            number_of_cubes, cube_colour = cube_type.strip().split()
            if cubes[cube_colour] < int(number_of_cubes):
                cubes[cube_colour] = int(number_of_cubes)
    return numpy.prod(list(cubes.values()))


def calculate_result(filename):
    with open(filename, "r") as file:
        res = 0
        for line in file:
            res += calculate_power(line.split(":")[1].strip())
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
