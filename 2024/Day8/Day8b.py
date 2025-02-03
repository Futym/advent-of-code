import itertools
import os
from collections import defaultdict
from typing import List, Dict, Set, Tuple


def get_antennas(grid: List[List[str]]) -> Dict[str, Set[Tuple[int, int]]]:
    antennas = defaultdict(set)
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if column != '.':
                antennas[column].add((row_index, column_index))
    return antennas


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)

    with open(input_path) as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
        antinodes = set()
        antennas = get_antennas(grid)
        for antennas_positions in antennas.values():
            # antinodes.add(antennas_positions)
            antennas_pairs = list(itertools.combinations(antennas_positions, 2))
            for pair in antennas_pairs:
                vector = [a-b for a, b in zip(pair[0], pair[1])]
                antinode_a = pair[0]
                antinode_b = pair[1]
                while 0 <= antinode_a[0] < len(grid) and 0 <= antinode_a[1] < len(grid[0]):
                    antinodes.add(antinode_a)
                    antinode_a = tuple([a + b for a, b in zip(antinode_a, vector)])

                while 0 <= antinode_b[0] < len(grid) and 0 <= antinode_b[1] < len(grid[0]):
                    antinodes.add(antinode_b)
                    antinode_b = tuple([a - b for a, b in zip(antinode_b, vector)])

    print(f"Antinodes: {len(antinodes)}")


if __name__ == "__main__":
    solution("input.txt")
