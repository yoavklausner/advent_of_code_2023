import re


''' level 1 utils
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
'''


# =========== level 3 sub-methods
''' part one
def is_symbol(character: chr):
    return not character.isdigit() and character != '.'


def search_symbol(schema_grid, line_index, start_search, end_search):
    found = False
    for i in range(start_search, end_search):
        found |= is_symbol(schema_grid[line_index][i])
    return found


def is_part_number(re_match: re.Match, line_index, schema_grid):
    start = re_match.start()
    end = re_match.end()
    line_len = len(schema_grid[line_index])
    start_search = start - 1 if start > 0 else 0
    end_search = end + 1 if end < line_len - 1 else line_len - 1
    if is_symbol(schema_grid[line_index][start_search]) or is_symbol(schema_grid[line_index][end_search - 1]):
        return True
    if line_index > 0 and search_symbol(schema_grid, line_index - 1, start_search, end_search):
        return True
    if line_index < len(schema_grid) - 1 and search_symbol(schema_grid, line_index + 1, start_search, end_search):
        return True
    return False


def sum_engine_part_numbers(schema_grid):
    part_nums_sum = 0
    pattern = re.compile(r'\d+')
    for i, line in enumerate(schema_grid):
        line.strip('\n')  # ignoring \n
        matches = re.finditer(pattern, line)
        for num_match in matches:
            if is_part_number(num_match, i, schema_grid):
                part_nums_sum += int(num_match.group())
    return part_nums_sum
'''


NUMBER_PATTERN = re.compile(r'\d+')
LEFT_ADJACENT_NUM_PATTERN = re.compile(r'\d+$')
RIGHT_ADJACENT_NUM_PATTERN = re.compile(r'^\d+')


def get_adjacent_numbers(number_matches, star_index):
    adjacent_numbers = []
    for num_match in number_matches:
        if num_match.start() <= star_index + 1 and num_match.end() >= star_index:
            adjacent_numbers.append(int(num_match.group()))
    return adjacent_numbers


def get_gear_ratio(star_match, line_index, schema_grid):
    start = star_match.start()
    end = star_match.end()
    all_adjacent_numbers = []
    left_adjacent_match = LEFT_ADJACENT_NUM_PATTERN.search(schema_grid[line_index][:start])
    right_adjacent_match = RIGHT_ADJACENT_NUM_PATTERN.search(schema_grid[line_index][end:]) if end < len(schema_grid[line_index]) else None
    if line_index > 0:
        all_adjacent_numbers.extend(get_adjacent_numbers(re.finditer(NUMBER_PATTERN, schema_grid[line_index - 1]), start))
    if line_index < len(schema_grid) - 1:
        all_adjacent_numbers.extend(get_adjacent_numbers(re.finditer(NUMBER_PATTERN, schema_grid[line_index + 1]), start))
    if left_adjacent_match:
        all_adjacent_numbers.append(int(left_adjacent_match.group()))
    if right_adjacent_match:
        all_adjacent_numbers.append(int(right_adjacent_match.group()))
    return all_adjacent_numbers[0]*all_adjacent_numbers[1] if len(all_adjacent_numbers) == 2 else 0


def sum_gear_ratios(schema_grid):
    ratios_sum = 0
    for i, line in enumerate(schema_grid):
        line.strip('\n')
        for star_match in re.finditer(r'\*', line):
            ratios_sum += get_gear_ratio(star_match, i, schema_grid)
    return ratios_sum

# ===========


if __name__ == "__main__":
    '''  level 1
    with open("lev1_input.txt", 'r') as input_file:
        sum = 0
        for line in input_file.readlines():
            length = len(line)
            first = dig_first_or_last(line, True)
            last = dig_first_or_last(line, False)
            current = first * 10 + last
            sum += current
        print(sum)
    '''
    '''     level 2
    with open("lev2_input.txt", 'r') as sec_input_file:
        id_sum = 0
        RED = "red"
        BLUE = "blue"
        GREEN = "green"
        for i, line in enumerate(sec_input_file.readlines()):
            max_red = 1
            max_green = 1
            max_blue = 1
            sets = line.split(':')[1].split(';')
            for cubes_set in sets:
                current_cubes = cubes_set.split(',')
                for cube in current_cubes:
                    amount = int(re.search(r'\d+', cube).group())
                    if RED in cube and amount > max_red:
                        max_red = amount
                    elif GREEN in cube and amount > max_green:
                        max_green = amount
                    elif BLUE in cube and amount > max_blue:
                        max_blue = amount
            id_sum += max_green * max_blue * max_red
        print(id_sum)
    '''
    with open("lev3_input.txt", 'r') as third_input_file:
        schema = third_input_file.readlines()
        # print(sum_engine_part_numbers(schema)) ** first part **
        print(sum_gear_ratios(schema))
    '''
    pattern = re.compile(r'-*\d+')
    s = "1723....230583....-30239235*...--2219,..._...39"
    sum_this = 0
    for m in re.findall(pattern, s):
        sum_this += int(m)
    print(sum_this)
    '''
