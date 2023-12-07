def find_number(line, idx):
    number = 0
    if 0 <= idx < len(line) and line[idx].isdigit():
        while idx >= 0 and line[idx].isdigit():
            idx -= 1
        idx += 1
        while idx < len(line) and line[idx].isdigit():

            number = number*10 + int(line[idx])
            idx += 1
    if number > 0:
        print(number)
    return number


def calculate_act_line(batch):
    ret = 0
    idx = 0
    while idx < len(batch['act_line']):
        if batch['act_line'][idx] == '*':
            parts_counter = 0
            parts_mul = 1
            if batch['prev_line']:
                found_number = find_number(batch['prev_line'], idx)
                if found_number != 0:
                    parts_counter += 1
                    parts_mul *= found_number
                else:
                    found_number = find_number(batch['prev_line'], idx+1)
                    if found_number:
                        parts_counter += 1
                        parts_mul *= found_number
                    found_number = find_number(batch['prev_line'], idx-1)
                    if found_number:
                        parts_counter += 1
                        parts_mul *= found_number

            found_number = find_number(batch['act_line'], idx + 1)
            if found_number:
                parts_counter += 1
                parts_mul *= found_number
            found_number = find_number(batch['act_line'], idx - 1)
            if found_number:
                parts_counter += 1
                parts_mul *= found_number

            if batch['next_line']:
                found_number = find_number(batch['next_line'], idx)
                if found_number != 0:
                    parts_counter += 1
                    parts_mul *= found_number
                else:
                    found_number = find_number(batch['next_line'], idx+1)
                    if found_number:
                        parts_counter += 1
                        parts_mul *= found_number
                    found_number = find_number(batch['next_line'], idx-1)
                    if found_number:
                        parts_counter += 1
                        parts_mul *= found_number
            if parts_counter == 2:
                ret += parts_mul
        idx += 1
    return ret


def calculate_result(filename):
    with open(filename, "r") as file:
        actual_batch = {'prev_line': None,
                        'act_line': None,
                        'next_line': None}
        res = 0
        lines = file.readlines()
        for idx, line in enumerate(lines):
            if idx > 0:
                actual_batch['prev_line'] = actual_batch['act_line']
            actual_batch['act_line'] = line.strip()
            if idx < len(lines) - 1:
                actual_batch['next_line'] = lines[idx+1].strip()
            else:
                actual_batch['next_line'] = None
            res += calculate_act_line(actual_batch)

        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
