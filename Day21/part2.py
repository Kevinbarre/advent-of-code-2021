import itertools
from collections import Counter
from pprint import pprint

TARGET_SCORE = 21

# Possible sum of the values of the dirac dice on 3 rolls
ROLLS = Counter(sum(roll) for roll in itertools.product((1, 2, 3), repeat=3))


# print(ROLLS)


def play_turn(player_position, player_score, rolls):
    player_position = (player_position + rolls - 1) % 10 + 1
    player_score += player_position
    # print("rolls {} and move to space {} for a total score of {}.".format(rolls, player_position, player_score))
    return player_position, player_score


player_1_starting_position = int(input().split(': ')[1])
player_2_starting_position = int(input().split(': ')[1])

# # print("Player 1 starting position:", player_1_starting_position)
# # print("Player 2 starting position:", player_2_starting_position)
#
player_1_starting_score = 0
player_2_starting_score = 0

# Universes (Player 1 position, player 1 score, player 2 position, player 2 score) by count
ongoing_universes = {
    (player_1_starting_position, player_1_starting_score, player_2_starting_position, player_2_starting_score): 1}
# Count number of time each player won
winning_player = {1: 0, 2: 0}

round = 0
while ongoing_universes:
    # pprint(ongoing_universes)
    new_universes = {}
    for universe, count in ongoing_universes.items():
        for possible_roll, roll_count in ROLLS.items():
            new_universe_count = count * roll_count  # Total number of universes created by the roll
            player_1_position, player_1_score, player_2_position, player_2_score = universe
            if round % 2 == 0:
                # Player 1 plays
                player_1_position, player_1_score = play_turn(player_1_position, player_1_score, possible_roll)
            else:
                # Player 2 plays
                player_2_position, player_2_score = play_turn(player_2_position, player_2_score, possible_roll)

            if player_1_score >= TARGET_SCORE:
                # Player 1 won in these universes with this roll
                winning_player[1] += new_universe_count
            elif player_2_score >= TARGET_SCORE:
                # Player 2 won in these universes with this roll
                winning_player[2] += new_universe_count
            else:
                # Nobody won, keep playing in new universes
                try:
                    new_universes[
                        (player_1_position, player_1_score, player_2_position, player_2_score)] += new_universe_count
                except KeyError:
                    new_universes[
                        (player_1_position, player_1_score, player_2_position, player_2_score)] = new_universe_count

    # Moving on for another round
    ongoing_universes = new_universes
    round += 1

print("Result:", max(winning_player.values()))
