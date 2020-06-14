# Print 3 random ints between range 0 - 10
import random

for i in range(3):
    print(random.randint(0,10))


# Choose random member of array
import random

members = ['Steve', 'Harry', 'John', 'Bob']
leader = random.choice(members)
print(leader)


# Rolling a dice
import random


class Dice:
    def roll(self):
        first_value = random.randint(1,6)
        second_value = random.randint(1,6)
        return (first_value,second_value)


dice = Dice()
print(dice.roll())