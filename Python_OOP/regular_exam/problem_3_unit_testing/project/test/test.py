from unittest import TestCase, main
from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player1 = SoccerPlayer("Cristiano Ronaldo", 36, 800, "Manchester United")
        self.player2 = SoccerPlayer("Lionel Messi", 34, 750, "PSG")

    def test_valid_initialization(self):
        self.assertEqual(self.player1.name, "Cristiano Ronaldo")
        self.assertEqual(self.player1.age, 36)
        self.assertEqual(self.player1.goals, 800)
        self.assertEqual(self.player1.team, "Manchester United")
        self.assertEqual(self.player1.achievements, {})

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Mess", 34, 750, "PSG")
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Kylian Mbappe", 15, 150, "PSG")
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_invalid_team(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Zlatan Ibrahimovic", 39, 500, "AC Milan")
        self.assertEqual(str(ex.exception),
                         "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!")

    def test_negative_goals(self):
        player = SoccerPlayer("Karim Benzema", 33, -50, "Real Madrid")
        self.assertEqual(player.goals, 0)

    def test_change_team_success(self):
        result = self.player1.change_team("Juventus")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player1.team, "Juventus")

    def test_change_team_failure(self):
        result = self.player1.change_team("AC Milan")
        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.player1.team, "Manchester United")

    def test_add_new_achievement(self):
        result = self.player1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements["Ballon d'Or"], 1)

        # Add the same achievement again
        result = self.player1.add_new_achievement("Ballon d'Or")
        self.assertEqual(self.player1.achievements["Ballon d'Or"], 2)

    def test_comparison(self):
        result = self.player1 < self.player2
        self.assertEqual(result, "Cristiano Ronaldo is a better goal scorer than Lionel Messi.")

        result = self.player2 < self.player1
        self.assertEqual(result, "Cristiano Ronaldo is a top goal scorer! S/he scored more than Lionel Messi.")

if __name__ == "__main__":
    main()