numbers = []
for item in range(10) :
    numbers.append(int(input()))
print(numbers)
largest = 0
for item in numbers :
    if item > largest:
        largest = item
print(f"largest number in list is {largest}")