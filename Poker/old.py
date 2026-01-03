import os, random, time
def clear():
    os.system("cls" if os.name=="nt" else "clear")

clear()

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "jack", "queen", "king"]
card_symbols = ["spades", "hearts", "diamonds", "clubs"]
card_colors = ["black", "red"]

'''
player_card = random.choice(cards)
player_card_symbol = random.choice(card_symbols)
if player_card_symbol in ["spades", "clubs"]:
    player_card_color = "black"
else:
    player_card_color = "red"
try:
    print(f"-------\n{player_card.capitalize()} {player_card_color.capitalize()} {player_card_symbol.capitalize()}")
    time.sleep(0.5)
except AttributeError:
    print(f"-------\n{player_card} {player_card_color.capitalize()} {player_card_symbol.capitalize()}")
    time.sleep(0.5)
'''
