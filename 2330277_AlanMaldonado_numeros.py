# ==================================================
# NUMBERS + BOOLEANS — 6 PROBLEMS (INTERACTIVE)
# ==================================================
# Notes:
# - Variables and output messages are in English.
# - Each problem includes: Description, Inputs, Outputs, Validations, Test cases.
# ==================================================


# --------------------------------------------------
# Problem 1: Temperature converter and range flag
# --------------------------------------------------
# Description:
# Converts a temperature from Celsius to Fahrenheit and Kelvin.
# Also sets a boolean flag is_high_temperature (temp_c >= 30.0).
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" True/False
#
# Validations:
# - temp_c must be convertible to float
# - temp_c must be >= -273.15
#
# Test cases:
# 1) Normal: "30"
# 2) Edge case: "-273.15"
# 3) Error: "-300"
def problem_1():
    temp_text = input("Enter temperature in Celsius: ").strip()

    try:
        temp_c = float(temp_text)
    except ValueError:
        print("Error: invalid input")
        return

    if temp_c < -273.15:
        print("Error: invalid input")
        return

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    is_high_temperature = (temp_c >= 30.0)

    print(f"Fahrenheit: {temp_f}")
    print(f"Kelvin: {temp_k}")
    print(f"High temperature: {is_high_temperature}")


problem_1()


# --------------------------------------------------
# Problem 2: Work hours and overtime payment
# --------------------------------------------------
# Description:
# Calculates weekly pay. Up to 40 hours at hourly_rate.
# Overtime hours (>40) paid at 1.5x. Also sets has_overtime flag.
#
# Inputs:
# - hours_worked (int)
# - hourly_rate (float)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" True/False
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: hours="45", rate="100"
# 2) Edge case: hours="40", rate="1"
# 3) Error: hours="-1", rate="50"
def problem_2():
    hours_text = input("Enter hours worked: ").strip()
    rate_text = input("Enter hourly rate: ").strip()

    try:
        hours_worked = int(hours_text)
        hourly_rate = float(rate_text)
    except ValueError:
        print("Error: invalid input")
        return

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return

    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    has_overtime = (hours_worked > 40)

    print(f"Regular pay: {regular_pay}")
    print(f"Overtime pay: {overtime_pay}")
    print(f"Total pay: {total_pay}")
    print(f"Has overtime: {has_overtime}")


problem_2()


# --------------------------------------------------
# Problem 3: Discount eligibility with booleans
# --------------------------------------------------
# Description:
# Eligible if is_student OR is_senior OR purchase_total >= 1000.0.
# Applies 10% discount if eligible.
#
# Inputs:
# - purchase_total (float)
# - is_student_text ("YES"/"NO")
# - is_senior_text ("YES"/"NO")
#
# Outputs:
# - "Discount eligible:" True/False
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0
# - is_student_text and is_senior_text must be YES or NO
#
# Test cases:
# 1) Normal: total="1200", student="NO", senior="NO"
# 2) Edge case: total="0", student="YES", senior="NO"
# 3) Error: total="100", student="MAYBE", senior="NO"
def problem_3():
    total_text = input("Enter purchase total: ").strip()
    is_student_text = input("Is student (YES/NO): ").strip().upper()
    is_senior_text = input("Is senior (YES/NO): ").strip().upper()

    try:
        purchase_total = float(total_text)
    except ValueError:
        print("Error: invalid input")
        return

    if purchase_total < 0:
        print("Error: invalid input")
        return

    if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
        return

    is_student = (is_student_text == "YES")
    is_senior = (is_senior_text == "YES")

    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total

    print(f"Discount eligible: {discount_eligible}")
    print(f"Final total: {final_total}")


problem_3()


# --------------------------------------------------
# Problem 4: Basic statistics of three integers
# --------------------------------------------------
# Description:
# Reads three integers and prints sum, average, max, min,
# and a boolean flag all_even (all numbers are even).
#
# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" True/False
#
# Validations:
# - All inputs must be convertible to int
#
# Test cases:
# 1) Normal: "2", "4", "6"
# 2) Edge case: "-1", "0", "1"
# 3) Error: "a", "2", "3"
def problem_4():
    n1_text = input("Enter n1: ").strip()
    n2_text = input("Enter n2: ").strip()
    n3_text = input("Enter n3: ").strip()

    try:
        n1 = int(n1_text)
        n2 = int(n2_text)
        n3 = int(n3_text)
    except ValueError:
        print("Error: invalid input")
        return

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")


problem_4()


# --------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# --------------------------------------------------
# Description:
# Computes debt_ratio = monthly_debt / monthly_income
# Eligible if monthly_income >= 8000.0 AND debt_ratio <= 0.4 AND credit_score >= 650.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" True/False
#
# Validations:
# - monthly_income > 0.0
# - monthly_debt >= 0.0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: income="10000", debt="2000", score="700"
# 2) Edge case: income="8000", debt="3200", score="650"
# 3) Error: income="0", debt="100", score="700"
def problem_5():
    income_text = input("Enter monthly income: ").strip()
    debt_text = input("Enter monthly debt: ").strip()
    score_text = input("Enter credit score: ").strip()

    try:
        monthly_income = float(income_text)
        monthly_debt = float(debt_text)
        credit_score = int(score_text)
    except ValueError:
        print("Error: invalid input")
        return

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
        return

    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

    print(f"Debt ratio: {debt_ratio}")
    print(f"Eligible: {eligible}")


problem_5()


# --------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# --------------------------------------------------
# Description:
# Calculates BMI and prints category flags:
# - is_underweight (bmi < 18.5)
# - is_normal (18.5 <= bmi < 25.0)
# - is_overweight (bmi >= 25.0)
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - "BMI:" <rounded_bmi>
# - "Underweight:" True/False
# - "Normal:" True/False
# - "Overweight:" True/False
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
#
# Test cases:
# 1) Normal: weight="70", height="1.75"
# 2) Edge case: weight="50", height="1.65"
# 3) Error: weight="0", height="1.75"
def problem_6():
    weight_text = input("Enter weight (kg): ").strip()
    height_text = input("Enter height (m): ").strip()

    try:
        weight_kg = float(weight_text)
        height_m = float(height_text)
    except ValueError:
        print("Error: invalid input")
        return

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
        return

    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)

    is_underweight = (bmi < 18.5)
    is_normal = (bmi >= 18.5) and (bmi < 25.0)
    is_overweight = (bmi >= 25.0)

    print(f"BMI: {bmi_rounded}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight}")


problem_6()
