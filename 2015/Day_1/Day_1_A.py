def calculate_floor(filename):
    with open(filename, "r") as file:
        floor = 0
        line = file.readline().strip()
        for char in line:
            if char == ")":
                floor -= 1
            if char == "(":
                floor += 1
    return floor


if __name__ == "__main__":
    result = calculate_floor("input.txt")
    print(result)
