def calculate_transformation(table, number_ranges):
    new_number_ranges = []
    for seed_range in number_ranges:
        seed = seed_range[0]
        while seed < seed_range[1]:
            min_dist_to_next_sec = float('inf')
            for line in table:
                if line[1] <= seed < line[1] + line[2]:
                    new_number_ranges.append([line[0] + seed - line[1],
                                              line[0] + min(line[2], seed_range[1] - line[1])])
                    seed = min(line[1] + line[2], seed_range[1])
                    break
                else:
                    if 0 < line[1] - seed < min_dist_to_next_sec:
                        min_dist_to_next_sec = line[1] - seed
            else:
                if min_dist_to_next_sec < float('inf'):
                    new_number_ranges.append([seed, seed + min_dist_to_next_sec])
                    seed = seed + min_dist_to_next_sec
                else:
                    new_number_ranges.append([seed, seed_range[1]])
                    seed = seed_range[1]
    return new_number_ranges


def calculate_coordinates(filename):
    with open(filename, "r") as file:
        seeds_groups = list(map(lambda x: int(x), file.readline().split(":")[1].strip().split()))
        seeds = []
        for i in range(0, len(seeds_groups), 2):
            seeds.append([seeds_groups[i], seeds_groups[i] + seeds_groups[i+1]])
        transformation_tables = []
        for line in file:
            if line == "\n":
                table = []
                transformation_tables.append(table)
            elif line.strip().split()[0].isdigit():
                table.append(list(map(lambda x: int(x), line.strip().split())))
        min_location = float("inf")
        for seed_range in seeds:
            numbers_ranges = [seed_range]
            for table in transformation_tables:
                numbers_ranges = calculate_transformation(table, numbers_ranges)
            for number_range in numbers_ranges:
                if number_range[0] < min_location:
                    min_location = number_range[0]
        return min_location


if __name__ == "__main__":
    result = calculate_coordinates("input.txt")
    print(result)
