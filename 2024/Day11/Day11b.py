import os
from collections import defaultdict


def do_blink(stones: defaultdict) -> defaultdict:
    new_stones = defaultdict(int)
    for stone in stones:
        if stone == 0:
            new_stones[1] += stones[0]
        elif len(str(stone)) % 2 == 0:
            new_stones[int(str(stone)[:len(str(stone))//2])] += stones[stone]
            new_stones[int(str(stone)[len(str(stone))//2:])] += stones[stone]
        else:
            new_stones[stone * 2024] += stones[stone]
    return new_stones


def solution(input_file_name: str, blinks: int):
    input_path = os.path.join(os.getcwd(), input_file_name)
    with open(input_path) as file:
        stones_input = [int(stone) for stone in file.readline().strip().split()]
        stones = defaultdict(int)
        for stone in stones_input:
            stones[stone] += 1
        for blink in range(blinks):
            stones = do_blink(stones)

    print(f"All stones: {sum(stones.values())}")


if __name__ == "__main__":
    solution("input.txt", 75)
