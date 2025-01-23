import os


def is_safe(line: str) -> bool:
    levels = line.strip().split()
    direction = 1 if int(levels[0]) < int(levels[1]) else -1
    prev_elem = int(levels[0])
    for elem in levels[1:]:
        step = (int(elem) - int(prev_elem)) * direction
        if step <= 0 or step > 3:
            return False
        prev_elem = elem
    else:
        return True


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    safe_reports = 0
    with open(input_path) as file:
        for line in file:
            safe_reports += int(is_safe(line))
    print(f"Safe reports: {safe_reports}")


if __name__ == "__main__":
    solution("input.txt")
