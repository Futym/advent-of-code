import os


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    checksum = 0
    with open(input_path) as file:
        drive = [int(block) for block in file.readline().strip()]
    right_drive_index = len(drive) - 1
    left_drive_index = 0
    index = 0
    left_file_id = 0
    right_file_id = len(drive)//2
    while left_drive_index <= right_drive_index:
        if left_drive_index % 2 == 0:
            for j in range(drive[left_drive_index]):
                checksum += (index * left_file_id)
                index += 1
            left_file_id += 1
        else:
            j = 0
            while j < drive[left_drive_index]:
                if right_drive_index % 2 == 0:
                    if drive[right_drive_index] > 0:
                        checksum += (right_file_id * index)
                        index += 1
                        drive[right_drive_index] -= 1
                        j += 1
                    else:
                        while drive[right_drive_index] == 0:
                            right_drive_index -= 1
                        right_file_id -= 1
                else:
                    right_drive_index -= 1
        left_drive_index += 1

    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    solution("input.txt")
