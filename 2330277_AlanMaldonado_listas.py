# --------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# --------------------------------------------------
# Description:
# Parses an initial items string like "apple:2,banana:5", builds a list of item names,
# allows adding a new item, and checks if a search item exists (case-insensitive).
#
# Inputs:
# - initial_items_text (string; e.g., "apple:2,banana:5,orange:6")
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" True/False
#
# Validations:
# - initial_items_text not empty after strip()
# - new_item and search_item not empty after strip()
#
# Test cases:
# 1) Normal: initial="apple:2,banana:5,orange:6", new="mango", search="banana"
# 2) Edge case: initial="  apple:2  ,  banana:5  ", new="APPLE", search="apple"
# 3) Error: initial="   " (only spaces)
def problem_1():
    initial_items_text = input("Enter initial items (e.g., apple:2,banana:5): ").strip()
    if initial_items_text == "":
        print("Error: invalid input")
        return

    parts = initial_items_text.split(",")
    items_list = []

    for p in parts:
        p_clean = p.strip()
        if p_clean == "":
            continue

        if ":" in p_clean:
            name_part = p_clean.split(":")[0].strip().lower()
        else:
            name_part = p_clean.strip().lower()

        if name_part != "":
            items_list.append(name_part)

    new_item = input("Enter new item: ").strip().lower()
    search_item = input("Enter search item: ").strip().lower()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
        return

    items_list.append(new_item)

    is_in_list = (search_item in items_list)

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {is_in_list}")


problem_1()


# --------------------------------------------------
# Problem 2: Points and distances with tuples
# --------------------------------------------------
# Description:
# Reads 4 numbers to create two 2D points as tuples, calculates the Euclidean distance,
# and creates a midpoint tuple.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
#
# Validations:
# - All inputs must be convertible to float
#
# Test cases:
# 1) Normal: (0,0) and (3,4)
# 2) Edge case: (-1.5,2.5) and (-1.5,2.5)
# 3) Error: x1="a"
def problem_2():
    x1_text = input("Enter x1: ").strip()
    y1_text = input("Enter y1: ").strip()
    x2_text = input("Enter x2: ").strip()
    y2_text = input("Enter y2: ").strip()

    try:
        x1 = float(x1_text)
        y1 = float(y1_text)
        x2 = float(x2_text)
        y2 = float(y2_text)
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")


problem_2()


# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# --------------------------------------------------
# Description:
# Uses a dictionary of product prices. Reads a product name and quantity,
# then prints unit price and total if product exists.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - If found: "Unit price:", "Quantity:", "Total:"
# - If not found: "Error: product not found"
#
# Validations:
# - product_name not empty after strip()
# - quantity > 0
# - product_name must exist in dictionary
#
# Test cases:
# 1) Normal: product="apple", qty=3
# 2) Edge case: product="APPLE", qty=1
# 3) Error: product="carrot", qty=2
def problem_3():
    product_prices = {"apple": 10.0, "banana": 5.0, "orange": 8.0}

    product_name = input("Enter product name: ").strip().lower()
    quantity_text = input("Enter quantity: ").strip()

    if product_name == "":
        print("Error: invalid input")
        return

    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Error: invalid input")
        return

    if quantity <= 0:
        print("Error: invalid input")
        return

    if product_name not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price}")


problem_3()


# --------------------------------------------------
# Problem 4: Student grades with dict and list
# --------------------------------------------------
# Description:
# Stores student grades in a dictionary where each value is a list of floats.
# Reads a student name, prints grades, average, and passed flag (average >= 70).
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - If found: "Grades:", "Average:", "Passed:"
# - If not found: "Error: student not found"
#
# Validations:
# - student_name not empty after strip()
# - student must exist in dictionary
# - grades list must not be empty
#
# Test cases:
# 1) Normal: student="Alice"
# 2) Edge case: student="bob" (case-insensitive match if stored lower)
# 3) Error: student="Unknown"
def problem_4():
    grades = {
        "alice": [90.0, 85.0, 78.0],
        "bob": [70.0, 72.0, 68.0],
        "carol": [100.0, 95.0, 92.0]
    }

    student_name = input("Enter student name: ").strip().lower()
    if student_name == "":
        print("Error: invalid input")
        return

    if student_name not in grades:
        print("Error: student not found")
        return

    grades_list = grades[student_name]
    if len(grades_list) == 0:
        print("Error: invalid input")
        return

    average = sum(grades_list) / len(grades_list)
    is_passed = (average >= 70.0)

    print(f"Grades: {grades_list}")
    print(f"Average: {average}")
    print(f"Passed: {is_passed}")


problem_4()


# --------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# --------------------------------------------------
# Description:
# Reads a sentence, removes basic punctuation, converts to lowercase, splits into words,
# builds a frequency dictionary, and prints the most common word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>
#
# Validations:
# - sentence not empty after strip()
# - words list must not be empty
#
# Test cases:
# 1) Normal: "Hello, hello world!"
# 2) Edge case: "Test." (single word)
# 3) Error: "   "
def problem_5():
    sentence = input("Enter a sentence: ").strip()
    if sentence == "":
        print("Error: invalid input")
        return

    for ch in ".,!?;:":
        sentence = sentence.replace(ch, "")

    words_list = sentence.lower().split()
    if len(words_list) == 0:
        print("Error: invalid input")
        return

    freq_dict = {}
    for w in words_list:
        freq_dict[w] = freq_dict.get(w, 0) + 1

    most_common_word = words_list[0]
    for w in freq_dict:
        if freq_dict[w] > freq_dict[most_common_word]:
            most_common_word = w

    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


problem_5()


# --------------------------------------------------
# Problem 6: Simple address book (dictionary CRUD)
# --------------------------------------------------
# Description:
# Implements a mini address book with a dictionary (CRUD):
# - ADD: saves/updates a contact
# - SEARCH: finds a contact
# - DELETE: removes a contact
#
# Inputs:
# - action_text ("ADD", "SEARCH", "DELETE")
# - name (string)
# - phone (string, only for ADD)
#
# Outputs:
# - ADD: "Contact saved: <name> <phone>"
# - SEARCH: "Phone: <phone>" or "Error: contact not found"
# - DELETE: "Contact deleted: <name>" or "Error: contact not found"
#
# Validations:
# - action_text must be one of ADD/SEARCH/DELETE (case-insensitive)
# - name not empty after strip()
# - phone not empty for ADD
#
# Test cases:
# 1) Normal: action="ADD", name="Alice", phone="123"
# 2) Edge case: action="SEARCH", name=" alice " (spaces + case)
# 3) Error: action="DELETE", name="Unknown"
def problem_6():
    contacts = {"alice": "1234567890", "bob": "5550001111", "carol": "7778889999"}

    action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
    if action_text not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid input")
        return

    name = input("Enter name: ").strip().lower()
    if name == "":
        print("Error: invalid input")
        return

    if action_text == "ADD":
        phone = input("Enter phone: ").strip()
        if phone == "":
            print("Error: invalid input")
            return
        contacts[name] = phone
        print(f"Contact saved: {name} {phone}")

    elif action_text == "SEARCH":
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")


problem_6()
