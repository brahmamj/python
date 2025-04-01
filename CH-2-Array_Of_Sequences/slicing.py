# Slicing in python is a powerful feature that allows you to extract a portion of a sequence (like a list, tuple, or string) by specifying a start and end index.
# It is a way to access a subset of elements in a sequence without modifying the original sequence.
# Slicing is done using the colon (:) operator.
# list, tuple, and string support slicing.
# The syntax for slicing is:
# sequence[start:end:step]
# The start index is inclusive, while the end index is exclusive.

list_ = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_[0:5]) # Output: [0, 1, 2, 3, 4]
print(list_[5:]) # Output: [5, 6, 7, 8, 9]
print(list_[1::2]) # Output: [1, 3, 5, 7, 9]
print(list_[::2]) # Output: [0, 2, 4, 6, 8]


# String slicing
# String slicing is similar to list slicing, but it works with strings.
# Strings are immutable, so slicing a string creates a new string.
# The syntax for string slicing is the same as for list slicing:
string_ ="Namma Benguluru"
print(string_[0:5]) # Output: Namma
print(string_[5:]) # Output: Benguluru
print(f"---Reverse--- ",string_[::-1]) # Output: urulugneB ammaN


# Tuple slicing
# Tuple slicing is also similar to list slicing, but it works with tuples.
# Tuples are immutable, so slicing a tuple creates a new tuple.
# The syntax for tuple slicing is the same as for list slicing:
tuple_ = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple_[0:5]) # Output: (0, 1, 2, 3, 4)
print(tuple_[5:]) # Output: (5, 6, 7, 8, 9) 
print(tuple_[::-1])
