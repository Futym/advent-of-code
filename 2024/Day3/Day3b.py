import os
import re


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    sum_of_muls = 0
    enabled = True
    with open(input_path) as file:
        for line in file:
            pairs = re.findall(r'(don\'t\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))', line)
            for pair in pairs:
                if pair[0] == "don't()":
                    enabled = False
                elif pair[0] == "do()":
                    enabled = True
                elif enabled:
                    sum_of_muls += int(pair[1]) * int(pair[2])

    print(f"Sum of multiplications: {sum_of_muls}")


if __name__ == "__main__":
    solution("input.txt")
