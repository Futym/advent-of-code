import os


def get_number_of_stones(stone: int, blinks: int):
    if blinks == 0:
        return 1
    if stone == 0:
        return get_number_of_stones(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        return (get_number_of_stones(int(str(stone)[:len(str(stone))//2]), blinks - 1) +
                get_number_of_stones(int(str(stone)[len(str(stone))//2:]), blinks - 1))
    else:
        return get_number_of_stones(stone * 2024, blinks - 1)


def solution(input_file_name: str, blinks: int):
    input_path = os.path.join(os.getcwd(), input_file_name)
    with open(input_path) as file:
        stones = [int(stone) for stone in file.readline().strip().split()]
        all_stones = 0
        for stone in stones:
            all_stones += get_number_of_stones(stone, blinks)

    print(f"All stones: {all_stones}")


if __name__ == "__main__":
    solution("input.txt", 75)
