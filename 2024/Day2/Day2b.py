import math
import os
from typing import List


def is_safe(levels: List[int]) -> bool:
    for i in range(0, len(levels)):
        partial_report = levels[:i] + levels[i+1:]
        direction = 0
        for j in range(len(partial_report)-1):
            if direction == 0:
                direction = math.copysign(1, partial_report[j + 1] - partial_report[j])
            step = (partial_report[j + 1] - partial_report[j]) * direction
            if step <= 0 or step > 3:
                break
        else:
            return True
    return False


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    safe_reports = 0
    with open(input_path) as file:
        for line in file:
            safe_reports += is_safe([int(elem) for elem in line.strip().split()])

    print(f"Safe reports: {safe_reports}")


if __name__ == "__main__":
    solution("input.txt")
