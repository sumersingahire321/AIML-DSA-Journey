# Problem: Find largest number in a list

num = [3, 7, 2, 9, 5]

largest = num[0]

for n in num:
    if n > largest:
        largest = n

print(f"The Largest number is {largest} . ")