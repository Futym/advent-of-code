import os
from itertools import groupby
from collections import defaultdict
from typing import List
from copy import deepcopy


def get_guard_position(grid: List[List[str]]) -> (int, int):
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value in ["^", ">", "v", "<"]:
                return row_index, col_index


def search_for_loop(grid: List[List[str]], x, y, direction) -> int:
    while len(grid[0]) - 1 > y > 0 and len(grid) - 1 > x > 0:
        x, y, direction = get_next_position(grid, x, y, direction)
        if grid[x][y] == direction:
            return True
    return False


def get_next_position(grid: List[List[str]], x, y, direction) -> (int, int, int):
    movement_map = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }
    x_step, y_step = movement_map[direction]
    if grid[x + x_step][y + y_step] == "#":
        direction = (direction + 1) % 4
    else:
        if grid[x][y] == ".":
            grid[x][y] = direction
        x += x_step
        y += y_step
    return x, y, direction


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    movement_map_support = {
        "^": 0,
        ">": 1,
        "v": 2,
        "<": 3
    }
    ways_to_loop = 0

    with open(input_path) as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
        x, y = get_guard_position(grid)
        initial_grid = deepcopy(grid)
        initial_grid[x][y] = "."
        movement_direction = movement_map_support[grid[x][y]]
        obstructions_checked = {(x, y):  True}
        while len(grid[0]) - 1 > y > 0 and len(grid) - 1 > x > 0:
            x_next, y_next, movement_direction_next = get_next_position(grid, x, y, movement_direction)
            if (x_next != x or y_next != y) and not obstructions_checked.get((x_next, y_next)):
                grid_copy = deepcopy(initial_grid)
                grid_copy[x_next][y_next] = "#"
                if search_for_loop(grid_copy, x, y, movement_direction):
                    ways_to_loop += 1
                obstructions_checked[(x_next, y_next)] = True

            x, y, movement_direction = x_next, y_next, movement_direction_next

    print(f"Ways to loop: {ways_to_loop}")


if __name__ == "__main__":
    solution("input.txt")
