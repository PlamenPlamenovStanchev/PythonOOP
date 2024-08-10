from PythonOOP.unit_testing.worker import Worker


from unittest import TestCase, main


class TestWorker(TestCase):
    def test_init_worker(self):

        w = Worker("Plamen", 1800, 100)

        self.assertEqual("Plamen", w.name)
        self.assertEqual(1800, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

    def test_work_worker_does_not_have_energy_raises(self):

        w = Worker("Plamen", 1800, 0)
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        w = Worker("Plamen", 1800, -1)
        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)

    def test_worker_works(self):
        w = Worker("Plamen", 1800, 100)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

        w.work()

        self.assertEqual(99, w.energy)
        self.assertEqual(1000, w.money)

        w.work()

        self.assertEqual(98, w.energy)
        self.assertEqual(2000, w.money)

    def test_rest_worker_energy_increases(self):
        w = Worker("Plamen", 1800, 100)
        self.assertEqual(100, w.energy)

        w.rest()

        self.assertEqual(101, w.energy)

    def test_get_info(self):
        w = Worker("Plamen", 1800, 100)

        result = w.get_info()
        expected = "Plamen has saved 0 money"

        self.assertEqual(expected, result)

        w.work()
        self.assertEqual(w.salary, w.money)

        result = w.get_info()
        expected = "Plamen has saved 1800 money"

        self.assertEqual(expected, result)


if  __name__ == '__main__':
    main()
