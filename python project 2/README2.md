# 🔺 Pattern Generator & Number Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-orange)

---

## 📖 Description

**Pattern Generator & Number Analyzer** is a beginner-friendly, menu-driven Python console application. It lets the user choose from a set of options to either print a star pattern (right-angled triangle, pyramid, or left-angled triangle) or analyze a range of numbers by classifying each one as **Even** or **Odd**.

The project is a great hands-on example of using loops, nested loops, conditional statements, and user input to build an interactive command-line tool.

---

## ✨ Features

- 📐 **Right-Angled Triangle** — prints a star pattern that grows from 1 star to `row` stars
- 🔺 **Pyramid** — prints a centered pyramid pattern using spaces and stars
- 📏 **Left-Angled Triangle** — prints a mirrored (right-aligned) triangle pattern
- 🔢 **Number Range Analyzer** — loops through a user-defined range and prints whether each number is **Even** or **Odd**, then prints a running count of the numbers processed
- 📋 **Interactive Menu** — a simple numbered menu (1–4) lets the user pick which feature to run
- ⚠️ **Invalid Option Handling** — prints an "invalid choise" message if the entered option doesn't match 1–4

---

## 🛠 Technologies Used

- Python 3
- Standard Python Libraries only *(no external/third-party libraries used — built entirely with `input()`, `int()`, `for` loops, and `if`/`elif`/`else` statements)*

---

## 📂 Project Structure

```text
/
├── py_pr_2.py          # Main Python program
├── output.png          # Screenshot of the program output
└── README.md
```

---

## ⚙️ Installation Guide

No external dependencies or installation steps are required — this project runs with a standard Python 3 installation.

1. Make sure **Python 3** is installed on your machine.
2. Download or clone this repository (see below).

---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhyeykakadiya71-dotcom/python-project.git
   ```
2. **Open the project folder**
   ```bash
   cd python-project
   ```
3. **Run the Python file**
   ```bash
   python py_pr_2.py
   ```
4. **Follow the on-screen menu** and enter a number from `1` to `4` to select a feature.

---

## 🔄 Program Workflow

1. The program displays a welcome banner.
2. A menu with 4 options is shown to the user.
3. The user enters a number (`1`, `2`, `3`, or `4`) to select an option.
4. Based on the selection:
   - **Options 1–3** ask for the number of rows and print the corresponding star pattern.
   - **Option 4** asks for a start and end number, then loops through the range printing whether each number is Even or Odd, followed by a final count message.
5. If an option outside `1–4` is entered, the program prints `"invalide choise"` and ends.

---

## 📋 Example Menu Output

```text
 *************************************************************** 
|                                                               |
| Welcome to Pattern Generator and Number Analyzer! Loading.... |
|                                                               |
 *************************************************************** 

Select an Option:
1. Right-angele Triangel
2. Pyramid
3. Left-angele Triangel
4. Analyze Range of Number
Enter the Option:2
Enter the Row number of Pyramid:4
   *
  ***
 *****
*******
```

```text
Enter the Option:4
Enter the starting range:1
Enter the ending range:5
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
Sum of all numbers from 1 to 5 is: 5
```

> ℹ️ **Note:** In Option 4, the value labeled `total_sum` is incremented by `1` for every number processed rather than adding the numbers themselves — so the final message currently reports a **count** of numbers in the range, not the actual sum of their values.

---

## 📸 Screenshot

![Program Output](output.png)

---

## 📚 Learning Concepts Covered

| Concept | Description |
|----------|-------------|
| 🔤 Variables | Storing user choices, row counts, and range values |
| ⌨️ User Input | Collecting menu selections and numeric input using `input()` |
| 🔀 Conditional Statements | Using `if` / `elif` / `else` to route the program to the selected feature |
| 🔁 Nested Loops | Using loops inside loops to build triangle and pyramid patterns |
| 🔂 For Loops | Iterating over ranges to print patterns and analyze numbers |
| ⭐ Pattern Printing | Printing shapes using `*` and spaces with `end=""` formatting |
| 🔢 Number Analysis | Determining whether numbers are even or odd within a given range |

---

## 🎯 Learning Objectives

By exploring this project, beginners can learn:

- How to build a menu-driven console application using conditional logic
- How to use nested `for` loops to construct visual patterns
- How to control print formatting using the `end` parameter
- How to iterate over a numeric range and apply conditional checks
- How to structure a simple, multi-feature Python program

---

## 🔮 Future Improvements

- ✅ Add **input validation** to prevent crashes on non-numeric or invalid input
- 🛡 Add **exception handling** (`try`/`except`) for safer input handling
- 🧮 Fix the **Option 4 summary** so it correctly sums the numbers in the range instead of counting them
- 🔁 Add a **"run again" loop** so the menu redisplays after each operation instead of ending the program
- 🎨 Improve pattern options (e.g., diamond, hollow shapes, inverted pyramid)
- 🖼 Build a **GUI version** using Tkinter for a more interactive experience

---

## 🤝 Contributing

Contributions are welcome and appreciated! 🎉

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m "Add some feature"`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

Please keep contributions clean, well-commented, and beginner-friendly in spirit with the rest of the project.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it with proper attribution.

---

## 👨‍💻 Author

```
Author: Dhyey kakadiya
GitHub: https://github.com/dhyeykakadiya71-dotcom/python-project/tree/main/python%20project
```

---

## ⭐ Support

If you found this project helpful or interesting, please consider giving it a **⭐ star** on GitHub — it helps a lot and motivates further development!
