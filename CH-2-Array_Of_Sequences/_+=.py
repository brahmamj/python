# += and +* expression
# 1. The `+=` operator is used to add a value to a variable and assign the result back to that variable.
# 2. The `+=` operator modifies the original variable in place, while the `+` operator creates a new object.
# 3. The `+=` operator is more efficient than the `+` operator because it does not create a new object.
# 4. The `+=` operator can be used with mutable objects (like lists) to modify them in place, while the `+` operator creates a new object.
# 5. The `+=` operator can be used with immutable objects (like strings and tuples) to create a new object.
# 6. The `+=` operator can be used with numbers to add them together and assign the result back to the variable.
# 7. The `+=` operator can be used with strings to concatenate them and assign the result back to the variable.
# 8. The `+=` operator can be used with lists to append elements to the list and assign the result back to the variable.
# 9. The `+=` operator can be used with tuples to concatenate them and assign the result back to the variable.
# 10. The `+=` operator can be used with dictionaries to add key-value pairs to the dictionary and assign the result back to the variable.
# 11. The `+=` operator can be used with sets to add elements to the set and assign the result back to the variable.
# 12. The `+=` operator can be used with frozensets to create a new frozenset and assign the result back to the variable.
# 13. The `+=` operator can be used with bytes to create a new bytes object and assign the result back to the variable.
# 14. The `+=` operator can be used with bytearrays to modify the bytearray in place and assign the result back to the variable.
# 15. The `+=` operator can be used with memoryviews to modify the memoryview in place and assign the result back to the variable.
# 16. The `+=` operator can be used with arrays to modify the array in place and assign the result back to the variable.
# 17. The `+=` operator can be used with numpy arrays to modify the numpy array in place and assign the result back to the variable.
# 18. The `+=` operator can be used with pandas DataFrames to modify the DataFrame in place and assign the result back to the variable.
# 19. The `+=` operator can be used with pandas Series to modify the Series in place and assign the result back to the variable.
# 20. The `+=` operator can be used with pandas Index to modify the Index in place and assign the result back to the variable.


# list
list_ = [0,1,2,3,4,5,6,7,8,9]
# The `id()` function returns the identity of an object. The identity is unique and constant for this object during its lifetime.
print(id(list_))
list_1 = [10,11,12,13,14,15,16,17,18,19]
list_ += list_1
print(list_) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# output of the following should be same as above
print(id(list_))

# String
string_ = "Namma Benguluru"
print(id(string_))
string_ += " is great"
print(string_) # Output: Namma Benguluru is great
# Since strings are immutable, a new string object is created and the original string remains unchanged.
# The id of the new string object is different from the original string object.
print(id(string_)) 


# Tuple
tuple_ = (0,1,2,3,4,5,6,7,8,9)
print(id(tuple_))
tuple_ += (10,11,12,13,14,15,16,17,18,19)
print(tuple_) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
# Since tuples are immutable, a new tuple object is created and the original tuple remains unchanged.
# The id of the new tuple object is different from the original tuple object.
print(id(tuple_))
# The `+=` operator creates a new object and assigns it to the variable.

# The *
# list
list_ = [0,1,2,3,4,5,6,7,8,9]
print(id(list_))
list_ *= 2
print(list_) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
# output of the following should be same as above
print(id(list_))

# String
string_ = "Namma Benguluru"
print(id(string_))
string_ *= 2
print(string_) # Output: Namma BenguluruNamma Benguluru
# Since strings are immutable, a new string object is created and the original string remains unchanged.
# The id of the new string object is different from the original string object.

# Tuple
tuple_ = (0,1,2,3,4,5,6,7,8,9)
print(id(tuple_))
tuple_ *= 2
print(tuple_) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# Since tuples are immutable, a new tuple object is created and the original tuple remains unchanged.
# The id of the new tuple object is different from the original tuple object.
print(id(tuple_))
# The `*` operator creates a new object and assigns it to the variable.