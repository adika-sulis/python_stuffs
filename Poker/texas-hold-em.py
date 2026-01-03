import os, random, time
def clear():
    os.system("cls" if os.name=="nt" else "clear")

clear()

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "jack", "queen", "king"]
card_symbols = ["spades", "hearts", "diamonds", "clubs"]
# card_colors = ["black", "red"]

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

class comp:
    def __init__(self, comp_card, comp_color, comp_symbol):
        self.comp_card = comp_card
        self.comp_color = comp_color
        self.comp_symbol = comp_symbol

counter = 0
for _ in range(2):
    try:
        comp_card = random.choice(cards)
        comp_symbol = random.choice(card_symbols)
        if comp_symbol in ["spades", "clubs"]:
            comp_color = "black"
        else:
            comp_color = "red"
        if counter == 0:
            comp_card_one = comp(comp_card, comp_symbol, comp_color)
            counter += 1
        else:
            comp_card_two = comp(comp_card, comp_symbol, comp_color)               
    except ValueError:
        pass

try:
    open(f"{os.path.dirname(__file__)}/tries.txt", "w", encoding="utf-8")
except FileNotFoundError:
        open(f"{os.path.dirname(__file__)}/tries.txt", "a")

with open(f"{os.path.dirname(__file__)}/tries.txt", "w", encoding="utf-8") as t:
    t.write(f"\n------------------\nJÁTÉKOS\n   ELSŐ Kártya: {card_one.card} {card_one.symbol} {card_one.color}\n   MÁSODIK Kártya: {card_two.card} {card_two.symbol} {card_two.color}       \n------------------\n")
    t.write(f"\n------------------\nCOMP\n    ELSŐ Kártya: {comp_card_one.comp_card} {comp_card_one.comp_symbol} {comp_card_one.comp_color}\n    MÁSODIK Kártya: {comp_card_two.comp_card}  {comp_card_two.comp_symbol} {comp_card_two.comp_color}\n------------------\n")


