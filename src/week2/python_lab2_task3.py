
"""
Lab 3.3 – Operator Frequency Counter

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.

Instructions:
1. Ask the user for an arithmetic expression, e.g. "3 + 5 * (2 - 1) + 7 / 2".
2. Count how many times each operator occurs:
   +  -  *  /  (  )
3. Store counts in a dictionary.
4. Print the result.
"""

# Lab 3.3 – Operator Frequency Counter

# 1. Get input from the user
expression = input("Enter an arithmetic expression: ")

# 2. Define possible operators
operators = ['+', '-', '*', '/', '(', ')']

# 3. Initialize frequency dictionary
operator_counts = {op: 0 for op in operators}

# 4. Count occurrences
for char in expression:
    if char in operators:
        operator_counts[char] += 1

# 5. Print results
print("Operator counts:")
for op, count in operator_counts.items():
    print(f"  {op}: {count}")
