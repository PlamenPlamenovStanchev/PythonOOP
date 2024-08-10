import unittest

from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student_1 = Student("Plamen", {"Python": ["n1", "n2", "n3"], "QA": ["n1", "n2"]})
        self.student_2 = Student("Ivaylo")

    def test_init_with_courses(self):
        self.assertEqual("Plamen", self.student_1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"], "QA": ["n1", "n2"]}, self.student_1.courses)
        self.assertIsInstance(self.student_1.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual("Ivaylo", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)
        self.assertIsInstance(self.student_2.courses, dict)

    def test_enroll_in_existing_course(self):
        result = self.student_1.enroll("Python", ["n4", "n5"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5"], "QA": ["n1", "n2"]},
                         self.student_1.courses)
        result = self.student_1.enroll("Python", ["n6", "n7"], "N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5", "n6", "n7"], "QA": ["n1", "n2"]},
                         self.student_1.courses)

    def test_enroll_in_not_exiting_course_with_y(self):
        result = self.student_1.enroll("JS", ["n1", "n2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student_1.courses["JS"])
        self.assertIn("JS", self.student_1.courses)

    def test_enroll_in_not_exiting_course_with_empty_string(self):
        result = self.student_1.enroll("JS", ["n1", "n2"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student_1.courses["JS"])
        self.assertIn("JS", self.student_1.courses)

    def test_enroll_in_not_exiting_course_not_adding_notes(self):
        result = self.student_2.enroll("Digital marketing", ["n1", "n2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_2.courses["Digital marketing"])
        self.assertTrue("Digital marketing", self.student_2.courses)

    def test_add_notes_to_existing_course(self):
        self.student_2.enroll("Digital marketing", ["n1", "n2"])
        result = self.student_2.add_notes("Digital marketing", "n3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2", "n3"], self.student_2.courses["Digital marketing"])

    def test_add_notes_to_not_exiting_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("C#", ["n1", "n2"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_existing_course(self):
        result = self.student_1.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn('Python', self.student_1.courses)

    def test_leaving_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Java Advanced")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()