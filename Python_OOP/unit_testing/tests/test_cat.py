from PythonOOP.unit_testing.cat import Cat


from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Lady")

    def test_init(self):
        self.assertEqual("Lady", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_cat_already_fed(self):
        self.cat.fed = True
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)
        self.assertEqual("Already fed.", str(ex.exception))

    def test_eat(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

        self.cat.fed = False
        self.cat.eat()
        self.assertEqual(2, self.cat.size)

    def test_sleep_cat_cannot_sleep_if_hungry(self):
        self.cat.sleepy = True
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

    def test_cat_sleeps(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        self.cat.sleep()
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()