def count_winning_options(time, distance):
    for i in range(time):
        if i * (time - i) > distance:
            return time - 2 * i + 1


def calculate_result(filename):
    with open(filename, "r") as file:
        time = int(file.readline().split(":")[1].replace(" ", ""))
        distance = int(file.readline().split(":")[1].replace(" ", ""))
        return count_winning_options(time, distance)


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
