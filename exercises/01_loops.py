"""
TODO:
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5

"""
for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

x = 0
for i in range(1, 101):
    x = x + i
print(x)

for i in range(1, 13):
    print(f"5 x {i} = {5 * i}")