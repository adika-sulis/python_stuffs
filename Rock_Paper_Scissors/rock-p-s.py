import os, random, json
from string import Template as template

with open("Rock_Paper_Scissors/responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

userPont = 0
compPont = 0
choiceLIST = ["k", "p", "o"]
langList = ["hu", "en"]
lang = "en"

class resp():
    response_name = responses["name"][lang]
    response_errors = responses["errors"]["lang_errors"]
    response_max_points = responses["max_point"][lang]
clear()

lang = input("Kérlek válaszd ki a nyelvet / Please choose the language:\n    >> Magyar (hu) | English (en) <<    ")

if lang.lower() == "magyar" or lang.lower() == "hu":
    lang = "hu"
elif lang.lower() == "english" or lang.lower() == "en":
    lang = "en"
elif lang not in langList:
    lang="undefined"
    msg_response = template(resp.response_errors[lang]).substitute(
    langList=", ".join(langList)
)
    clear()
    print(msg_response)
    exit()
else:
    print("Unexpected error! Leaving imideately...")
    exit()

msg_response = template(resp.response_errors[lang]).substitute(
    lang = lang,
    langList=", ".join(langList)
)

clear()
resp()
print(resp.response_name)
maxPoint = int(input(resp.response_max_points))

if maxPoint <= 0:
    print(f"\nNot a valid point input!\nYour input: {maxPoint}\nPlease restart the game, and choose a valid positive integer number!")
    exit()
elif maxPoint > 100:
    print(f"\nThe maximum point limit is 100!\nYour input: {maxPoint}\nPlease restart the game, and choose a valid positive integer number under 100!")
    exit()
elif maxPoint > 0 and maxPoint <=100:
    pass
else:
    print("Unexpected error! Leaving imideately...")
    exit()

class comp:
    def __init__(self):
        self.choice = random.choice(choiceLIST)
        if lang == "hu":
            if self.choice == "o":
                self.irasban = "olló"
            elif self.choice == "p":
                self.irasban = "papír"
            else:
                self.irasban = "kő"
        elif lang == "en":
            if self.choice == "o" or self.choice == "s":
                self.irasban = "scissors"
            elif self.choice == "p":
                self.irasban = "paper"
            else:
                self.irasban = "rock"

    def game(self):
        global userPont
        global compPont
        global kerdesTovabb
        
        if user == "k" and self.choice == "o" or user == "p" and self.choice == "k" or user == "o" and self.choice == "p":
            clear()
            userPont += 1
            print(">>> KŐ PAPÍR OLLÓ <<<")
            print(f"\nGratulálok, ezt a kört megnyerted!\nEzt választottad:      {irasbanUser}\nA gép ezt választotta: {self.irasban}\n\nPontszámod:   {userPont}\nGép pontszáma: {compPont}")
        elif user == self.choice:
            clear()
            print(">>> KŐ PAPÍR OLLÓ <<<")
            print(f"\nEz a kör DÖNTETLEN!\nEzt választottad:      {irasbanUser}\nA gép ezt választotta: {self.irasban}\n\nPontszámod:   {userPont}\nGép pontszáma: {compPont}")
        else:
            clear()
            compPont += 1
            print(">>> KŐ PAPÍR OLLÓ <<<")
            print(f"\nSajnálom elvesztetted ezt a kört!\nEzt választottad:      {irasbanUser}\nA gép ezt választotta: {self.irasban}\n\nPontszámod:   {userPont}\nGép pontszáma: {compPont}")
        kerdesTovabb = input("\nA következő körhöz ENTER!\nKilépéshez >> vége\n")
        if kerdesTovabb.lower() == "vége" or kerdesTovabb.lower() == "vege" or kerdesTovabb.lower() == "exit":
            clear()
            exit()
        
while userPont < maxPoint and compPont < maxPoint:
    clear()
    print(">>> KŐ PAPÍR OLLÓ <<<")

    user = input("\nKérlek válassz!\n| Kő (k) | Papír (p) | Olló (o) | Kilépés (vége) |   ")

    while True:
        if not user:
            clear()
            print(">>> KŐ PAPÍR OLLÓ <<<")
            user = input("\nKérlek válassz!\n| Kő (k) | Papír (p) | Olló (o) | Kilépés (vége) |   ")
        elif user.lower() == "papír" or user.lower() == "papir":
            user = "p"
        elif user.lower() == "kő" or user.lower() == "ko":
            user = "k"
        elif user.lower() == "olló" or user.lower() == "ollo":
            user = "o"
        elif user.lower() == "vége" or user.lower() == "vege" or user.lower() == "exit":
            clear()
            exit()
        elif user != "p" and user != "k" and user != "o":
            clear()
            print(">>> KŐ PAPÍR OLLÓ <<<")
            print(f"\nNem érvényes a megadott válasz!\nVálaszod: {user}")
            user = input("\nKérlek válassz!\n| Kő (k) | Papír (p) | Olló (o) | Kilépés (vége) |   ")
        else:
            break

    if user == "o":
        irasbanUser = "olló"
    elif user == "p":
        irasbanUser = "papír"
    else:
        irasbanUser = "kő"

    comp()
    comp().game()

if userPont == maxPoint:
    clear()
    print(">>> KŐ PAPÍR OLLÓ <<<")
    print(f"\nGratulálok, Te voltál az első aki megnyert {maxPoint} kört!\n\n>> Pontszámok:\n   A Te pontszámod:  {userPont}\n   A Gép pontszáma:  {compPont}\n")
else:
    clear()
    print(">>> KŐ PAPÍR OLLÓ <<<")
    print(f"\nSajnálom, a gép volt az aki elsőnek megnyert {maxPoint} kört!\n\n>> Pontszámok:\n   A Te pontszámod:  {userPont}\n   A Gép pontszáma:  {compPont}\n")
 