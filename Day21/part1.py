TARGET_SCORE = 1000
DICE_FACES = 100


class Dice:
    def __init__(self, nb_faces):
        self._nb_faces = nb_faces
        self._value = self._nb_faces
        self.roll_count = 0

    def roll(self):
        self.roll_count += 1
        self._value += 1
        if self._value > self._nb_faces:
            self._value = 1
        return self._value


def play_turn(player_position, player_score, dice):
    # Roll dice 3 times
    rolls = sum(dice.roll() for _ in range(3))
    player_position = (player_position + rolls - 1) % 10 + 1
    player_score += player_position
    # print("rolls {} and move to space {} for a total score of {}.".format(rolls, player_position, player_score))
    return player_position, player_score


player_1_position = int(input().split(': ')[1])
player_2_position = int(input().split(': ')[1])

# print("Player 1 starting position:", player_1_position)
# print("Player 2 starting position:", player_2_position)

player_1_score = 0
player_2_score = 0

deterministic_dice = Dice(DICE_FACES)

round = 0
while player_1_score < TARGET_SCORE and player_2_score < TARGET_SCORE:
    if round % 2 == 0:
        # Player 1 plays
        # print("Player 1 ", end='')
        player_1_position, player_1_score = play_turn(player_1_position, player_1_score, deterministic_dice)
    else:
        # Player 2 plays
        # print("Player 2 ", end='')
        player_2_position, player_2_score = play_turn(player_2_position, player_2_score, deterministic_dice)
    round += 1

losing_player_score = min(player_1_score, player_2_score)
# print("Losing player score:", losing_player_score)
# print("Die had been rolled", deterministic_dice.roll_count)
print("Result", losing_player_score * deterministic_dice.roll_count)
