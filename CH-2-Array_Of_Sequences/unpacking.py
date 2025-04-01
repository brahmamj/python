# unpacking with * operator
# # The * operator can be used to unpack the remaining values in a tuple into a list.
# # This is useful when you want to capture multiple values from a tuple without explicitly specifying each one.
# # Example of unpacking with * operator

a,b,*rest = range(5)
print(a,b,rest) # Output: 0 1 [2, 3, 4]

*rest, a, b = range(10)
print(a,b,rest) # Output: 8 9 [0, 1, 2, 3, 4, 5, 6, 7]

a,*rest,b = range(10)
print(a,b,rest) # Output: 0 9 [1, 2, 3, 4, 5, 6, 7, 8]

print([1,2,*range(5)]) # Output: [1, 2, 0, 1, 2, 3, 4]

county,latitube,longitude = "India", 20.5937, 78.9629
print(county,latitube,longitude) # Output: India 20.5937 78.9629

# Contries tuple with latitude and longitude as list
countries = ("India", [20.5937, 78.9629], "USA", [37.0902, -95.7129], "UK", [55.3781, -3.4360])
india,usa,uk = countries[0], countries[1], countries[3]
print(india,usa,uk) # Output: India [20.5937, 78.9629] USA [37.0902, -95.7129] UK [55.3781, -3.4360]

## Nested unpacking
# # Nested unpacking allows you to unpack values from nested tuples or lists.
# # This is useful when you have a complex data structure and want to extract specific values.
# # Example of nested unpacking
print("=============Nested unpacking=================")
metro_areas =[("Tokyo", "Japan", 36.933, (35.6895, 139.6917)),("Delhi", "India", 21.372, (28.6139, 77.2090))
              ,("Mexico City", "Mexico", 19.4326, (19.4326, -99.1332)),("New York", "USA", 8.623, (40.7128, -74.0060))
              ,("London", "UK", 8.982, (51.5074, -0.1278)),("Paris", "France", 2.244, (48.8566, 2.3522))]
for city, country, population, (latitude, longitude) in metro_areas:
    print(f"{city}, {country}: {population}, coordinates: ({latitude}, {longitude})")

# # Example of nested unpacking function
print(f"=============Nested unpacking function=================")
def main1():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name,_,_, (latitude, longitude) in metro_areas:
        print(f"{name:15} | {latitude:9} | {longitude:9}")
if __name__ == "__main__":
    main1()