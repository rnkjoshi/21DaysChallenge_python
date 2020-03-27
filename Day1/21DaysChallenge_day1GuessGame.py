import math

number = int(9)

print("Guess a number between 1-10.but you've only three chance.")
i = 1
win = False
while i<=3:
    value = int(input(f"guess{i} : "))
    if number == value :
        win = True
        break;
    i += 1
if win :
    print("you guessed correct.")
else:
    print("sorry...you lost the game!")
print("Game Over!!!")

numbers = [5,2,5,2,2]
for item in numbers:
    result = ''
    for iterate in range(item):
        result += 'X'
    print(result)