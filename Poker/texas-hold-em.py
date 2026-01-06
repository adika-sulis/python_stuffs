import os, random, time
def clear():
    os.system("cls" if os.name=="nt" else "clear")

clear()

cards = ['2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades', 'Ace Spades', 'Jack Spades', 'Queen Spades', 'King Spades', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', '8 Clubs', '9 Clubs', '10 Clubs', 'Ace Clubs', 'Jack Clubs', 'Queen Clubs', 'King Clubs', '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', '10 Hearts', 'Ace Hearts', 'Jack Hearts', 'Queen Hearts', 'King Hearts', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', '10 Diamonds', 'Ace Diamonds', 'Jack Diamonds', 'Queen Diamonds', 'King Diamonds']

usedCards = []
removedCards = []

# balances
compBal = 5000
userBal = 5000
bettingPool = None
minimumBetAmount = 1.15
previousBet = None

def removeUsedCardFromCards():
    for usedCARD in usedCards:
        try:
            removedCards.append(usedCARD)
            cards.remove(usedCARD)
        except ValueError:
            pass

for i in range(13):
    random.shuffle(cards)

class card_mechanic:
    def __init__(self, card, color):
        self.card = card
        self.color = color

for _ in range(1):
   # try:
        def get2PlayerCards():
            global card,color,card_one,card_two, counter, cardContains,usedCards
            counter = 0

            for __ in range(2):
                card = random.choice(cards)
                while True:
                    if card in usedCards:
                        removeUsedCardFromCards()
                        card = random.choice(cards)
                        break
                    else:
                        break
                cardContains = card.split()
                if cardContains[1] in ["Spades", "Clubs"]:
                    color = "Black"
                else:
                    color = "Red"
                if counter == 0:
                    card_one = card_mechanic(card, color)
                    usedCards.append(card_one.card)      
                    counter += 1
                    removeUsedCardFromCards()

                else:
                    card_two = card_mechanic(card, color)
                    usedCards.append(card_two.card)
                    removeUsedCardFromCards()


        def get2CompCards():  
            global card,comp_card,comp_color,compCardContains, usedCards,comp_card_one,comp_card_two, counterComp

            counterComp = 0

            for ___ in range(2):
                comp_card = random.choice(cards)
                while True:
                    if comp_card in cards or card in cards:
                        comp_card = random.choice(cards)
                        break
                    else:
                        break
                compCardContains = card.split()
                if compCardContains[1] in ["Spades", "Clubs"]:
                    comp_color = "Black"
                else:
                    comp_color = "Red"
                if counterComp == 0:
                    comp_card_one = card_mechanic(comp_card, comp_color)
                    usedCards.append(comp_card_one.card)      
                    counterComp += 1
                    removeUsedCardFromCards()
                else:
                    comp_card_two = card_mechanic(comp_card, comp_color)
                    usedCards.append(comp_card_two.card)
                    removeUsedCardFromCards()
                   
        get2PlayerCards()
        get2CompCards()
   # except ValueError:
     #   print('ValueError ig')

try:
    open(f"{os.path.dirname(__file__)}/tries.txt", "x", encoding="utf-8")
except FileExistsError:
    pass
time.sleep(0.5)
with open(f"{os.path.dirname(__file__)}/tries.txt", "w", encoding="utf-8") as t:
    t.write(f"\n------------------\nPlayer\n   First Card: {card_one.card} {card_one.color}\n   Second Card: {card_two.card}  {card_two.color}       \n------------------\n")
    t.write(f"\n------------------\nComputer\n    First Card: {comp_card_one.card} {comp_card_one.color}\n    Second Card: {comp_card_two.card} {comp_card_two.color}\n------------------\n")

time.sleep(2)

fieldCounter = 0

def get_a_FieldCard():
    global card,field_card,field_color,fieldCardContaines, usedCards,field_card_one,field_card_two, field_card_three, field_card_four, field_card_five, fieldCounter

    for ___ in range(1):
       field_card = random.choice(cards)
       while True:
           if field_card in cards or card in cards:
               field_card = random.choice(cards)
               break
           else:
               break
       fieldCardContaines = card.split()
       if fieldCardContaines[1] in ["Spades", "Clubs"]:
           field_color = "Black"
       else:
           field_color = "Red"
       if fieldCounter == 0:
           field_card_one = card_mechanic(field_card, field_color)
           usedCards.append(field_card_one.card)      
           fieldCounter += 1
           removeUsedCardFromCards()
       elif fieldCounter == 1:
           field_card_two = card_mechanic(field_card, field_color)
           usedCards.append(field_card_two.card)
           fieldCounter += 1
           removeUsedCardFromCards()
       elif fieldCounter == 2:
           field_card_three = card_mechanic(field_card, field_color)
           usedCards.append(field_card_three.card)
           fieldCounter += 1
           removeUsedCardFromCards()
       elif fieldCounter == 3:
           field_card_four = card_mechanic(field_card, field_color)
           usedCards.append(field_card_four.card)
           fieldCounter += 1
           removeUsedCardFromCards()
       else:
           field_card_five = card_mechanic(field_card, field_color)
           usedCards.append(field_card_five.card)
           removeUsedCardFromCards()

for get3fieldcards_ in range(3):
    get_a_FieldCard()

with open(f"{os.path.dirname(__file__)}/tries.txt", "w", encoding="utf-8") as t:
    t.write(f"\n------------------\nPlayer\n   First Card: {card_one.card} {card_one.color}\n   Second Card: {card_two.card}  {card_two.color}       \n------------------\n")

    t.write(f"\n------------------\nComputer\n    First Card: {comp_card_one.card} {comp_card_one.color}\n    Second Card: {comp_card_two.card} {comp_card_two.color}\n------------------\n")


with open(f"{os.path.dirname(__file__)}/tries.txt", "a", encoding="utf-8") as fieldCardsPrint:

    if fieldCounter == 3:
        fieldCardsPrint.write(f"\n-------------------\nField Cards:\n 1st card: {field_card_one.card} {field_card_one.color}\n 2nd card: {field_card_two.card} {field_card_two.color}\n 3rd card: {field_card_three.card} {field_card_three.color}")
    '''elif fieldCounter == 4:
        fieldCardsPrint.write(f" 4th card: {field_card_four.card} {field_card_four.color}")
    elif fieldCounter == 5:
        fieldCardsPrint.write(f" 5th card: {field_card_five.card} {field_card_five.color}\n-------------------")'''


def compMove():
    global compMoveChoice, comp_card_one, comp_card_two, compBal, bettingPool, minimumBetAmount, compBet, firstRound, previousBet

    compMoveChoice = random.choice(["s","f","b"])

    if compMoveChoice == "s":
        pass
    elif compMoveChoice == "f":
        comp_card_one.card = 0
        comp_card_one.color = 0
        comp_card_two.card = 0
        comp_card_two.color = 0
        comp_card_one = 0
        comp_card_two = 0

    else: # bet
        if firstRound == True:
            compBet = random.randint(25, compBal+1)
        elif firstRound == False:
            if previousBet != None:
                compBet = random.randint(previousBet, compBal+1) * minimumBetAmount
            else:
                compBet = random.randint(25, compBal+1) * minimumBetAmount

            if compBal < 0:
                compBet = compBal

        previousBet = compBet
        bettingPool + compBet
        compBal - compBet


firstRound = True

while True:
    usersMove = input("What will you do?\n Stand (s) | Fold (f) | Bet (b)")
    if not usersMove:
        pass
    elif usersMove.strip().lower() in ["s","f","b"]:
        if usersMove.strip().lower() == "s":
            print("stand")
            break
        elif usersMove.strip().lower() == "f":
            print("fold")
            break
        elif usersMove.strip().lower() == "b":
            if firstRound == True:
                userBet = int(input("Please give me your bet!\n Minimum 25:   "))
                if # to be continued
        elif firstRound == False:
            if previousBet != None:
                userBet = random.randint(previousBet, compBal+1) * minimumBetAmount
            else:
                userBet = random.randint(25, compBal+1) * minimumBetAmount

            if compBal < 0:
                userBet = compBal
        bettingPool + userBet
        compBal - userBet
        previousBet = userBet
        break
    else:
        pass

firstRound = False