### 🤝 Contributing

We welcome contributions of all kinds — from bug reports and fixes to feature improvements and documentation updates.

👉 To get started, please read our [Contributing Guidelines](https://github.com/CodeJam-by-CSE/Practise/blob/main/CONTRIBUTING.md).

### 🎯 Intended Behavior

This Grade Calculator project simulates a competition entry where users can input scores, compute grades, and view the remaining time until a deadline. The application includes the following core behaviors:

**Input Format:**  
Scores should be entered as comma-separated numeric values (e.g., `85, 90, 78`).

![image](https://github.com/user-attachments/assets/3e7a3100-7dd4-45bd-9880-ffa68a1dd2c3)


🧠 Core Logic

    Score Validation

        Accepts numeric scores between 0 and 100, separated by commas.

        Whitespace is ignored.

        Invalid inputs (e.g., negative numbers, non-numeric characters, or empty values) are rejected with an "Invalid input" message.

    Average and Grade Calculation

        Computes the average of all valid scores.

        Assigns a grade:

            A: 90–100

            B: 80–89

            C: 70–79

            D: 60–69

            F: Below 60

    Pass/Fail Logic

        A score of 60 or above is considered a pass.

        The is_passed() function returns True for pass scores.

⏳ Countdown Timer

    Displays the time left until a predefined competition deadline in the format:

Time Left: 1d 2h 30m 15s

If the deadline has passed, the timer displays:

    Time Left: 0d 0h 0m 0s - Competition ended

🎨 Text Color Logic (UI Feedback)

    Result text is green if the input is valid and a grade is calculated.

    Result text is red if the input is invalid.

    Countdown timer text is green if the competition is ongoing and red if it has ended.

✅ Tested Scenarios

The following behaviors are verified through unit tests:

    Correct time formatting before, during, and after the competition.

    Accurate validation of input scores (valid ranges, whitespace handling, edge cases).

    Correct color logic for result and timer messages.

    Accurate average and grade calculations for different score combinations.
