import utils


def rock_paper_scissors(opponent_choices, players_choices):
    player_score = 0
    game_count = 0

    for opp_choice, ply_choice in zip(opponent_choices, players_choices):
        game_count += 1
        player_score += utils.give_base_score(ply_choice)

        if opp_choice == "rock":
            if ply_choice == "rock":
                player_score += 3
            elif ply_choice == "paper":
                player_score += 6
            # elif ply_choice == "scissors": pass

        elif opp_choice == "paper":
            if ply_choice == "rock":
                pass  # No score change
            elif ply_choice == "paper":
                player_score += 3
            elif ply_choice == "scissors":
                player_score += 6

        elif opp_choice == "scissors":
            if ply_choice == "rock":
                player_score += 6
            elif ply_choice == "paper":
                pass  # No score change
            elif ply_choice == "scissors":
                player_score += 3

    print(f"""
    Game Count: {game_count}
    Player Score: {player_score}
""")
