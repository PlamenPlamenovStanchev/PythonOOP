from PythonOOP.unit_testing.List.extended_list import IntegerList


from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(5, -3, 4, 1, 17, 2)

    def test_init(self):
        l = IntegerList()
        self.assertEqual([], l._IntegerList__data)

        l = IntegerList("asd", 5, -3, 4.2, [1, 2, 3])
        self.assertEqual([5, 3], l._IntegerList__data)

    def test_get_data(self):
        result = self.list.get_data()
        self.assertEqual(self.list._IntegerList__data, result)
        self.assertEqual(id(self.list._IntegerList__data), id(result))

    def test_add_non_integer_raises(self):
        self.assertNotIn("asd", self.list._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            self.list.add("asd")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertNotIn("asd", self.list._IntegerList__data)

    def test_add_integer_at_the_end(self):
        self.assertEqual([5, -3, 4, 1, 17, 2], self.list._IntegerList__data)
        result = self.list.add(100)
        self.assertIn(100, self.list._IntegerList__data)
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], result)

    def test_remove_index_is_equal_or_greater_than_length_raises(self):
        index_to_remove = len(self.list.get_data())
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(index_to_remove)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        index_to_remove = len(self.list.get_data()) + 1
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(index_to_remove)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

    def remove_index_removes_element(self):
        self.assertIn(5, self.list._IntegerList__data)
        result = self.list.remove_index(0)

        self.assertNotIn(5, self.list._IntegerList__data)
        self.assertEqual(5, result)

        self.assertIn(17, self.list._IntegerList__data)
        result = self.list.remove_index(3)

        self.assertNotIn(17, self.list._IntegerList__data)
        self.assertEqual(17, result)

    def test_get_index_is_equal_or_greater_than_length_raises(self):
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)
        self.assertEqual(6, len(self.list._IntegerList__data))

        index_to_get = len(self.list.get_data())
        with self.assertRaises(IndexError) as ex:
            self.list.get(index_to_get)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        index_to_get = len(self.list.get_data()) + 1
        with self.assertRaises(IndexError) as ex:
            self.list.get(index_to_get)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

    def test_get_returns_element(self):
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        index_to_get = 3

        result = self.list.get(index_to_get)
        self.assertEqual(1, result)
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

    def test_insert_equal_or_greater_than_length_raises(self):
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)
        index = len(self.list.get_data())
        with self.assertRaises(IndexError) as ex:
            self.list.get(index)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)
        index = len(self.list.get_data()) + 1
        with self.assertRaises(IndexError) as ex:
            self.list.get(index)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

    def test_insert_valid_index_wrong_type_raises(self):
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            self.list.insert(1, "asd")

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

    def test_insert(self):
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

        result = self.list.insert(1, 100)
        self.assertIsNone(result)
        self.assertEqual([5, -3, 4, 1, 17, 2, 100], self.list._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual([5, -3, 4, 1, 17, 2], self.list._IntegerList__data)

        result = self.list.get_biggest()
        self.assertEqual(17, result)
        self.assertEqual([5, -3, 4, 1, 17, 2], self.list._IntegerList__data)

    def test_get_index(self):
        self.assertEqual([5, -3, 4, 1, 17, 2], self.list._IntegerList__data)

        result = self.list.get_index(5)
        self.assertEqual(2, result)


if __name__ == "__main__":
    main()