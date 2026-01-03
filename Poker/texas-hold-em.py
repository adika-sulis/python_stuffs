import os, random, time
def clear():
    os.system("cls" if os.name=="nt" else "clear")

clear()

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Ace", "Jack", "Queen", "King"]
card_symbols = ["Spades", "Hearts", "Diamonds", "Clubs"]

for i in range(13):
    random.shuffle(cards)
    random.shuffle(card_symbols)

class card_mechanic:
    def __init__(self, card, color, symbol):
        self.card = card
        self.color = color
        self.symbol = symbol

for _ in range(1):
    try:
        def get2PlayerCards():
            global card,color,symbol,card_one,card_two, counter
            counter = 0

            for __ in range(2):
                card = random.choice(cards)
                symbol = random.choice(card_symbols)
                if symbol in ["Spades", "Clubs"]:
                    color = "Black"
                else:
                    color = "Red"
                if counter == 0:
                    card_one = card_mechanic(card, color, symbol)
                    counter += 1
                else:
                    card_two = card_mechanic(card, color, symbol)

        def scanPlayerCards():
            global card,color,symbol,card_one,card_two, counter

            while True:
                if card_one.card == card_two.card and card_one.symbol ==    card_two.symbol:
                    get2PlayerCards()
                else:
                    break        

        def get2CompCards():   
            global comp_card,comp_color,comp_symbol,comp_card_one,comp_card_two, counterComp

            counterComp = 0

            for ___ in range(2):
                comp_card = random.choice(cards)
                comp_symbol = random.choice(card_symbols)
                if comp_symbol in ["Spades", "Clubs"]:
                    comp_color = "Black"
                else:
                    comp_color = "Red"
                if counterComp == 0:
                    comp_card_one = card_mechanic(comp_card, comp_color, comp_symbol)
                    counterComp += 1
                else:
                    comp_card_two = card_mechanic(comp_card, comp_color,comp_symbol)

        def scanCompCards():
            global comp_card,comp_color,comp_symbol,comp_card_one,comp_card_two, counterComp

            while True:
                if comp_card_one.card == comp_card_two.card and comp_card_one.symbol == comp_card_two.symbol:
                    get2CompCards()
                else:
                    break
        def scanCardsTogether():
            while True:
                if comp_card_one.card == card_one.card and comp_card_one.symbol == card_one.symbol or comp_card_two.card == card_two.card and comp_card_two.symbol == card_two.symbol or comp_card_one.card == card_two.card and comp_card_one.symbol == card_two.symbol or comp_card_two.card == card_one.card and comp_card_two.symbol == card_one.symbol:
                    get2CompCards()
                    get2PlayerCards()
                    scanCompCards()
                    scanPlayerCards()
                    scanCardsTogether()
                else:
                    break
                    
        get2PlayerCards()
        get2CompCards()
        scanPlayerCards()
        scanCompCards()
        scanCardsTogether()
    except ValueError:
        print('ValueError ig')

try:
    open(f"{os.path.dirname(__file__)}/tries.txt", "x", encoding="utf-8")
except FileExistsError:
    pass

with open(f"{os.path.dirname(__file__)}/tries.txt", "w", encoding="utf-8") as t:
    t.write(f"\n------------------\nPlayer\n   First Card: {card_one.card} {card_one.symbol} {card_one.color}\n   Second Card: {card_two.card} {card_two.symbol} {card_two.color}       \n------------------\n")
    t.write(f"\n------------------\nComputer\n    First Card: {comp_card_one.card} {comp_card_one.symbol} {comp_card_one.color}\n    Second Card: {comp_card_two.card} {comp_card_two.symbol} {comp_card_two.color}\n------------------\n")


