WRITTEN_NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def check_written_numbers(first, last, line):
    for idx, number in enumerate(WRITTEN_NUMBERS):
        first_index = line.find(number)
        last_index = line.rfind(number)
        if first_index != -1:
            if first_index < first.get("index"):
                first["index"] = first_index
                first["number"] = idx
        if last_index != -1:
            if last_index > last.get("index"):
                last["index"] = last_index
                last["number"] = idx


def calculate_line(line):
    last = {"index": -1,
            "number": None}
    first = {"index": float('inf'),
             "number": None}
    for i in range(len(line)):
        if not first.get("number") and line[i].isdigit():
            first = {"index": i,
                     "number": int(line[i])}
        if not last.get("number") and line[-i-1].isdigit():
            last = {"index": len(line)-i-1,
                    "number": int(line[-i-1])}

    check_written_numbers(first, last, line)
    print(first.get("number")*10+last.get("number"))
    return int(first.get("number")*10+last.get("number"))


def calculate_coordinates(filename):
    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file.readlines()):
            res += calculate_line(line)
        print(res)


if __name__ == "__main__":
    calculate_coordinates("input.txt")
