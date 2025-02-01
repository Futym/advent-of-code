import os
from operator import mul, add
from itertools import product


def solution(input_file_name: str) -> None:
    input_path = os.path.join(os.getcwd(), input_file_name)
    sum_of_operations = 0
    operators = [mul, add]
    with open(input_path) as file:
        for line in file:
            expected_result, components = line.strip().split(": ")
            components = components.split(" ")
            operators_combinations = list(product(*([operators] * (len(components) - 1))))
            for combination in operators_combinations:
                result = None
                for i, component in enumerate(components):
                    if not result:
                        result = int(component)
                    else:
                        result = combination[i-1](result, int(component))
                if result == int(expected_result):
                    sum_of_operations += result
                    break

    print(f"Sum of operations: {sum_of_operations}")


if __name__ == "__main__":
    solution("input.txt")
