import random

low = 1
high = 100
options = ("rock", "paper", "Scissors")
cards = ["2","3","6","4","8","9","A","K","Q"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)

print(cards)
