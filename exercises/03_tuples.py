"""
TODO:
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.
Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.
Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""

coordinates = (40.7128, -74.0060, 10)
lat, lon, alt = coordinates
print("Latitude:", lat)
print("Longitude:", lon)
print("Altitude:", alt)

person_info = ("Rena", 20, 5.4)
name, age, height = person_info
print("Name:", name)
print("Age:", age)
print("Height:", height)

immutable_tuple = (10, 12, 14)

try:
    immutable_tuple[1] = 11
except TypeError as e:
    print(e)