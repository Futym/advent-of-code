def calculate_scratch(line):
    winning_numbers, your_numbers = line.strip().split(":")[1].strip().split("|")
    winning_numbers = winning_numbers.strip().split()
    your_numbers = your_numbers.strip().split()
    win_count = len([winning_number for winning_number in winning_numbers if winning_number in your_numbers])
    if win_count != 0:
        return 1 << (win_count-1)
    return 0


def calculate_coordinates(filename):
    with open(filename, "r") as file:
        res = 0
        for line in file:
            res += calculate_scratch(line)
        return res


if __name__ == "__main__":
    result = calculate_coordinates("input.txt")
    print(result)
