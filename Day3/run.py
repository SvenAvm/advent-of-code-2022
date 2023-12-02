import utils

starting_items = (utils.parse_input("day_3_input.txt"))
task_1_sum = 0
task_2_sum = 0
badges = utils.find_badges(starting_items)

for rucksack in starting_items:
    compartment_1 = utils.split_compartment_1(rucksack)
    compartment_2 = utils.split_compartment_2(rucksack)
    duplicate = utils.check_for_duplicates(compartment_1, compartment_2)
    task_1_sum += utils.get_item_priority(utils.priorities, duplicate)

for badge in badges:
    task_2_sum += utils.get_item_priority(utils.priorities, badge)


print(f"""
Task 1 Sum: {task_1_sum}
Task 2 Sum: {task_2_sum}
""")
