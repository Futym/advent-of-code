import os
from collections import defaultdict


def read_file(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    with open(input_path) as file:
        left = []
        right = defaultdict(int)
        for line in file:
            left_elem, right_elem = line.strip().split()
            left.append(int(left_elem))
            right[int(right_elem)] += 1
    return left, right


def solution(input_file_name: str):
    left, right = read_file(input_file_name)
    result = 0
    for left_elem in left:
        result += left_elem * right[left_elem]
    print(f"Result is: {result}")


if __name__ == "__main__":
    solution("input.txt")
