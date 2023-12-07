def calculate_scratch(line):
    winning_numbers, your_numbers = line.strip().split(":")[1].strip().split("|")
    winning_numbers = winning_numbers.strip().split()
    your_numbers = your_numbers.strip().split()
    win_count = len([winning_number for winning_number in winning_numbers if winning_number in your_numbers])
    return win_count


def calculate_coordinates(filename):
    with open(filename, "r") as file:
        res = {}
        lines = file.readlines()
        cards = len(lines)
        for idx, line in enumerate(lines):
            if idx in res.keys():
                res[idx] += 1
            else:
                res[idx] = 1
            for i in range(1, min(calculate_scratch(line)+1, cards)):
                if idx+i in res.keys():
                    res[idx+i] += res[idx]
                else:
                    res[idx+i] = res[idx]
        return sum(res.values())


if __name__ == "__main__":
    result = calculate_coordinates("input.txt")
    print(result)
