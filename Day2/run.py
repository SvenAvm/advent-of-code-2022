import utils
import game

opponent_choices = utils.get_opponent_choices("day_2_input.txt")
player_choices_1 = utils.get_player_choices_1("day_2_input.txt")
player_choices_2 = utils.get_player_choices_2("day_2_input.txt", opponent_choices)

game.rock_paper_scissors(opponent_choices, player_choices_1)
game.rock_paper_scissors(opponent_choices, player_choices_2)
