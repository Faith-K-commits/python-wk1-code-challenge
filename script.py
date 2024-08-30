def add_numbers(num1, num2):
    print (num1 + num2)

def is_even(number):
    print (number % 2 == 0)

def reverse_string(text):
    # slice list from end to start
    print (text[::-1])

def count_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    # Split text into an array of characters
    array_text = list(text)
    # Convert all characters to lowercase
    array_text = [char.lower() for char in array_text]
    for char in array_text:
        if char in vowels:
            count += 1
    print (count)

def calculate_factorial(n):
    return 1 if n == 0 else n * calculate_factorial(n - 1)

def apply_decorator(func):
    def decorator_func():
        print("Decorator Applied")
        func()
    return decorator_func

@apply_decorator
def my_function():
    print("Function Called")

def sort_by_age(list):
    list.sort(key=lambda x: x[1])
    print(list)


def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        if key in dict2:
            merged_dict[key] = dict1[key] + dict2[key]
        else:
            merged_dict[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            merged_dict[key] = dict2[key]
    print(merged_dict)
    return


# define car class with make, model and year attributes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # define a method to print car information
    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")


add_numbers(5, 10)
is_even(8)
reverse_string("hello")
count_vowels("TEXT")
print(calculate_factorial(5))
my_function()
sort_by_age([('John', 25), ('Jane', 22), ('Dave', 31)])
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
volvo = Car("Volvo", "XC90", 2021)
volvo.display_info()

