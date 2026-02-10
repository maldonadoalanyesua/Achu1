# ==================================================
# FUNCTIONS (DEF / PARAMETERS / RETURN) — 6 PROBLEMS (INTERACTIVE)
# ==================================================
# Notes:
# - Function names, variables, constants, and outputs are in English.
# - Comments can be in Spanish, but outputs must be in English.
# - Each problem includes: Description, Inputs, Outputs, Validations, Test cases.
# ==================================================


# --------------------------------------------------
# Problem 1: Rectangle area and perimeter (basic functions)
# --------------------------------------------------
# Description:
# Defines two functions to calculate area and perimeter of a rectangle.
# The main code validates inputs before calling the functions.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
#
# Validations:
# - width > 0
# - height > 0
#
# Test cases:
# 1) Normal: width="5", height="3"
# 2) Edge case: width="0.1", height="0.1"
# 3) Error: width="0", height="4"
def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def problem_1():
    width_text = input("Enter width: ").strip()
    height_text = input("Enter height: ").strip()

    try:
        width = float(width_text)
        height = float(height_text)
    except ValueError:
        print("Error: invalid input")
        return

    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return

    area_value = calculate_area(width, height)
    perimeter_value = calculate_perimeter(width, height)

    print(f"Area: {area_value}")
    print(f"Perimeter: {perimeter_value}")


problem_1()


# --------------------------------------------------
# Problem 2: Grade classifier (function with return string)
# --------------------------------------------------
# Description:
# Defines a function classify_grade(score) that returns a letter grade A-F
# based on score ranges (0 to 100).
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
#
# Test cases:
# 1) Normal: score="92"
# 2) Edge case: score="60"
# 3) Error: score="120"
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def problem_2():
    score_text = input("Enter score (0-100): ").strip()

    try:
        score = float(score_text)
    except ValueError:
        print("Error: invalid input")
        return

    if score < 0 or score > 100:
        print("Error: invalid input")
        return

    grade_letter = classify_grade(score)
    print(f"Score: {score}")
    print(f"Category: {grade_letter}")


problem_2()


# --------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# --------------------------------------------------
# Description:
# Defines summarize_numbers(numbers_list) that returns a dictionary with
# min, max, and average values. Main code parses a comma-separated string.
#
# Inputs:
# - numbers_text (string; e.g., "10,20,30")
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
#
# Validations:
# - numbers_text not empty after strip()
# - list not empty after conversion
# - all elements must be convertible to float
#
# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge case: "5"
# 3) Error: "10,a,30"
def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


def problem_3():
    numbers_text = input("Enter numbers separated by commas: ").strip()
    if numbers_text == "":
        print("Error: invalid input")
        return

    parts = numbers_text.split(",")
    numbers_list = []

    for p in parts:
        p_clean = p.strip()
        if p_clean == "":
            print("Error: invalid input")
            return
        try:
            numbers_list.append(float(p_clean))
        except ValueError:
            print("Error: invalid input")
            return

    if len(numbers_list) == 0:
        print("Error: invalid input")
        return

    summary = summarize_numbers(numbers_list)

    print(f"Min: {summary['min']}")
    print(f"Max: {summary['max']}")
    print(f"Average: {summary['average']}")


problem_3()


# --------------------------------------------------
# Problem 4: Apply discount list (pure function)
# --------------------------------------------------
# Description:
# Defines apply_discount(prices_list, discount_rate) that returns a new list
# with discounted prices. The original list must not be modified.
#
# Inputs:
# - prices_text (string; e.g., "100,200,300")
# - discount_rate (float; 0 to 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - prices_text not empty and list not empty
# - each price > 0
# - 0 <= discount_rate <= 1
#
# Test cases:
# 1) Normal: prices="100,200,300", rate="0.10"
# 2) Edge case: prices="50", rate="0"
# 3) Error: prices="100,-5,200", rate="0.2"
def apply_discount(prices_list, discount_rate):
    discounted_list = []
    for price in prices_list:
        discounted_list.append(price * (1 - discount_rate))
    return discounted_list


def problem_4():
    prices_text = input("Enter prices separated by commas: ").strip()
    rate_text = input("Enter discount rate (0 to 1): ").strip()

    if prices_text == "":
        print("Error: invalid input")
        return

    try:
        discount_rate = float(rate_text)
    except ValueError:
        print("Error: invalid input")
        return

    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
        return

    parts = prices_text.split(",")
    prices_list = []

    for p in parts:
        p_clean = p.strip()
        if p_clean == "":
            print("Error: invalid input")
            return
        try:
            price_value = float(p_clean)
        except ValueError:
            print("Error: invalid input")
            return
        if price_value <= 0:
            print("Error: invalid input")
            return
        prices_list.append(price_value)

    if len(prices_list) == 0:
        print("Error: invalid input")
        return

    discounted_list = apply_discount(prices_list, discount_rate)

    print(f"Original prices: {prices_list}")
    print(f"Discounted prices: {discounted_list}")


problem_4()


# --------------------------------------------------
# Problem 5: Greeting function with default parameters
# --------------------------------------------------
# Description:
# Defines greet(name, title="") that returns: "Hello, <full_name>!"
# Demonstrates positional and named arguments.
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name not empty after strip()
#
# Test cases:
# 1) Normal: name="Alice", title="Dr."
# 2) Edge case: name="Bob", title=""
# 3) Error: name="   "
def greet(name, title=""):
    name_clean = name.strip()
    title_clean = title.strip()

    if title_clean != "":
        full_name = f"{title_clean} {name_clean}"
    else:
        full_name = name_clean

    return f"Hello, {full_name}!"


def problem_5():
    name = input("Enter name: ")
    title = input("Enter title (optional): ")

    if name.strip() == "":
        print("Error: invalid input")
        return

    greeting_positional = greet(name, title)
    greeting_named = greet(name=name, title=title)

    print(f"Greeting: {greeting_positional}")
    print(f"Greeting: {greeting_named}")


problem_5()


# --------------------------------------------------
# Problem 6: Factorial function (iterative)
# --------------------------------------------------
# Description:
# Defines factorial(n) using an iterative for loop and returns n!.
# Main code validates n and prints the result.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be convertible to int
# - n >= 0
# - optional limit: n <= 20
#
# Test cases:
# 1) Normal: n="5"
# 2) Edge case: n="0"
# 3) Error: n="-1"
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def problem_6():
    n_text = input("Enter n: ").strip()

    try:
        n = int(n_text)
    except ValueError:
        print("Error: invalid input")
        return

    if n < 0 or n > 20:
        print("Error: invalid input")
        return

    factorial_value = factorial(n)

    print(f"n: {n}")
    print(f"Factorial: {factorial_value}")


problem_6()
