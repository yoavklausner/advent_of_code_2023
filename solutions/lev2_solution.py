import re


def print_lev2_solution():
    with open("solutions/lev2_input.txt", 'r') as sec_input_file:
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
        print("lev2 part2:", id_sum)
