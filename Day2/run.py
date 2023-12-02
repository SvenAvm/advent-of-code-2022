import utils
import game

opponent_choices = utils.get_opponent_choices("input.txt")
player_choices_1 = utils.get_player_choices_1("input.txt")
player_choices_2 = utils.get_player_choices_2("input.txt", opponent_choices)

game.rock_paper_scissors(opponent_choices, player_choices_1)
game.rock_paper_scissors(opponent_choices, player_choices_2)
