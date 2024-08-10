from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "Blood Mage"
    level = 5
    health = 50.5
    damage = 10.6

    def setUp(self) -> None:
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_enemy_hero_has_the_same_name(self):
        enemy = Hero(self.username, 3, 333.3, 33.3)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_is_not_enough(self):
        self.hero.health = 0
        enemy = Hero("Arc Mage", 12, 30, 50)
        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(err.exception))
        self.hero.health = -1
        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(err.exception))

    def test_enemy_health_is_not_enough(self):
        enemy = Hero("Arc Mage", 12, 0, 50)
        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Arc Mage. He needs to rest", str(err.exception))
        enemy.health = -1
        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Arc Mage. He needs to rest", str(err.exception))

    def test_draw(self):
        enemy = Hero("Arc Mage", self.level, self.health, self.damage)
        result = self.hero.battle(enemy)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-2.5, self.hero.health)
        self.assertEqual(10.6, self.hero.damage)
        self.assertEqual("Draw", result)

    def test_hero_win(self):
        enemy = Hero("Arc Mage", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(54.5, self.hero.health)
        self.assertEqual(15.6, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy = Hero("Arc Mage", 100, 100, 100)
        result = self.hero.battle(enemy)
        self.assertEqual(101, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(105, enemy.damage)
        self.assertEqual("You lose", result)

    def test_string_representation(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected, str(self.hero))



if __name__ == "__main__":
    main()