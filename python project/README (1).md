# 🧾 Personal Data Collector

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![GitHub Ready](https://img.shields.io/badge/GitHub-Ready-success?logo=github)

---

## 📖 Description

**Personal Data Collector** is a simple console-based Python application that collects basic personal information from a user — such as name, age, height, and favorite number — and displays it back in a clean, formatted summary.

The program also demonstrates core Python fundamentals, including how to check the **data type** of a variable using `type()` and inspect its **memory address** using `id()`. As a bonus, it calculates the user's approximate **birth year** based on the age they provide.

This project is ideal for beginners who want to understand how Python handles user input, data types, and basic arithmetic in a real, interactive script.

---

## ✨ Features

- 👋 Friendly welcome banner and goodbye message
- 📝 Collects user's **name**, **age**, **height**, and **favorite number**
- 🔎 Displays the **data type** of each collected value using `type()`
- 📍 Displays the **memory address** of each variable using `id()`
- 🎂 Calculates the user's **approximate birth year** from their age
- 🖥 Clean, structured, and readable console output with formatted borders

---

## 🛠 Technologies Used

- Python 3
- Standard Python Libraries *(no external/third-party libraries used — only built-in functions like `input()`, `int()`, `float()`, `type()`, and `id()`)*

---

## 📂 Project Structure

```text
Project/
│── py_pr_1.py
│── README.md
```

---

## 🚀 How to Run

Follow these steps to run the project on your local machine:

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
   python py_pr_1.py
   ```

---

## 📋 Example Output

```text
 ***************************************** 
|                                         |
| welcome to the Personal Data Collector! |
|                                         |
 ***************************************** 


Please enter your name: Dhyey
Please enter your age: 19
Please enter your hight(in meters): 1.74
Please enter your favorite number: 0


Thank you! Here the information we collected:


Name: Dhyey (Type: <class 'str'> , memory address: 2915248622160
Age: 19 (Type: <class 'int'> , memory address: 140704716670648
HIght: 1.74 (Type: <class 'float'> , memory address: 2915248391504
Favorite Number: 0 (Type: <class 'int'> , memory address: 140704716670040


Your birth year is approximately: 2007 (Based on your age of 19 )


 ************************************************************ 
|                                                            |
| Thank you for using the personal data collector. Good bye! |
|                                                            |
 ************************************************************ 
```

---

## 📸 Program Preview

```text
+-------------------------------------------+
|      🎉 Personal Data Collector 🎉         |
+-------------------------------------------+
| > Please enter your name: ______           |
| > Please enter your age: ______            |
| > Please enter your height (m): ______     |
| > Please enter your favorite number: ___   |
+-------------------------------------------+
|  ✅ Data collected and displayed below      |
+-------------------------------------------+
```

---

## 📚 Concepts Demonstrated

| Concept | Description |
|----------|-------------|
| 🔤 Variables | Storing user data such as name, age, height, and favorite number |
| ⌨️ User Input | Collecting input from the console using `input()` |
| 🔢 Data Types | Working with `str`, `int`, and `float` |
| 🔄 Type Conversion | Converting input strings into `int` and `float` using `int()` and `float()` |
| ➕ Arithmetic Operations | Calculating the approximate birth year using subtraction |
| 🖨 Printing Output | Displaying formatted results using `print()` |
| 📍 Memory Address using `id()` | Showing the memory location of each variable |
| 🧬 `type()` Function | Displaying the data type of each variable |
| 💻 Basic Console Application | A simple, linear, interactive command-line program |

---

## 🎯 Learning Objectives

By studying and running this project, beginners can learn:

- How to take and store different types of user input in Python
- The difference between `str`, `int`, and `float` data types
- How to convert input values into the correct data type
- How Python variables reference objects in memory via `id()`
- How to perform simple arithmetic using stored variables
- How to structure and format clean console output

---

## 🔮 Future Improvements

- ✅ Add **input validation** to handle invalid or empty entries
- 🛡 Add **exception handling** (e.g., `try`/`except`) for non-numeric input
- 💾 **Save collected data** to a file (e.g., `.txt` or `.csv`)
- 🎨 Improve the **user interface** with clearer prompts and formatting
- 🖼 Build a **GUI version** using Tkinter or another GUI library
- 🗄 Add **database support** to store multiple users' data persistently

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

Please make sure your code follows clean and readable Python practices.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it with proper attribution.

---

## 👨‍💻 Author

```
Author: Dhyey
GitHub: https://github.com/dhyeykakadiya71-dotcom/python-project
```

---

## ⭐ Support

If you found this project helpful or interesting, please consider giving it a **⭐ star** on GitHub — it helps a lot and motivates further development!
