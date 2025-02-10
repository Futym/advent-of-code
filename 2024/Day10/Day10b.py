import os
from typing import List, Tuple, Set


def get_trailheads(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    trailheads = set()
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if column == 0:
                trailheads.add((row_index, column_index))
    return trailheads


def find_score(grid: List[List[int]], trailhead) -> List[Tuple[int, int]]:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    peaks = []
    if grid[trailhead[0]][trailhead[1]] == 9:
        return [trailhead]
    for direction in directions:
        if len(grid) > trailhead[0] + direction[0] >= 0 and len(grid[0]) > trailhead[1] + direction[1] >= 0:
            if grid[trailhead[0]][trailhead[1]] + 1 == grid[trailhead[0] + direction[0]][trailhead[1] + direction[1]]:
                peak_pos = find_score(grid, (trailhead[0] + direction[0], trailhead[1] + direction[1]))
                if peak_pos:
                    peaks += peak_pos
    return peaks


def solution(input_file_name: str) -> None:
    input_path = os.path.join(os.getcwd(), input_file_name)

    with open(input_path) as file:
        lines = file.readlines()
        grid = [list(map(int, line.strip())) for line in lines]
        trailheads = get_trailheads(grid)
        scores_sum = 0
        for trailhead in trailheads:
            scores_sum += len(find_score(grid, trailhead))

    print(f"Sum of scores: {scores_sum}")


if __name__ == "__main__":
    solution("input.txt")
