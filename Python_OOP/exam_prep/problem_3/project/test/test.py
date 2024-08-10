from project.robot import Robot

from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("One1", "Education", 150, 10)

    def test_init(self):
        r = Robot("One1", "Education", 150, 10)
        self.assertEqual(r.robot_id, "One1")
        self.assertEqual(r.category, "Education")
        self.assertEqual(r.available_capacity, 150)
        self.assertEqual(r.price, 10)
        self.assertEqual(r.hardware_upgrades, [])
        self.assertEqual(r.software_updates, [])

    def test_init_invalid_category_raises(self):
        with self.assertRaises(ValueError) as ex:
            r = Robot("One1", "a", 150, 10)
        self.assertEqual(str(ex.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_init_robot_invalid_price_raises(self):
        with self.assertRaises(ValueError) as ex:
            r = Robot("One1", "Education", 150, -1)
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_hardware_upgrade_with_component_in_the_list(self):
        self.robot.hardware_upgrades.append("Part A")
        self.assertEqual(self.robot.hardware_upgrades, ["Part A"])
        self.assertEqual(self.robot.price, 10)
        result = self.robot.upgrade("Part A", 10)
        self.assertEqual(self.robot.hardware_upgrades, ["Part A"])
        self.assertEqual(self.robot.price, 10)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not upgraded.")

    def test_hardware_upgrade_with_component_not_in_the_list(self):
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.price, 10)
        result = self.robot.upgrade("Part 1", 10)
        self.assertEqual(self.robot.hardware_upgrades, ["Part 1"])
        self.assertEqual(self.robot.price, 25.0)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was upgraded with Part 1.')

    def test_updates_no_updates_yet_does_update(self):
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 150)
        result = self.robot.update(15, 200)
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 150)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    def test_update_with_version_less_than_existing_not_update(self):
        self.robot.software_updates = [10, 20, 5]
        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 150)
        result = self.robot.update(15, 200)
        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 150)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    def test_update_available_capacity_is_not_enough_does_not_update(self):
        self.robot.software_updates = [10, 20, 5]
        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 150)
        self.assertLess(self.robot.available_capacity, 200)
        result = self.robot.update(25, 200)
        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 150)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    def test_update(self):
        self.robot.software_updates = [10, 20, 5]
        self.assertEqual(self.robot.software_updates, [10, 20, 5])
        self.assertEqual(self.robot.available_capacity, 150)
        result = self.robot.update(25, 30)
        self.assertEqual(self.robot.software_updates, [10, 20, 5, 25])
        self.assertEqual(self.robot.available_capacity, 120)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was updated to version 25.')

    def test_compare(self):
        robot_less = Robot("One1", "Education", 150, 1)
        robot_equal = Robot("One1", "Education", 150, 10)
        robot_greater = Robot("One1", "Education", 150, 20)

        result = self.robot.__gt__(robot_less)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} 'f'is more expensive than Robot with ID {robot_less.robot_id}.)

        result = self.robot.__gt__(robot_equal)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {robot_equal.robot_id}.')

        result = self.robot.__gt__(robot_greater)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {robot_greater.robot_id}.'


if __name__ == "__main__":
    main()
