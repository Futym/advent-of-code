import os
from itertools import groupby


def read_input(file_name):
    input_path = os.path.join(os.getcwd(), file_name)
    with open(input_path) as file:
        lines = file.readlines()
        [pages_order, manual_pages] = [list(group) for k, group in groupby(lines, lambda x: x == "\n") if not k]
        return pages_order, manual_pages


def check_order(instruction, pages_order_dict):
    pages = instruction.strip().split(",")
    for i, page in enumerate(pages):
        if pages_order_dict.get(page):
            for prev_page in pages_order_dict[page]:
                if prev_page in pages[i:]:
                    return -1
    return pages[len(pages)//2]


def solution(input_file_name: str):
    pages_order, instructions = read_input(input_file_name)
    pages_order_dict = dict()
    sum_middle_pages = 0
    for line in pages_order:
        first_page, second_page = line.strip().split("|")
        if pages_order_dict.get(second_page):
            pages_order_dict[second_page] = pages_order_dict[second_page]+[first_page]
        else:
            pages_order_dict[second_page] = [first_page]

    for instruction in instructions:
        middle_page = check_order(instruction, pages_order_dict)
        if middle_page != -1:
            sum_middle_pages += int(middle_page)

    print(f"Sum of middle pages: {sum_middle_pages}")


if __name__ == "__main__":
    solution("input.txt")
