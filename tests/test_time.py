import unittest
from datetime import datetime, timedelta
from calculator import time_left_until_competition


class TestTimeLeftUntilCompetition(unittest.TestCase):

    def test_time_left_in_future(self):
        # Set competition end time to 1 day, 2 hours, and 30 minutes from now
        future_time = datetime.now() + timedelta(days=1, hours=2, minutes=30)

        # Get the time left until competition ends
        time_left_text = time_left_until_competition(future_time)

        # Check if the time left is in the expected format
        self.assertIn("Time Left", time_left_text)
        self.assertIn("1d", time_left_text)
        self.assertIn("2h", time_left_text)
        self.assertIn("30m", time_left_text)
        self.assertIn("s", time_left_text)  # Seconds should be part of the text

    def test_time_left_now(self):
        # Set the competition end time to exactly now
        current_time = datetime.now()

        # Get the time left until competition ends
        time_left_text = time_left_until_competition(current_time)

        # Check if the time left text indicates the competition has ended or zero time left
        self.assertIn("Time Left", time_left_text)
        self.assertIn("0d", time_left_text)
        self.assertIn("0h", time_left_text)
        self.assertIn("0m", time_left_text)

    def test_time_left_in_past(self):
        # Set competition end time to 1 day in the past
        past_time = datetime.now() - timedelta(days=1)

        # Get the time left until competition ends (should show past competition)
        time_left_text = time_left_until_competition(past_time)

        # Check if the time left text indicates that the competition has passed
        self.assertIn("Time Left", time_left_text)
        self.assertIn("0d", time_left_text)  # Should show 0 days left
        self.assertIn("0h", time_left_text)
        self.assertIn("0m", time_left_text)
        self.assertIn(
            "Competition ended", time_left_text
        )  # You could return a message like this if the time has passed

    def test_time_left_exact_minutes(self):
        # Set competition end time to exactly 5 minutes from now
        future_time = datetime.now() + timedelta(minutes=5)

        # Get the time left until competition ends
        time_left_text = time_left_until_competition(future_time)

        # Check if the time left text contains exactly 5 minutes
        self.assertIn("Time Left", time_left_text)
        self.assertIn("0d", time_left_text)  # Should show 0 days
        self.assertIn("0h", time_left_text)  # Should show 0 hours
        self.assertIn("5m", time_left_text)  # Should show 5 minutes


if __name__ == "__main__":
    unittest.main()
