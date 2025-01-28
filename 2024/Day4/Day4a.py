import os
import re


def transpose_diagonally(matrix, direction: int = 1):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = []
    for i in range(m + n - 1):
        row = ""
        r = max(0, n - i - 1)
        c = max(i - n + 1, 0)
        for j in range(min(n - r, m - c)):
            if direction == 1:
                row += matrix[r + j][c + j]
            else:
                row += matrix[n - 1 - r - j][c + j]
        new_matrix.append(row)
    return new_matrix


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        row = ""
        for j in range(len(matrix)):
            row += matrix[j][i]
        new_matrix.append(row)
    return new_matrix


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    xmas_count = 0
    with open(input_path) as file:
        matrix = file.readlines()
        matrix = [line.strip() for line in matrix]
        matrix_transposed = transpose(matrix)
        matrix_diagonal_forward = transpose_diagonally(matrix)
        matrix_diagonal_backward = transpose_diagonally(matrix, -1)
        xmas_count += sum([len(re.findall(r"(?=(XMAS|SAMX))", line)) for line in matrix])
        xmas_count += sum([len(re.findall(r"(?=(XMAS|SAMX))", line)) for line in matrix_transposed])
        xmas_count += sum([len(re.findall(r"(?=(XMAS|SAMX))", line)) for line in matrix_diagonal_forward])
        xmas_count += sum([len(re.findall(r"(?=(XMAS|SAMX))", line)) for line in matrix_diagonal_backward])
        print(f"xmas count: {xmas_count}")


if __name__ == "__main__":
    solution("input.txt")
