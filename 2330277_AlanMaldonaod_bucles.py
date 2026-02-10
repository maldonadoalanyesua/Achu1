# ==================================================
# LOOPS (FOR / WHILE) — 6 PROBLEMS (INTERACTIVE)
# ==================================================
# Notes:
# - Variables and output messages are in English.
# - Each problem includes: Description, Inputs, Outputs, Validations, Test cases.
# ==================================================


# --------------------------------------------------
# Problem 1: Sum of integers in a range
# --------------------------------------------------
# Description:
# Calculates the sum of integers from 1 to n (inclusive) and also the sum
# of even numbers in the same range using a for loop.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
#
# Validations:
# - n must be convertible to int
# - n >= 1
#
# Test cases:
# 1) Normal: n="10"
# 2) Edge case: n="1"
# 3) Error: n="0"
def problem_1():
    n_text = input("Enter n: ").strip()

    try:
        n = int(n_text)
    except ValueError:
        print("Error: invalid input")
        return

    if n < 1:
        print("Error: invalid input")
        return

    total_sum = 0
    even_sum = 0

    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i

    print(f"Sum 1..n: {total_sum}")
    print(f"Even sum 1..n: {even_sum}")


problem_1()


# --------------------------------------------------
# Problem 2: Multiplication table with for
# --------------------------------------------------
# Description:
# Prints the multiplication table of a base number from 1 to m.
#
# Inputs:
# - base (int)
# - m (int)
#
# Outputs:
# - Lines like: "5 x 1 = 5"
#
# Validations:
# - base and m must be convertible to int
# - m >= 1
#
# Test cases:
# 1) Normal: base="5", m="4"
# 2) Edge case: base="7", m="1"
# 3) Error: base="3", m="0"
def problem_2():
    base_text = input("Enter base: ").strip()
    m_text = input("Enter m: ").strip()

    try:
        base = int(base_text)
        m = int(m_text)
    except ValueError:
        print("Error: invalid input")
        return

    if m < 1:
        print("Error: invalid input")
        return

    for i in range(1, m + 1):
        product = base * i
        print(f"{base} x {i} = {product}")


problem_2()


# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# --------------------------------------------------
# Description:
# Reads numbers until the user enters a sentinel value (-1).
# Only numbers >= 0 are accepted. Negative numbers (except -1) are rejected.
# Computes count and average of valid numbers. If no valid numbers, prints error.
#
# Inputs:
# - number (float) repeated
# - SENTINEL_VALUE = -1 (constant)
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - Or: "Error: no data"
#
# Validations:
# - Each input must be convertible to float
# - Accept only numbers >= 0 (except sentinel)
#
# Test cases:
# 1) Normal: 10, 20, 30, -1
# 2) Edge case: -1 (first input)
# 3) Error: "abc", 5, -1
def problem_3():
    SENTINEL_VALUE = -1.0

    count = 0
    total = 0.0

    while True:
        text = input("Enter a number (-1 to stop): ").strip()

        try:
            number = float(text)
        except ValueError:
            print("Error: invalid input")
            continue

        if number == SENTINEL_VALUE:
            break

        if number < 0:
            print("Error: invalid input")
            continue

        total += number
        count += 1

    if count == 0:
        print("Error: no data")
        return

    average_value = total / count
    print(f"Count: {count}")
    print(f"Average: {average_value}")


problem_3()


# --------------------------------------------------
# Problem 4: Password attempts with while
# --------------------------------------------------
# Description:
# Simple password attempt system. User has MAX_ATTEMPTS tries to enter the correct password.
# If correct, prints "Login success"; otherwise prints "Account locked".
#
# Inputs:
# - user_password (string) repeated
#
# Outputs:
# - "Login success" or "Account locked"
#
# Validations:
# - MAX_ATTEMPTS > 0 (constant in code)
#
# Test cases:
# 1) Normal: correct on first try
# 2) Edge case: correct on last try
# 3) Error: always wrong -> locked
def problem_4():
    CORRECT_PASSWORD = "admin123"
    MAX_ATTEMPTS = 3

    if MAX_ATTEMPTS <= 0:
        print("Error: invalid input")
        return

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_password = input("Enter password: ")
        if user_password == CORRECT_PASSWORD:
            print("Login success")
            return
        attempts += 1

    print("Account locked")


problem_4()


# --------------------------------------------------
# Problem 5: Simple menu with while
# --------------------------------------------------
# Description:
# Repeats a text menu until the user selects 0 to exit.
# It supports greeting, showing a counter, and incrementing the counter.
#
# Inputs:
# - option (string/int) repeated
#
# Outputs:
# - "Hello!"
# - "Counter: <value>"
# - "Counter incremented"
# - "Bye!"
# - "Error: invalid option"
#
# Validations:
# - option must be convertible to int
# - accepted options: 0, 1, 2, 3
#
# Test cases:
# 1) Normal: 1, 3, 2, 0
# 2) Edge case: 0 (exit immediately)
# 3) Error: "x", 9, 0
def problem_5():
    counter = 0
    option = -1

    while option != 0:
        print("\n1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")

        option_text = input("Choose an option: ").strip()

        try:
            option = int(option_text)
        except ValueError:
            print("Error: invalid option")
            continue

        if option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
        else:
            print("Error: invalid option")


problem_5()


# --------------------------------------------------
# Problem 6: Pattern printing with nested loops
# --------------------------------------------------
# Description:
# Prints a right triangle pattern of '*' using nested for loops.
# Also prints an inverted pattern (optional extension included).
#
# Inputs:
# - n (int)
#
# Outputs:
# - Lines of '*' increasing from 1 to n
# - Optional inverted triangle from n to 1
#
# Validations:
# - n must be convertible to int
# - n >= 1
#
# Test cases:
# 1) Normal: n="4"
# 2) Edge case: n="1"
# 3) Error: n="0"
def problem_6():
    n_text = input("Enter number of rows: ").strip()

    try:
        n = int(n_text)
    except ValueError:
        print("Error: invalid input")
        return

    if n < 1:
        print("Error: invalid input")
        return

    # Increasing pattern
    for i in range(1, n + 1):
        line = ""
        for j in range(i):
            line += "*"
        print(line)

    # Optional inverted pattern
    for i in range(n, 0, -1):
        line = ""
        for j in range(i):
            line += "*"
        print(line)


problem_6()
