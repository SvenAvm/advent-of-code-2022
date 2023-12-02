import utils

parsed_input = utils.parse_input_to_elf_dict("day_1_input.txt")
solution = f"""
{utils.find_max_elf(parsed_input)}
Top three Elves are carrying a total of {utils.find_top_three_sum(parsed_input)} calories.
"""

print(solution)
