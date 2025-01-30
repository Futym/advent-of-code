import os
from typing import List


def get_guard_position(grid: List[List[str]]) -> (int, int):
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value in ["^", ">", "v", "<"]:
                print(row_index, col_index)

                return row_index, col_index


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    movement_map = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }
    movement_map_support = {
        "^": 0,
        ">": 1,
        "v": 2,
        "<": 3
    }
    count_tiles = 0

    with open(input_path) as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
        x, y = get_guard_position(grid)
        movement_direction = movement_map_support[grid[x][y]]
        while len(grid[0]) - 1 > y > 0 and len(grid) - 1 > x > 0:
            x_step, y_step = movement_map[movement_direction]
            if grid[x + x_step][y + y_step] == "#":
                movement_direction = (movement_direction + 1) % 4
            else:
                if grid[x][y] != "X":
                    count_tiles += 1
                    grid[x][y] = "X"
                x += x_step
                y += y_step
        count_tiles += 1

    print(f"Tiles visited: {count_tiles}")


if __name__ == "__main__":
    solution("input.txt")
