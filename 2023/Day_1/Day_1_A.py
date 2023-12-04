def calculate_line(line):
    last = None
    first = None
    for i in range(len(line)):
        if not first and line[i].isdigit():
            first = line[i]
        if not last and line[-i-1].isdigit():
            last = line[-i-1]
        if last and first:
            print(first+last)
            return int(first + last)


def calculate_coordinates(filename):
    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file.readlines()):
            res += calculate_line(line)
        print(res)


if __name__ == "__main__":
    calculate_coordinates("input.txt")
