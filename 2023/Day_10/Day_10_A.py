import numpy as np


DIRECTIONS_TO_VEC = {"S": np.array([-1, 0]), "N": np.array([1, 0]), "E": np.array([0, -1]), "W": np.array([0, 1])}


def get_next_from_direction(pipe, from_direction):
    match from_direction:
        case "W":
            if pipe == "J":
                return "S"
            if pipe == "7":
                return "N"
            return "W"
        case "E":
            if pipe == "L":
                return "S"
            if pipe == "F":
                return "N"
            return "E"
        case "N":
            if pipe == "L":
                return "W"
            if pipe == "J":
                return "E"
            return "N"
        case "S":
            if pipe == "F":
                return "W"
            if pipe == "7":
                return "E"
            return "S"
        case _:
            pass


def find_loop_length(lines, starting_point):

    if lines[starting_point[0]][starting_point[1]+1] in ["-", "J", "7"]:
        from_direction = "W"
    elif lines[starting_point[0]][starting_point[1]-1] in ["-", "F", "L"]:
        from_direction = "E"
    else:
        from_direction = "N"
    next_pipe = starting_point + DIRECTIONS_TO_VEC[from_direction]
    step = 0
    while not np.array_equal(next_pipe, starting_point):
        from_direction = get_next_from_direction(lines[next_pipe[0]][next_pipe[1]], from_direction)
        next_pipe += DIRECTIONS_TO_VEC[from_direction]
        step += 1
    return step


def calculate_result(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        starting_point = None
        for idx, line in enumerate(lines):
            if "S" in line:
                starting_point = np.array([idx, line.find("S")])
        loop_length = find_loop_length(lines, starting_point)
        return loop_length // 2 + loop_length % 2


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
