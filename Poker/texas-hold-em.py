import os, random, time
def clear():
    os.system("cls" if os.name=="nt" else "clear")

clear()

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "jack", "queen", "king"]
card_symbols = ["Spades", "Hearts", "Diamonds", "Clubs"]
# card_colors = ["black", "red"]

for i in range(13):
    random.shuffle(cards)
    random.shuffle(card_symbols)

class card_mechanic:
    def __init__(self, card, color, symbol):
        self.card = card
        self.color = color
        self.symbol = symbol

counter = 0
counterComp = 0

for _ in range(2):
    try:
        def get2PlayerCards():
            global card,color,symbol,card_one,card_two, counter
            for __ in range(2):
                card = random.choice(cards)
                symbol = random.choice(card_symbols)
                if symbol in ["Spades", "Clubs"]:
                    color = "Black"
                else:
                    color = "Red"
                if counter == 0:
                    card_one = card_mechanic(card, symbol, color)
                    counter += 1
                else:
                    card_two = card_mechanic(card, symbol, color)
        get2PlayerCards()

        while True:
            if card_one.card == card_two.card and card_one.color ==     card_two.color and card_one.symbol == card_two.symbol:
                print(f"\n------------------\nJÁTÉKOS\n   ELSŐ Kártya: {card_one.card} {card_one.symbol} {card_one.color}\n   MÁSODIK Kártya: {card_two.card} {card_two.symbol} {card_two.color}       \n------------------\n")

                get2PlayerCards()
            # Ha a játékos két kártyája ELTÉR
            else:
                break

        comp_card = random.choice(cards)
        comp_symbol = random.choice(card_symbols)
        if comp_symbol in ["Spades", "Clubs"]:
            comp_color = "Black"
        else:
            comp_color = "Red"
        if counterComp == 0:
            comp_card_one = card_mechanic(comp_card, comp_symbol, comp_color)
            counterComp += 1
        else:
            comp_card_two = card_mechanic(comp_card, comp_symbol, comp_color)                
    except ValueError:
        print('ValueError ig')

try:
    open(f"{os.path.dirname(__file__)}/tries.txt", "x", encoding="utf-8")
except FileExistsError:
    pass

with open(f"{os.path.dirname(__file__)}/tries.txt", "w", encoding="utf-8") as t:
    t.write(f"\n------------------\nJÁTÉKOS\n   ELSŐ Kártya: {card_one.card} {card_one.symbol} {card_one.color}\n   MÁSODIK Kártya: {card_two.card} {card_two.symbol} {card_two.color}       \n------------------\n")
    t.write(f"\n------------------\nCOMP\n    ELSŐ Kártya: {comp_card_one.card} {comp_card_one.symbol} {comp_card_one.color}\n    MÁSODIK Kártya: {comp_card_two.card} {comp_card_two.symbol} {comp_card_two.color}\n------------------\n")


