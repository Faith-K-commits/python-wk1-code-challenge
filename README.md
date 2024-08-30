
# Week One Code Challenge

This repository contains a collection of Python functions that perform various tasks such as mathematical operations, string manipulation, sorting, and more. The script also includes a simple `Car` class with methods to display car information.

## Table of Contents

- [Cloning the Repository](#cloning-the-repository)
- [Functions](#functions)
  - [add_numbers](#add_numbers)
  - [is_even](#is_even)
  - [reverse_string](#reverse_string)
  - [count_vowels](#count_vowels)
  - [calculate_factorial](#calculate_factorial)
  - [apply_decorator](#apply_decorator)
  - [sort_by_age](#sort_by_age)
  - [merge_dicts](#merge_dicts)
- [Class](#class)
  - [Car](#car)
  

## Cloning the Repository

To clone this repository, you can use the following command in your terminal:

```bash
git clone https://github.com/Faith-K-commits/python-wk1-code-challenge.git
````

```bash
cd python-wk1-code-challenge
```

Run the script using the following command:
```bash
python3 script.py
```

## Functions

### add_numbers

Adds two numbers and prints the result.

**Parameters:**
- `num1` (int or float): The first number.
- `num2` (int or float): The second number.

**Example:**
```python
add_numbers(5, 10)  # Output: 15
```

### is_even

Checks if a number is even and prints `True` if it is, otherwise `False`.

**Parameters:**
- `number` (int): The number to check.

**Example:**
```python
is_even(8)  # Output: True
```

### reverse_string

Reverses a given string and prints the result.

**Parameters:**
- `text` (str): The string to reverse.

**Example:**
```python
reverse_string("hello")  # Output: "olleh"
```

### count_vowels

Counts the number of vowels in a given text and prints the count.

**Parameters:**
- `text` (str): The text to analyze.

**Example:**
```python
count_vowels("TEXT")  # Output: 1
```

### calculate_factorial

Calculates the factorial of a number recursively and returns the result.

**Parameters:**
- `n` (int): The number to calculate the factorial of.

**Example:**
```python
print(calculate_factorial(5))  # Output: 120
```

### apply_decorator

A decorator function that prints "Decorator Applied" before executing the decorated function.

**Parameters:**
- `func` (function): The function to decorate.

**Example:**
```python
@apply_decorator
def my_function():
    print("Function Called")

my_function()  # Output: "Decorator Applied" followed by "Function Called"
```

### sort_by_age

Sorts a list of tuples by the second element (assumed to be age) and prints the sorted list.

**Parameters:**
- `list` (list of tuples): The list of tuples to sort.

**Example:**
```python
sort_by_age([('John', 25), ('Jane', 22), ('Dave', 31)])
# Output: [('Jane', 22), ('John', 25), ('Dave', 31)]
```

### merge_dicts

Merges two dictionaries by adding the values of common keys and prints the merged dictionary.

**Parameters:**
- `dict1` (dict): The first dictionary.
- `dict2` (dict): The second dictionary.

**Example:**
```python
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
# Output: {'a': 1, 'b': 5, 'c': 4}
```

## Class

### Car

A class to represent a car with attributes for make, model, and year.

**Attributes:**
- `make` (str): The make of the car.
- `model` (str): The model of the car.
- `year` (int): The year of the car.

**Methods:**
- `display_info()`: Prints the car's details in the format `Car Details: <year> <make> <model>`.

**Example:**
```python
volvo = Car("Volvo", "XC90", 2021)
volvo.display_info()  # Output: "Car Details: 2021 Volvo XC90"
```

## Usage

Run the script to see the functions in action. For example:

```python
add_numbers(5, 10)
is_even(8)
reverse_string("hello")
count_vowels("TEXT")
print(calculate_factorial(5))
my_function()
sort_by_age([('John', 25), ('Jane', 22), ('Dave', 31)])
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
volvo.display_info()
```

Each function will print its respective output to the console.
