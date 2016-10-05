#!/usr/bin/python -tt

"""
Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors
that allows five choices. Each choice wins against two other choices,
loses against two other choices and ties against itself.


Scissors cuts paper,
paper covers rock.
Rock crushes lizard,
lizard poisons Spock.
Spock smashes scissors,
scissors decapitates lizard.
Lizard eats paper,
paper disproves Spock,
Spock vaporizes rock,
rock crushes scissors.


see: https://www.coursera.org/learn/interactive-python-1/supplement/ijRP5/mini-project-description
"""

# TODO: use enum34?
choices = ['rock', 'spock', 'paper', 'lizard', 'scissors']


def get_choice(player_name):
    while True:
        choice = input(player_name + " enter choice (" + str(choices) + "): ")
        if choice.lower() in choices:
            return choice, choices.index(choice.lower())

    # Can't get here
    return None


# Think of this as a clock-face with rock at 0, spock at 1, etc.
# The rule is you beat opponents that are counter-clockwise
# and lost to opponents that are clockwise
# Subtract the number chosen by player two from the number chosen by player one,
# and then take the remainder modulo 5 of the result.
# Player one is the victor if the difference is one or two, and
# player two is the victor if the difference is three or four.
# If the difference is zero, the game is a tie.
def pick_winner(p1_choice_index, p2_choice_index):
    value = (p1_choice_index - p2_choice_index) % 5
    if value == 0:
        return "Tie"
    elif value == 1 or value == 2:
        return "Player 1"
    else:
        return "Player 2"


def main():
    p1_choice = get_choice("Player 1")
    p2_choice = get_choice("Player 2")

    result = pick_winner(p1_choice[1], p2_choice[1])
    print(result)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
