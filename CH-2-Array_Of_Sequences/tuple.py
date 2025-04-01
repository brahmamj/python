#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are used to store multiple items in a single variable.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Tuple items can be of any data type.
# A tuple can have items of different data types.
# A tuple can also be empty.
# Tuple can be concatenated using + operator.
# Tuple can be repeated using * operator.
# Tuple can be sliced using [start:end] operator.
# Tuple can be converted to list using list() function.
# Tuple can be converted to string using str() function.
# Tuple can be converted to set using set() function.
# Tuple can be converted to dictionary using dict() function.
# Tuple can be used as records in databases.

t = (1,2,3,4,5)
print(t) # Output: (1, 2, 3, 4, 5)
t1 = tuple(i for i in range(1, 11))
print(t1) # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple(reversed(t1))) 
print(t1 == t)

# Dummy varabile in tuple unpacking
# Dummy variable is a variable that is used to hold a value temporarily and is not used in any further calculations or operations.  
# It is often used in tuple unpacking to ignore certain values in a tuple.
# In Python, you can use an underscore (_) as a dummy variable to indicate that you are intentionally ignoring a value.
# This is a common convention in Python and helps improve code readability.
# Example of dummy variable in tuple unpacking
# The following example demonstrates how to use a dummy variable in tuple unpacking to ignore certain values in a tuple.

country_list = ["India", "USA", "UK", "Canada"]
country_code_list = ["IN", "US", "UK", "CA"]

touple_list = list(zip(country_list, country_code_list))
print(touple_list) # Output: [('India', 'IN'), ('USA', 'US'), ('UK', 'UK'), ('Canada', 'CA')]

# Unpacking the tuple and ignoring the second value using a dummy variable
for country, _ in touple_list:
    print(country) # Output: India USA UK Canada

# In this example, the second value in the tuple (country code) is ignored by using a dummy variable (_).
# This allows us to focus only on the first value (country name) while unpacking the tuple.
