import os


def solution(input_file_name: str):
    input_path = os.path.join(os.getcwd(), input_file_name)
    xmas_count = 0
    with open(input_path) as file:
        input = file.readlines()
        for i in range(1, len(input)-1):
            for j in range(1, len(input[i])-1):
                if input[i][j] == "A":
                    x_mas = True
                    if (input[i-1][j-1] + input[i+1][j+1] != "SM" and input[i-1][j-1] + input[i+1][j+1] != "MS") \
                            or (input[i+1][j-1] + input[i-1][j+1] != "SM" and input[i+1][j-1] + input[i-1][j+1] != "MS"):
                        x_mas = False
                    if x_mas:
                        xmas_count += 1
    print(f"x_mas count: {xmas_count}")


if __name__ == "__main__":
    solution("example.txt")
