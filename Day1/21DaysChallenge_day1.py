weight = int(input('Weight:'))

weightType = input('(L)bs or (K)g ? ')

if weightType.upper() == 'L':
    print('your weight in Kg is ')
    print(weight / 2.3)
elif weightType.upper() == 'K':
    print('your weight in Lbs is ')
    print(weight * 2.3)
else:
    print("unit is invalid! please enter correct unit.")
