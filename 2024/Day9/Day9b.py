import os


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    checksum = 0
    with open(input_path) as file:
        drive = [int(block) for block in file.readline().strip()]
    right_drive_index = len(drive) - 1
    right_file_id = len(drive)//2
    files_ids = list(range(len(drive)//2 + 1))

    while 0 <= right_drive_index:
        if right_drive_index % 2 == 0:
            for i in range(1, right_drive_index, 2):
                space = drive[i]
                if space >= drive[right_drive_index]:
                    drive[i] = space - drive[right_drive_index]
                    drive.insert(i, drive[right_drive_index])
                    drive.insert(i, 0)
                    right_drive_index += 2
                    drive[right_drive_index] += drive[right_drive_index - 1]
                    if right_drive_index < len(drive) - 1:
                        drive[right_drive_index] += drive[right_drive_index + 1]
                        del drive[right_drive_index + 1]
                    del drive[right_drive_index-1]
                    files_ids.insert(i//2+1, files_ids[right_file_id])
                    del files_ids[right_file_id+1]
                    right_file_id += 1
                    break
            right_file_id -= 1
            right_drive_index -= 2
    index = 0
    for i, item in enumerate(drive):
        if i % 2 == 0:
            for j in range(index, index + item):
                checksum += (files_ids[i//2] * j)
            index += item
        else:
            index += item

    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    solution("input.txt")
