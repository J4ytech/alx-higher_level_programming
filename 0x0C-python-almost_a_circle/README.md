# 0x0C. Python - Almost a Circle

## Project Description
This project is a review of everything learned in Python up to this point, preparing for the AirBnB project. It implements a class hierarchy to represent shapes (Rectangles and Squares) using Object-Oriented Programming (OOP) concepts.

## Concepts Covered
- Import
- Exceptions
- Class and Private attributes
- Getter/Setter
- Class method and Static method
- Inheritance
- Unittest
- Read/Write file
- `*args` and `**kwargs`
- Serialization and Deserialization (JSON & CSV)

## File Structure
- `models/` - Package containing the core classes
  - `base.py` - Base class that manages the `id` attribute and handles JSON/CSV file operations
  - `rectangle.py` - Rectangle class inheriting from Base, with width, height, x, y, and area/display methods
  - `square.py` - Square class inheriting from Rectangle, using size instead of width/height
- `tests/` - Package containing all unit tests
  - `test_models/` - Package containing tests for the models

