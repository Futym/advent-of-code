import numpy as np


DIRECTIONS_TO_VEC = {"S": np.array([-1, 0]), "N": np.array([1, 0]), "E": np.array([0, -1]), "W": np.array([0, 1])}


def count_enclosed_tiles(line):
    is_inside_loop = False
    enclosed_tiles = 0
    for ch in line:
        if ch not in ["P", "W"] and is_inside_loop:
            enclosed_tiles += 1
        elif ch == "W":
            is_inside_loop = not is_inside_loop
    return enclosed_tiles


def get_next_direction(pipe, from_direction):
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


def mark_loop(lines, starting_point):
    if lines[starting_point[0]][starting_point[1]+1] in ["-", "J", "7"]:
        from_direction = "W"
    elif lines[starting_point[0]][starting_point[1]-1] in ["-", "F", "L"]:
        from_direction = "E"
    else:
        from_direction = "N"
    next_pipe = starting_point + DIRECTIONS_TO_VEC[from_direction]

    if len(lines)-1 > starting_point[0] > 0:
        if lines[starting_point[0]-1][starting_point[1]] in ["|", "7", "F"]:
            lines[starting_point[0]] = lines[starting_point[0]][:starting_point[1]] + "W" + lines[starting_point[0]][
                                                                                            starting_point[1] + 1:]
        else:
            lines[starting_point[0]] = lines[starting_point[0]][:starting_point[1]] + "P" + lines[starting_point[0]][
                                                                                        starting_point[1] + 1:]

    while not np.array_equal(next_pipe, starting_point):
        from_direction = get_next_direction(lines[next_pipe[0]][next_pipe[1]], from_direction)
        if lines[next_pipe[0]][next_pipe[1]] in ["J", "L", "|"]:
            lines[next_pipe[0]] = lines[next_pipe[0]][:next_pipe[1]] + "W" + lines[next_pipe[0]][next_pipe[1]+1:]
        else:
            lines[next_pipe[0]] = lines[next_pipe[0]][:next_pipe[1]] + "P" + lines[next_pipe[0]][next_pipe[1] + 1:]
        next_pipe += DIRECTIONS_TO_VEC[from_direction]


def calculate_result(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        starting_point = None
        for idx, line in enumerate(lines):
            if "S" in line:
                starting_point = np.array([idx, line.find("S")])
        mark_loop(lines, starting_point)
        res = 0
        for line in lines[1:-1]:
            res += count_enclosed_tiles(line)
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
