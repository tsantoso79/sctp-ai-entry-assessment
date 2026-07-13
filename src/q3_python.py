# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    """Return the name as "LastName, FirstName", title-casing each part."""
    formatted_first = firstName.title()
    formatted_last = lastName.title()
    return f"{formatted_last}, {formatted_first}"


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    """Return uppercase initials like "J.S." regardless of input casing."""
    # Use only the first character from each name and normalize it to uppercase.
    # Guard against empty strings so indexing [0] can never raise IndexError.
    first_initial = firstName[0].upper() if firstName else ""
    last_initial = lastName[0].upper() if lastName else ""
    return f"{first_initial}.{last_initial}."


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

if __name__ == "__main__":
    print(formatName("Alice", "Tan"))
    print(formatName("bob", "lim"))
    print(formatInitials("Alice", "Tan"))
    print(formatInitials("bob", "lim"))
