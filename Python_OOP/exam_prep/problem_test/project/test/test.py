import unittest

from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player_1 = TennisPlayer("Dimitrov", 33, 3770)
        self.player_2 = TennisPlayer("Djokovic", 37, 8460)
        self.player_3 = TennisPlayer("Rune", 21, 2300)

    def test_init(self):
        self.assertEqual("Dimitrov", self.player_1.name)
        self.assertEqual(33, self.player_1.age)
        self.assertEqual(3770, self.player_1.points)
        self.assertEqual([], self.player_1.wins)

    def test_name_less_or_equal_of_two_symbols_raises_error(self):
        with self.assertRaises(ValueError) as err:
            TennisPlayer("Aa", 20, 2222)
        self.assertEqual("Name should be more than 2 symbols!", str(err.exception))

    def test_age_less_or_equal_to_18_raises_error(self):
        with self.assertRaises(ValueError) as err:
            TennisPlayer("Nadal", 17, 3564)
        self.assertEqual("Players must be at least 18 years of age!", str(err.exception))

    def test_add_tournament_win_if_not_existing_should_add(self):
        result = self.player_1.add_new_win("Brisbane 2024")
        self.assertEqual(["Brisbane 2024"], self.player_1.wins)
        self.assertIsNone(result)

    def test_add_already_existing_tournament_win_should_not_add(self):
        self.player_1.add_new_win("Brisbane 2024")
        result = self.player_1.add_new_win("Brisbane 2024")
        self.assertEqual(f"Brisbane 2024 has been already added to the list of wins!", result)

    def test_lt_should_return_self_player_is_better(self):
        result = self.player_1 < self.player_3
        self.assertEqual("Dimitrov is a better player than Rune", result)

    def test_lt_should_return_that_other_player_is_better(self):
        result = self.player_1 < self.player_2
        self.assertEqual('Djokovic is a top seeded player and he/she is better than Dimitrov')

    def test_str_with_no_wins(self):
        result = str(self.player_1)
        self.assertEqual("Tennis Player: Dimitrov\nAge: 33\nPoints: 3770.0\nTournaments won: ", result)

    def test_str_with_wins(self):
        self.player_1.add_new_win("ATP Finals 2017")
        self.player_1.add_new_win("Brisbane 2024")
        result = str(self.player_1)
        expected = ("Tennis Player: Dimitrov\nAge: 33\nPoints: 3770\nTournaments won: ATP Finals 2017, Brisbane 2024")
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()