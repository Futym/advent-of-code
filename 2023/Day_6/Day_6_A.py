def count_winning_options(time, distance):
    for i in range(time):
        if i * (time - i) > distance:
            return time - 2 * i + 1


def calculate_result(filename):
    with open(filename, "r") as file:
        res = 1
        times = [int(x) for x in file.readline().split(":")[1].strip().split()]
        distances = [int(x) for x in file.readline().split(":")[1].strip().split()]
        for i in range(len(times)):
            res *= count_winning_options(times[i], distances[i])
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
