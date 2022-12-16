

INPUT = "1321131112"

if __name__ == "__main__":
    result = INPUT
    iterations = input("Give number of Iterations: ")
    for i in range(int(iterations)):
        temp_result = ""
        prev_num = "0"
        repetition_of_number = 0
        for number in result:
            if (number == prev_num):
                repetition_of_number += 1
            else:
                if (prev_num != "0"):
                    temp_result += str(repetition_of_number) + prev_num
                prev_num = number
                repetition_of_number = 1
        temp_result += str(repetition_of_number) + prev_num
        result = temp_result

    print(len(result))
