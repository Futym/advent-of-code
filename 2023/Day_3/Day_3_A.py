import re


def calculate_act_line(batch):
    pattern = r"\d+"
    ret = 0
    idx = 0
    while idx < len(batch['act_line']):
        if batch['act_line'][idx].isdigit():
            search_res = re.search(pattern, batch['act_line'][idx:])
            number = int(search_res.group())
            start_idx = search_res.start() + idx
            if search_res.end() + idx < len(batch['act_line']):
                end_idx = (search_res.end() + idx)
            else:
                end_idx = len(batch['act_line']) - 1
            idx = search_res.end() + idx
            for searched_idx in range(start_idx-1, end_idx+1):
                if batch['prev_line'] and batch['prev_line'][searched_idx] != "." \
                        and not batch['prev_line'][searched_idx].isdigit() \
                        or batch['act_line'][searched_idx] != "." \
                        and not batch['act_line'][searched_idx].isdigit() \
                        or batch['next_line'] and batch['next_line'][searched_idx] != "."\
                        and not batch['next_line'][searched_idx].isdigit():
                    ret += number
                    break
        else:
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
