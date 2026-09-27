import random

coin = random.choice(["heads", "tails"])
num = random.randint(1,2)
cards = ["joker", "queen", "king"]
random.shuffle(cards)
print(f"{num} {coin}")
for card in cards:
    print(card)