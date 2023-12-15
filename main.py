
digs_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,

}


def finish_line(line_iter, input_line, is_first: bool):
    if is_first:
        if line_iter == len(input_line):
            return True
    else:
        if -1*line_iter > len(input_line):
            return True
    return False


def dig_first_or_last(input_line, is_first: bool):
    line_iter = 0 if is_first else -1
    while not finish_line(line_iter, line, is_first):
        if input_line[line_iter].isdigit():
            return int(input_line[line_iter])
        for dig in digs_dict.keys():
            is_dig = True
            for i, letter in enumerate(dig[::1 if is_first else -1]):
                i = i if is_first else -1*(i+1)
                if finish_line(line_iter + i, input_line, is_first):
                    break
                is_dig &= letter == input_line[line_iter + i]
                if not is_dig:
                    break
            if is_dig:
                return digs_dict[dig]
        line_iter += 1 if is_first else -1


if __name__ == "__main__":
    with open("lev1_input.txt", 'r') as input_file:
        sum = 0
        for line in input_file.readlines():
            length = len(line)
            first = dig_first_or_last(line, True)
            last = dig_first_or_last(line, False)
            current = first * 10 + last
            sum += current
        print(sum)
