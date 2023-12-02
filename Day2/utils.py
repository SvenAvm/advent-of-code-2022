

def get_opponent_choices(file_path):
    opponent_choices = []
    opponents_choices_parsed = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            opponent_choices.append(parts[0])
    for choice in opponent_choices:
        if choice == 'A':
            opponents_choices_parsed.append("rock")
        elif choice == 'B':
            opponents_choices_parsed.append("paper")
        elif choice == 'C':
            opponents_choices_parsed.append("scissors")
    return opponents_choices_parsed


def get_player_choices_1(file_path):
    player_choices = []
    player_choices_parsed = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            player_choices.append(parts[1])
    for choice in player_choices:
        if choice == 'X':
            player_choices_parsed.append("rock")
        elif choice == 'Y':
            player_choices_parsed.append("paper")
        elif choice == 'Z':
            player_choices_parsed.append("scissors")
    return player_choices_parsed


def get_player_choices_2(file_path, opponent_choices):
    player_instructions = []
    player_instructions_parsed = []
    player_choices = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            player_instructions.append(parts[1])
    for choice in player_instructions:
        if choice == 'X':
            player_instructions_parsed.append("lose")
        elif choice == 'Y':
            player_instructions_parsed.append("draw")
        elif choice == 'Z':
            player_instructions_parsed.append("win")
    for instruction, opponent_choice in zip(player_instructions_parsed, opponent_choices):
        if opponent_choice == 'rock':
            if instruction == "lose":
                player_choices.append("scissors")
            elif instruction == "draw":  # Changed from "tie" to "draw"
                player_choices.append("rock")
            elif instruction == "win":
                player_choices.append("paper")
        elif opponent_choice == 'paper':
            if instruction == "lose":
                player_choices.append("rock")
            elif instruction == "draw":  # Changed from "tie" to "draw"
                player_choices.append("paper")
            elif instruction == "win":
                player_choices.append("scissors")
        elif opponent_choice == 'scissors':
            if instruction == "lose":
                player_choices.append("paper")
            elif instruction == "draw":  # Changed from "tie" to "draw"
                player_choices.append("scissors")
            elif instruction == "win":
                player_choices.append("rock")

    return player_choices


def give_base_score(choice):
    score = 0
    if choice == "rock":
        score += 1
    elif choice == "paper":
        score += 2
    elif choice == "scissors":
        score += 3
    return score
