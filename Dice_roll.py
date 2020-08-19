import random


# dice = ['1', '2', '3', '4', '5', '6']
# roll = random.choice(dice)
# print(roll)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

