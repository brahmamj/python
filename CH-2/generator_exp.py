#Generator expressions
# A generator expression is a compact way to create a generator object in Python.
# It is similar to a list comprehension but uses parentheses instead of square brackets.
# Generator expressions are more memory efficient than list comprehensions because they generate values on the fly and do not store them in memory.
# This makes them suitable for working with large datasets or infinite sequences.
# Generator expressions are often used in conjunction with functions like sum(), min(), max(), and any() to perform operations on the generated values.
# Example of a generator expression
# The following example demonstrates how to use a generator expression to calculate the sum of squares of numbers from 1 to 10.

sumation = sum( i for i in range(1,11))
print(sumation) # Output: 55


# The ord() function in Python takes a string of a single Unicode character and returns an integer representing its Unicode code point.
welcome = "Welcome to Python"
a = tuple(ord(char) for char in welcome)
print(a) # Output: (87, 101, 108, 99, 111, 109, 101, 32, 116, 111, 32, 80, 121, 116, 104, 111, 110)
# The output is a tuple of Unicode code points for the characters in the string "welcome".