# 🧾 Personal Data Collector

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Beginner%20Project-yellow)
![GitHub Ready](https://img.shields.io/badge/GitHub-Ready-brightgreen?logo=github)

---

## 📖 Description

**Personal Data Collector** is a simple, beginner-friendly Python console application that collects basic personal information from a user — including their **name**, **age**, **height**, and **favorite number** — and displays it back to them in a neatly formatted summary.

Along with displaying the collected values, the program also demonstrates core Python concepts such as **data types**, **type conversion**, and **memory addresses** using the built-in `type()` and `id()` functions. It also performs a small calculation to estimate the user's **approximate birth year** based on their age.

This project is ideal for beginners looking to understand how user input, data types, and basic arithmetic work together in a real, interactive script.

---

## ✨ Features

- 👋 Welcomes the user with a styled console banner
- 📝 Collects user input: name, age, height, and favorite number
- 🔄 Converts input strings into appropriate data types (`int`, `float`)
- 📊 Displays the type of each collected value using `type()`
- 🧠 Displays the memory address of each variable using `id()`
- 📅 Calculates and displays the user's approximate birth year
- 🎉 Displays a friendly closing message when the program ends

---

## 🛠 Technologies Used

- **Python 3**
- Standard Python Libraries only — no external/third-party packages required

---

## 📂 Project Structure

```text
Project/
│── main.py
│── README.md
```

> Note: Replace `main.py` with the actual filename of the script if different (e.g., `py_pr_1.py`).

---

## 🚀 How to Run

Follow these simple steps to run the project on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. **Open the project folder**
   ```bash
   cd repository-name
   ```
3. **Run the Python file**
   ```bash
   python main.py
   ```

> 💡 Make sure Python 3 is installed on your system before running the script.

---

## 📋 Example Output

```text
 ***************************************** 
|                                         |
| welcome to the Personal Data Collector! |
|                                         |
 ***************************************** 


Please enter your name: Alex
Please enter your age: 25
Please enter your hight(in meters): 1.75
Please enter your favorite number: 7


Thank you! Here the information we collected:


Name: Alex (Type: <class 'str'> , memory address: 140234567891234
Age: 25 (Type: <class 'int'> , memory address: 140234567891235
HIght: 1.75 (Type: <class 'float'> , memory address: 140234567891236
Favorite Number: 7 (Type: <class 'int'> , memory address: 140234567891237


Your birth year is approximately: 2001 (Based on your age of 25 )


 ************************************************************ 
|                                                            |
| Thank you for using the personal data collector. Good bye! |
|                                                            |
 ************************************************************ 
```

> ⚠️ Memory addresses shown by `id()` will differ every time the program runs, as they depend on your system's memory allocation.

---

## 📸 Program Preview

```text
+-----------------------------------------+
|   Welcome to the Personal Data Collector |
+-----------------------------------------+
|  Name:      _______________              |
|  Age:       _______________              |
|  Height:    _______________ (m)          |
|  Fav Number:_______________              |
+-----------------------------------------+
|  >> Displays type & memory info          |
|  >> Calculates approximate birth year    |
+-----------------------------------------+
```

*(No actual screenshots are available for this console-based project — the above is a text-based visual representation.)*

---

## 📚 Concepts Demonstrated

| Concept | Used In Project |
|----------|-----------------|
| Variables | ✅ |
| User Input (`input()`) | ✅ |
| Data Types (`str`, `int`, `float`) | ✅ |
| Type Conversion (`int()`, `float()`) | ✅ |
| Arithmetic Operations | ✅ |
| Printing Output (`print()`) | ✅ |
| Memory Address using `id()` | ✅ |
| `type()` Function | ✅ |
| Basic Console Application | ✅ |

---

## 🎯 Learning Objectives

By exploring this project, beginners can learn how to:

- Collect and process user input in Python
- Convert string input into numeric data types (`int`, `float`)
- Use `type()` to inspect the data type of a variable
- Use `id()` to understand how Python stores variables in memory
- Perform simple arithmetic calculations using user data
- Structure a basic, readable console application using `print()` statements

---

## 🔮 Future Improvements

This project currently does not include input validation or error handling. Potential future improvements include:

- ✅ Input validation (e.g., preventing non-numeric input for age/height)
- ✅ Exception handling (`try`/`except`) for invalid inputs
- 💾 Saving collected data to a file (e.g., `.txt` or `.csv`)
- 🎨 Improving the console user interface/formatting
- 🖥️ Building a GUI version using `tkinter` or similar libraries
- 🗄️ Adding database support to store multiple user records

---

## 🤝 Contributing

Contributions are welcome and appreciated! 🎉

If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

Please make sure your contributions align with the beginner-friendly spirit of this project.

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this project with proper attribution.

---

## 👨‍💻 Author

```
Author: Your Name
GitHub: https://github.com/yourusername
```

---

## ⭐ Support

If you found this project helpful or interesting, please consider giving it a **star** ⭐ on GitHub — it helps others discover it too!

