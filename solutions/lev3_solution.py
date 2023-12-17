import re

# region part 1


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
# endregion


# region part 2


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

# endregion


def print_lev3_solution():
    with open("solutions/lev3_input.txt", 'r') as third_input_file:
        schema = third_input_file.readlines()
        print("lev3 part1:", sum_engine_part_numbers(schema))
        print("lev3 part2:", sum_gear_ratios(schema))
