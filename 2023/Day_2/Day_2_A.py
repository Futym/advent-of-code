cubes = {'red': 12, 'green': 13, 'blue': 14}


def is_game_possible(sets):
    sets = sets.split(";")
    for single_set in sets:
        if not all(map(lambda item: cubes[item.strip().split()[1]] >= int(item.strip().split()[0]),
                       single_set.strip().split(","))):
            return False
    return True


def calculate_result(filename):
    with open(filename, "r") as file:
        res = 0
        for line in file:
            if is_game_possible(line.split(":")[1].strip()):
                game_id = int(line.split(":")[0][5:])
                res += game_id
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
