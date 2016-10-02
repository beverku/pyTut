#!/usr/bin/python -tt

import unittest
from unittest import TestCase

import rpsls

choices = rpsls.choices[:]
rock_index = choices.index('rock')
spock_index = choices.index('spock')
paper_index = choices.index('paper')
lizard_index = choices.index('lizard')
scissors_index = choices.index('scissors')

class TestRpsls(TestCase):

    # Scissors cuts paper,
    def test_pick_winner_scissors_cuts_paper(self):
        result = rpsls.pick_winner(scissors_index, paper_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(paper_index, scissors_index)
        self.assertEqual("Player 2", result)

    # paper covers rock.
    def test_pick_winner_paper_covers_rock(self):
        result = rpsls.pick_winner(paper_index, rock_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(rock_index, paper_index)
        self.assertEqual("Player 2", result)

    # Rock crushes lizard,
    def test_pick_winner_rock_crushes_lizard(self):
        result = rpsls.pick_winner(rock_index, lizard_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(lizard_index, rock_index)
        self.assertEqual("Player 2", result)

    # lizard poisons Spock.
    def test_pick_winner_lizard_poisons_spock(self):
        result = rpsls.pick_winner(lizard_index, spock_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(spock_index, lizard_index)
        self.assertEqual("Player 2", result)

    # Spock smashes scissors,
    def test_pick_winner_spock_smashes_scissors(self):
        result = rpsls.pick_winner(spock_index, scissors_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(scissors_index, spock_index)
        self.assertEqual("Player 2", result)

    # scissors decapitates lizard.
    def test_pick_winner_scissors_decapitates_lizard(self):
        result = rpsls.pick_winner(scissors_index, lizard_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(lizard_index, scissors_index)
        self.assertEqual("Player 2", result)

    # Lizard eats paper
    def test_pick_winner_lizard_eats_paper(self):
        result = rpsls.pick_winner(lizard_index, paper_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(paper_index, lizard_index)
        self.assertEqual("Player 2", result)

    # paper disproves Spock,
    def test_pick_winner_paper_disproves_spock(self):
        result = rpsls.pick_winner(paper_index, spock_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(spock_index, paper_index)
        self.assertEqual("Player 2", result)

    # Spock vaporizes rock,
    def test_pick_winner_spock_vaporizes_rock(self):
        result = rpsls.pick_winner(spock_index, rock_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(rock_index, spock_index)
        self.assertEqual("Player 2", result)

    # rock crushes scissors.
    def test_pick_winner_rock_crushes_scissors(self):
        result = rpsls.pick_winner(rock_index, scissors_index)
        self.assertEqual("Player 1", result)

        result = rpsls.pick_winner(scissors_index, rock_index)
        self.assertEqual("Player 2", result)

    # ties
    def test_pick_winner_ties(self):
        self.assertEqual("Tie", rpsls.pick_winner(rock_index, rock_index))
        self.assertEqual("Tie", rpsls.pick_winner(paper_index, paper_index))
        self.assertEqual("Tie", rpsls.pick_winner(scissors_index, scissors_index))
        self.assertEqual("Tie", rpsls.pick_winner(lizard_index, lizard_index))
        self.assertEqual("Tie", rpsls.pick_winner(spock_index, spock_index))

# Boilerplate for running unit test when this script is called
# With more verbose output
suite = unittest.TestLoader().loadTestsFromTestCase(TestRpsls)
unittest.TextTestRunner(verbosity=2).run(suite)