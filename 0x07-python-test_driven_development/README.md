# 0x07. Python - Test-driven Development

## Description
This project focuses on the practice of **Test-Driven Development (TDD)** in Python. The goal is to write requirements and edge-case tests before implementing the actual logic. By using the `doctest` and `unittest` modules, we ensure that our functions are robust, well-documented, and handle errors gracefully.

## Learning Objectives
* The importance of unit testing in software development.
* How to write effective docstrings for Python modules and functions.
* How to use the `doctest` module for interactive documentation testing.
* How to use the `unittest` framework for comprehensive unit tests.
* Handling exceptions and validating input data types.

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`.
* All files will be interpreted/compiled on **Ubuntu 20.04 LTS**.
* All files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file at the root of the project folder is mandatory.
* Your code should follow the **Pycodestyle** guidelines.
* All modules, classes, and functions must have documentation.

### Testing
* All test files should be placed in a folder named `tests`.
* Doctest files should be text files with the `.txt` extension.
* Tests are executed using the `doctest` or `unittest` modules.

## Tasks

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Integers addition** | `0-add_integer.py` | Function that adds two integers with type validation. |
| **1. Divide a matrix** | `2-matrix_divided.py` | Function that divides all elements of a matrix. |
| **2. Say my name** | `3-say_my_name.py` | Function that prints a formatted name string. |
| **3. Print square** | `4-print_square.py` | Function that prints a square using the `#` character. |
| **4. Text indentation** | `5-text_indentation.py` | Function that formats text based on specific characters. |
| **5. Max integer** | `tests/6-max_integer_test.py` | Writing unit tests for a specific function using `unittest`. |

## How to Run Tests
To run a doctest:
```bash
python3 -m doctest -v tests/FILENAME.txt