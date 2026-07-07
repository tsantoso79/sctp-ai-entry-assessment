# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):
    if unit == "C":
        # Celsius to Fahrenheit.
        result = (value * 9 / 5) + 32
    elif unit == "F":
        # Fahrenheit to Celsius.
        result = (value - 32) * 5 / 9
    else:
        return -1

    return round(result, 2)


# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

if __name__ == "__main__":
    print(convertTemp(100, "C"))
    print(convertTemp(32, "F"))
    print(convertTemp(37, "C"))
    print(convertTemp("invalid", "X"))
