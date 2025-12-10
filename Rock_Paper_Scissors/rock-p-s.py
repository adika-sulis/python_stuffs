import os
import random
def clear():
    os.system("cls" if os.name == "nt" else "clear")

userPont = 0
compPont = 0
choiceLIST = ["k", "p", "o"]

clear()
print(">>> KŐ PAPÍR OLLÓ <<<")
maxPoint = int(input("\nKérlek add meg, hogy hány pontig menjen!\nMegjegyzés: Addig meg, amíg Te vagy a Gép el nem éri a megadott pontszámot!   "))

class comp:
    def __init__(self):
        self.choice = random.choice(choiceLIST)
        if self.choice == "o":
            self.irasban = "olló"
        elif self.choice == "p":
            self.irasban = "papír"
        else:
            self.irasban = "kő"

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
 