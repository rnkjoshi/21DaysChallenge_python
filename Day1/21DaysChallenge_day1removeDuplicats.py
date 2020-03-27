numbers = [120,44,44,44,7,6,8,9,9]
numbers.sort();
print(numbers)
item = 0
while(item != len(numbers)-1):
    if numbers[item] == numbers[item+1]:
        numbers.remove(numbers[item+1])
        item -= 1
    item += 1
print(numbers)