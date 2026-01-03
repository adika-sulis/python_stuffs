import os, random, time
def clear():
    os.system("cls" if os.name=="nt" else "clear")

clear()

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "jack", "queen", "king"]
card_symbols = ["spades", "hearts", "diamonds", "clubs"]
card_colors = ["black", "red"]

class player:
    def __init__(self, card, color, symbol):
        self.card = card
        self.color = color
        self.symbol = symbol

counter = 0
for _ in range(2):
    try:
        card = random.choice(cards)
        symbol = random.choice(card_symbols)
        if symbol in ["spades", "clubs"]:
            color = "black"
        else:
            color = "red"
        if counter == 0:
            card_one = player(card, symbol, color)
            counter += 1
        else:
            card_two = player(card, symbol, color)               
    except ValueError:
        pass

print(f"\n------------------\nELSŐ Kártya: {card_one.card} {card_one.symbol} {card_one.color}\nMÁSODIK Kártya: {card_two.card} {card_two.symbol} {card_two.color}\n------------------\n")

