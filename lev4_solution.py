

WINNING_NUMS_COUNT = 10
MY_NUMS_COUNT = 25


def print_lev4_first_part_solution():

    with open("lev4_input.txt", 'r') as fourth_input_file:
        total_point = 0
        for scratch_card in fourth_input_file.readlines():
            card_matches = 0
            winning_nums_set, my_nums = scratch_card.split(':')[1].split('|')
            winning_nums_set = set(filter(str.isdigit, winning_nums_set.split(' ')))
            my_nums = list(filter(str.isdigit, my_nums.rstrip('\n').split(' ')))
            for num in my_nums:
                if num in winning_nums_set:
                    card_matches += 1
            if card_matches > 0:
                total_point += 2**(card_matches-1)
        print(total_point)
