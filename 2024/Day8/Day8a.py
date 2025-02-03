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
            antennas_pairs = list(itertools.combinations(antennas_positions, 2))
            for pair in antennas_pairs:
                vector = [a-b for a, b in zip(pair[0], pair[1])]
                antinodes.add(tuple([a + b for a, b in zip(pair[0], vector) if 0 <= (a + b) < len(grid)]))
                antinodes.add(tuple([a - b for a, b in zip(pair[1], vector) if 0 <= (a - b) < len(grid)]))
        antinodes = set(filter(lambda a: len(a) == 2, antinodes))

    print(f"Antinodes: {len(antinodes)}")


if __name__ == "__main__":
    solution("input.txt")
