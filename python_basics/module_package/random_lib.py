#random is a library that comes with python
import random

coin = random.choice(["heads", "tails"])
print(coin)

#to generate nmber b/w a and b
number = random.randint(1, 10)
print(number)

#list in random order
cards = ['jack', 'queen', 'king'] 
random.shuffle(cards)
for card in cards:
    print(card)
