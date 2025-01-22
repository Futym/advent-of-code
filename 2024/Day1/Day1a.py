import os


def read_file(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    with open(input_path) as file:
        left = []
        right = []
        for line in file:
            left_elem, right_elem = line.strip().split()
            left.append(int(left_elem))
            right.append(int(right_elem))
    return left, right


def solution(input_file_name: str):
    left, right = read_file(input_file_name)
    left.sort()
    right.sort()
    result = 0
    for left_elem, right_elem in zip(left, right):
        result += abs(left_elem - right_elem)
    print(f"Result is: {result}")


if __name__ == "__main__":
    solution("input.txt")
