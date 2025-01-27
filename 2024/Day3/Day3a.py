import os
import re


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    sum_of_muls = 0
    with open(input_path) as file:
        for line in file:
            pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
            sum_of_muls += sum([int(a)*int(b) for a, b in pairs])

    print(f"Sum of multiplications: {sum_of_muls}")


if __name__ == "__main__":
    solution("input.txt")
