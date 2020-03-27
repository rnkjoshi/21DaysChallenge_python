import random

class dice :
    def roll(self):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return {x,y}
roll1 = dice();

roll1Tuple = roll1.roll()
print(roll1Tuple)
