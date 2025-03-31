# MatchCase statement
# MatchCase is a new feature in Python 3.10 that allows for more powerful and flexible pattern matching.
# It is similar to switch-case statements in other languages, but with more advanced capabilities.
# MatchCase allows you to match against complex data structures, including lists, tuples, and dictionaries.
# It also supports guards, which are additional conditions that must be met for a match to be successful.
# This makes it a powerful tool for writing clean and readable code.
# # Example of MatchCase statement

def match_case_example(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3 | 4 | 5:
            return "Three, Four, or Five"
        case _:
            return "Something else"
# # Example of MatchCase with guards
def match_case_with_guards(value):
    match value:
        case x if x < 0:
            return "Negative"
        case x if x == 0:
            return "Zero"
        case x if x > 0:
            return "Positive"
        case _:
            return "Something else"

# # Example of MatchCase with lists
def match_case_with_lists(value):
    match value:
        case [1, 2, 3]:
            return "List with 1, 2, and 3"
        case [1, *rest]:
            return f"List with 1 and {rest}"
        case _:
            return "Something else"
        
# # Example of MatchCase with dictionaries
def match_case_with_dicts(value):
    match value:
        case {"name": "Alice", "age": age} if age > 18:
            return f"Alice is an adult, age {age}"
        case {"name": "Bob", "age": age} if age < 18:
            return f"Bob is a minor, age {age}"
        case _:
            return "Something else"

# Example of match case with metro_areas
metro_areas =[("Tokyo", "Japan", 36.933, (35.6895, 139.6917)),("Delhi", "India", 21.372, (28.6139, 77.2090))
              ,("Mexico City", "Mexico", 19.4326, (19.4326, -99.1332)),("New York", "USA", 8.623, (40.7128, -74.0060))
              ,("London", "UK", 8.982, (51.5074, -0.1278)),("Paris", "France", 2.244, (48.8566, 2.3522))]
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
            match record:
                case [name,_,_,(lat,lon)] if lon < 0:
                    print(f"{name:15} | {lat:9} | {lon:9}")

if __name__ == "__main__":
    print(match_case_example(3))  # Output: Three, Four, or Five
    print(match_case_with_guards(-5))  # Output: Negative
    print(match_case_with_lists([1, 2, 3]))  # Output: List with 1, 2, and 3
    print(match_case_with_dicts({"name": "Alice", "age": 20}))  # Output: Alice is an adult, age 20
    main()
