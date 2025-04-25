import unittest
from src.calculator import validate_scores


class TestInputValidation(unittest.TestCase):
    def test_valid_scores(self):
        self.assertEqual(validate_scores("85, 90, 78"), [85, 90, 78])

    def test_scores_with_whitespace(self):
        self.assertEqual(validate_scores(" 85 , 90 ,  78 "), [85, 90, 78])

    def test_out_of_range_scores(self):
        self.assertIsNone(validate_scores("110, 90, -10"))

    def test_invalid_characters(self):
        self.assertIsNone(validate_scores("90, abc, 70"))

    def test_empty_input(self):
        self.assertIsNone(validate_scores(""))

    def test_partial_empty_between_commas(self):
        self.assertIsNone(validate_scores("85, , 90"))

    def test_single_valid_score(self):
        self.assertEqual(validate_scores("100"), [100])


if __name__ == "__main__":
    unittest.main()
