

WINNING_NUMS_COUNT = 10
MY_NUMS_COUNT = 25

cards_copies_dict = {}


def init_dict(cards_count):
    cards_copies_dict.update({i: 1 for i in range(cards_count)})


def print_lev4_first_part_solution():
    with open("lev4_input.txt", 'r') as fourth_input_file:
        lines = fourth_input_file.readlines()
        init_dict(len(lines))
        for i, scratch_card in enumerate(lines):
            card_matches = 0
            winning_nums_set, my_nums = scratch_card.split(':')[1].split('|')
            winning_nums_set = set(filter(str.isdigit, winning_nums_set.split(' ')))
            my_nums = list(filter(str.isdigit, my_nums.rstrip('\n').split(' ')))
            for num in my_nums:
                if num in winning_nums_set:
                    card_matches += 1
            for row_below in range(i+1, i+1+card_matches):
                cards_copies_dict[row_below] += cards_copies_dict[i]
        print(sum(cards_copies_dict.values()))
