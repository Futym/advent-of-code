def calculate_next_elem(sequence):
    if all(map(lambda x: x == 0, sequence)):
        return 0
    else:
        new_sequence = []
        for i in range(len(sequence)-1):
            new_sequence.append(sequence[i+1] - sequence[i])
        return sequence[0] - calculate_next_elem(new_sequence)


def calculate_result(filename):
    with open(filename, "r") as file:
        res = 0
        for line in file:
            sequence = [int(x) for x in line.strip().split()]
            res += calculate_next_elem(sequence)
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
