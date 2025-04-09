import collections as cl
# Dict or map in Python is a collection of key-value pairs.
# It is unordered, mutable, and indexed. The keys must be unique and immutable.
# The values can be of any data type and can be duplicated.
# The keys are used to access the values in the dictionary.
# The dictionary is defined using curly braces {} or the dict() constructor.
# The key-value pairs are separated by a colon : and the pairs are separated by commas ,.
# The keys can be of any immutable data type such as strings, numbers, or tuples.
# The values can be of any data type such as strings, numbers, lists, or even other dictionaries.
# The dictionary can be empty or can contain one or more key-value pairs.
# The dictionary can be nested, meaning that the value of a key can be another dictionary.
# The dictionary can be accessed using the keys and the values can be modified or deleted.
# The dictionary can also be iterated over using a for loop.
# The dictionary can be converted to a list of tuples using the items() method.
# The dictionary can be converted to a list of keys using the keys() method.
# The dictionary can be converted to a list of values using the values() method.

dial_codes = {
    'India': 91,
    'USA': 1,
    'Canada': 1,
    'Australia': 61,
    'Germany': 49,
    'France': 33,
    'Italy': 39,
    'Spain': 34,
    'UK': 44,
    'Russia': 7
}
print(dial_codes)  # Print the entire dictionary
print(dial_codes['India'])  # Accessing the value using the key

#################### Dictionaly Comprehension ####################
# Dictionary comprehension is a concise way to create dictionaries in Python.

#Dictionay comprehension
# Creating a dictionary using dictionary comprehension
country_codes = {code : country for country, code in dial_codes.items()}
print(country_codes)  # Print the entire dictionary


########## **kwargs ##########
# **kwargs
# The **kwargs syntax is used to pass a variable number of keyword arguments to a function.
# It allows you to pass a dictionary of key-value pairs to the function.
# The **kwargs syntax is used to unpack the dictionary into keyword arguments.
# The function can then access the values using the keys as arguments.
# The **kwargs syntax is used to pass a variable number of keyword arguments to a function.

def print_country_codes(**kwargs):
    for country, code in kwargs.items():
        print(f"{country}: {code}")

print_country_codes(
    India=91,
    USA=1,
    Canada=1,
    Australia=61,
    Germany=49, 
    France=33,
    Italy=39,
    Spain=34,
    UK=44,
    Russia=7
)

################### Merging dictionaries ###################
# merging dictionaries
# Merging two dictionaries using the update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 5, 'c': 3, 'd': 4}
dict1.update(dict2)  # dict1 is updated with dict2
print(dict1)  # Print the merged dictionary

#merging with literal syntax
dict3 = {**dict1, **dict2}  # Merging two dictionaries using the literal syntax
print(dict3)  # Print the merged dictionary

#merging with union operator
dict4 = dict1 | dict2  # Merging two dictionaries using the union operator
print(dict4)  # Print the merged dictionary

#inplace merging
dict1 |= dict2  # Merging two dictionaries using the inplace operator
print(dict1)  # Print the merged dictionary
# The merge operator (|) is used to merge two dictionaries and create a new dictionary.
# while merging the dictionaries, duplicate keys are overwritten by the values from the second dictionary.
# The merge operator (|=) is used to merge two dictionaries and update the first dictionary in place.

############# Match case with dictionary #############
# The match case statement is used to match a value against a pattern.
# It is similar to the switch case statement in other programming languages.
# The match case statement can be used to match a value against a dictionary.
# The match case statement can be used to match a value against a dictionary key.
# The match case statement can be used to match a value against a dictionary value.
# The match case statement can be used to match a value against a dictionary key-value pair.
#Book crater example
# The book record is a dictionary with the following keys:

def get_creaters(record: dict)-> list:
    match record:
        case {'type': 'book', 'api': 1, 'authors': [*names]}:
            return [*names]
        case {'type': 'book', 'api': 2, 'authors': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f'invalid book record: {record}')
        case {'type': 'journal', 'api': 1, 'authors': [*names]}:
            return [*names]
        case _:
            raise ValueError(f'invalid book record: {record}')
# The get_creaters function takes a dictionary as input and returns a list of authors.
# The match case statement is used to match the dictionary against different patterns.
# The first case matches a book record with api 1 and a list of authors.
# The second case matches a book record with api 2 and a single author.
# The third case matches a book record with no authors.
# The fourth case matches a journal record with api 1 and a list of authors.
# The last case matches any other record and raises a ValueError.
# The match case statement is used to match the dictionary against different patterns.
# The match case statement is used to match a value against a dictionary key-value pair.

b1 = dict(type='book', api=1, authors=['John Doe', 'Jane Doe'])
b2 = dict(type='book', api=2, authors='John Doe')
b3= dict(type='book')

print(get_creaters(b1))  # Returns ['John Doe', 'Jane Doe']
print(get_creaters(b2))  # Returns ['John Doe']
#print(get_creaters(b3))  # Raises ValueError: invalid book record: {'type': 'book'}

orderd_dict = cl.OrderedDict(api=1, authors=["John Doe", "Jane Doe"], type="book")
print(orderd_dict)  # Print the ordered dictionary
print(get_creaters(orderd_dict))  # Returns ['John Doe', 'Jane Doe']
# The OrderedDict is a subclass of the built-in dict class.
# It is used to create a dictionary that maintains the order of the keys.
# The OrderedDict is used to create a dictionary that maintains the order of the keys.
#Even with the ordered dictionary, the match case statement works as expected.
# The match case statement is used to match the dictionary against different patterns.