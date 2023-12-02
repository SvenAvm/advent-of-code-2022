priorities = {
 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27,
 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}


def parse_input(filename):
    output = []
    with open(filename, 'r') as file:
        for line in file:
            output.append(line.strip())
    return output


def split_compartment_1(rucksack):
    midpoint = len(rucksack) // 2
    compartment_1 = ""
    for i in range(midpoint):
        compartment_1 += rucksack[i]
    return compartment_1


def split_compartment_2(rucksack):
    midpoint = len(rucksack) // 2
    compartment_2 = ""
    for i in range(midpoint, len(rucksack)):
        compartment_2 += rucksack[i]
    return compartment_2


def check_for_duplicates(compartment1, compartment2):
    for char in compartment1:
        if char in compartment2:
            return char


def get_item_priority(priorities_dict, key):
    if key in priorities_dict:
        return priorities_dict[key]


def find_badges(string_list):
    common_letters = []

    for i in range(0, len(string_list), 3):
        # Extract up to the next three strings
        group = string_list[i:i+3]

        # Check if the group has less than 3 strings
        if len(group) < 3:
            break

        # Find common letters in the three strings
        common_in_group = set(group[0]).intersection(group[1], group[2])

        # Add the common letters to the result list
        common_letters.extend(common_in_group)

    return common_letters
