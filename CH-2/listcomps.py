import collections
#list comprehension
# list comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

list = [x for x in range(10)]
print(list)

Person = collections.namedtuple('Person',['name','age','gender'])

names =["Alice","Bob","Charlie","David"]
ages = [25,30,35,40]
genders = ["F","M","M","M"]

personList = [Person(name,age,gender) for name in names for age in ages for gender in genders]
print(personList)

#Cartesian product of two lists
# The Cartesian product of two lists is the set of all possible ordered pairs (a,b) where a is from the first list and b is from the second list.
# In Python, you can use list comprehension to generate the Cartesian product of two lists.
colors = ['red', 'green']
sizes = ['S', 'M', 'L']

cartesian_product = [(color, size) for color in colors for size in sizes]
print(cartesian_product)

# ord() function
# The ord() function in Python takes a string of a single Unicode character and returns an integer representing its Unicode code point.
# The Unicode code point is a unique number assigned to each character in the Unicode standard.
# The ord() function is useful when you want to convert a character to its corresponding integer value.
# For example, the Unicode code point for 'A' is 65, so ord('A') returns 65.
# Similarly, ord('a') returns 97, which is the code point for lowercase 'a'.
# The ord() function is often used in string manipulation, cryptography, and encoding tasks.
# It can also be used to compare characters based on their Unicode values.
# In Python, the ord() function is built-in and can be used directly without any import statements.
# Example usage of ord() function   

print(ord('A'))  # Output: 65
special= "$%@*&"
ord_list = [ord(char) for char in special]
print(ord_list)  # Output: [36, 37, 64, 42, 38]
# The output is a list of Unicode code points for the characters in the string "special".

