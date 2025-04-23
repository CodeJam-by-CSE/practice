import unittest
from datetime import datetime, timedelta
from calculator import time_left_until_competition
from src.calculator import get_result_text_color, get_time_left_text_color


class TestTextColorLogic(unittest.TestCase):

    def test_valid_result_text_color(self):
        self.assertEqual(get_result_text_color("Average: 85.00, Grade: A"), "green")

    def test_invalid_result_text_color(self):
        self.assertEqual(get_result_text_color("Invalid input"), "red")

    def test_competition_ended_time_color(self):
        past_time = datetime.now() - timedelta(days=1)
        time_text = time_left_until_competition(past_time)
        self.assertEqual(get_time_left_text_color(time_text), "red")

    def test_competition_ongoing_time_color(self):
        future_time = datetime.now() + timedelta(days=1)
        time_text = time_left_until_competition(future_time)
        self.assertEqual(get_time_left_text_color(time_text), "green")


if __name__ == "__main__":
    unittest.main()
