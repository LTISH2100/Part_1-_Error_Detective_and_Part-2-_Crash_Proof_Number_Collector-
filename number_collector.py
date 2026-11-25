""" Error Dectective Part 1
1
TypeError
String and integer concatenation
Use str()
2
TypeError
Input returns a string
Use int()
3
SyntaxError
Missing quotation mark
Close the string
4
ValueError
Invalid integer conversion
Use numeric digits
5
NameError
Undefined variable
Define the variable
"""

#"Part Two"
# Number Collector

# Collect three numbers and handle invalid input.
try:
    num1 = int(input("Enter number 1: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num1 = 0

try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num2 = 0

try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num3 = 0

# Calculate the sum and average.
total = num1 + num2 + num3
average = total / 3

# Display the results.
print(f"\nYour numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
