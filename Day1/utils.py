def parse_input_to_elf_dict(file_path):
    sums_dict = {}
    current_sum = 0
    current_id = 1

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == '':  # Checks for a blank line
                sums_dict[f'Elf {current_id}'] = current_sum
                current_id += 1
                current_sum = 0
            else:
                current_sum += int(line.strip())

        # Adding the last sum if the file doesn't end with a blank line
        if current_sum > 0:
            sums_dict[str(current_id)] = current_sum

    return sums_dict


def find_max_elf(sums_dict):

    # Find the key with the maximum value
    max_elf = max(sums_dict, key=sums_dict.get)
    response = f"{max_elf} is carrying {sums_dict[max_elf]} calories, more then any other Elf."
    return response


def find_top_three_elves(elf_dict):
    top_three = sorted(elf_dict.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_three


def find_top_three_sum(elf_dict):
    top_three = find_top_three_elves(elf_dict)
    top_three_sum = sum(value for _, value in top_three)
    return top_three_sum
