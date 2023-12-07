def calculate_transformation(table, number):
    for line in table:
        if line[1] <= number < line[1] + line[2]:
            return line[0] + number - line[1]
    return number


def calculate_coordinates(filename):
    with open(filename, "r") as file:
        seeds = map(lambda x: int(x), file.readline().split(":")[1].strip().split())
        transformation_tables = []
        for line in file:
            if line == "\n":
                table = []
                transformation_tables.append(table)
                file.readline()
            else:
                table.append(list(map(lambda x: int(x), line.strip().split())))
        min_location = float("inf")
        for seed in seeds:
            number = seed
            for table in transformation_tables:
                number = calculate_transformation(table, number)
            min_location = min(min_location, number)
        return min_location


if __name__ == "__main__":
    result = calculate_coordinates("input.txt")
    print(result)
