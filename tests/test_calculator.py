import unittest
from src.calculator import calculate_grade, calculate_average, is_passed


class TestCalculator(unittest.TestCase):
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(85), "B")
        self.assertEqual(calculate_grade(70), "C")  # This will fail due to bug

    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)
        self.assertEqual(calculate_average([]), 0)

    def test_is_passed(self):
        self.assertTrue(is_passed(60))
        self.assertTrue(is_passed(50))  # This will fail due to bug

    def test_grade_for_average(self):
        scores = [70, 85, 90]
        avg = calculate_average(scores)
        grade = calculate_grade(avg)
        self.assertEqual(grade, "B")  # Helps detect pygame bug

    def test_average_of_three(self):
        self.assertAlmostEqual(calculate_average([80, 90, 100]), 90.0)

    def test_average_single_score(self):
        self.assertEqual(calculate_average([75]), 75.0)

    # --- calculate_grade tests ---
    def test_grade_a(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(85), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(75), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(65), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(55), "F")
