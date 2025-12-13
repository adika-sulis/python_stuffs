import os, random, json
from string import Template as template

with open("Rock_Paper_Scissors/responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

userPoint = 0
compPoint = 0
choiceLIST = ["k", "p", "o"]
langList = ["hu", "en"]
lang = "en"

class resp():
    lang = lang
    name = responses[lang]["name"]
    choices = responses[lang]["choices"]
    choicesRPS = responses[lang]["choicesRPS"]
    errors = responses[lang]["errors"]["lang_errors"]
    error_unexpected = responses["undefined"]["errors"]["unexpected"]
    error_wrong_response = responses[lang]["errors"]["wrong_response"]
    max_points = responses[lang]["max_point"]["limit"]
    max_points_too_low = responses[lang]["max_point"]["errors"]["too_low"]
    max_points_too_high = responses[lang]["max_point"]["errors"]["too_high"]
    outcome = responses[lang]["outcome"]
    overall_outcome = responses[lang]["overall_outcome"]

clear()
resp()

lang = input("Kérlek válaszd ki a nyelvet / Please choose the language:\n    >> Magyar (hu) | English (en) <<    ")

if lang.lower() == "magyar" or lang.lower() == "hu":
    lang = "hu"
elif lang.lower() == "english" or lang.lower() == "en":
    lang = "en"
elif lang not in langList:
    lang="undefined"
    msg_response = template(resp.errors).substitute(
        langList=", ".join(langList)
    )
    clear()
    print(msg_response)
    exit()
else:
    print(resp.error_unexpected)
    exit()

resp.lang = lang
resp.name = responses[lang]["name"]
resp.choices = responses[lang]["choices"]
resp.choicesRPS = responses[lang]["choicesRPS"]
resp.errors = responses[lang]["errors"]["lang_errors"]
resp.error_wrong_response = responses[lang]["errors"]["wrong_response"]
resp.max_points = responses[lang]["max_point"]["limit"]
resp.max_points_too_low = responses[lang]["max_point"]["errors"]["too_low"]
resp.max_points_too_high = responses[lang]["max_point"]["errors"]["too_high"]
resp.outcome = responses[lang]["outcome"]
resp.overall_outcome = responses[lang]["overall_outcome"]

def msg_response_func_outer():
    global msg_response
    msg_response = template(resp.lang).safe_substitute(
        lang=lang,
        langList=", ".join(langList),
    )

msg_response_func_outer()
clear()
print(resp.name)
maxPoint = int(input(resp.max_points))

if maxPoint <= 0:
    print(resp.max_points_too_low)
    exit()
elif maxPoint > 100:
    print(resp.max_points_too_high)
    exit()
elif maxPoint > 0 and maxPoint <=100:
    pass
else:
    print(resp.error_unexpected)
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
    
    def game(self, user_choice, irasbanUser):
        global userPoint, compPoint, continueQuestion

        msg_response = template(resp.lang).safe_substitute(
            lang=lang,
            langList=", ".join(langList),
            irasbanUser=irasbanUser,
            computerChoice=self.irasban,
            userPont=userPoint,
            compPont=compPoint
)



        if user_choice == "k" and self.choice == "o" or \
           user_choice == "p" and self.choice == "k" or \
           user_choice == "o" and self.choice == "p":
            userPoint += 1
            clear()
            print(resp.name)
            print(resp.outcome["win"])
        elif user_choice == self.choice:
            clear()
            print(resp.name)
            print(resp.outcome["draw"])
        else:
            compPoint += 1
            clear()
            print(resp.name)
            print(resp.outcome["lose"])

        continueQuestion = input(resp.outcome["continueQuestion"])
        if continueQuestion.lower() in ["vége","vege","exit"]:
            clear()
            exit()

while userPoint < maxPoint and compPoint < maxPoint:
    clear()
    print(resp.name)

    user = input(resp.choices)

    while True:
        if not user:
            clear()
            print(resp.name)
            user = input(resp.choices)
        elif user.lower() in ["papír","papir","paper"]:
            user = "p"
        elif user.lower() in ["kő","ko","r","rock"]:
            user = "k"
        elif user.lower() in ["olló","ollo","s","scissors"]:
            user = "o"
        elif user.lower() in ["vége","vege","exit"]:
            clear()
            exit()
        elif user not in ["p","k","o"]:
            clear()
            print(resp.name)
            print(resp.error_wrong_response)
            user = input(resp.choices)
        else:
            break

    if user == "o":
        irasbanUser = resp.choicesRPS["scissors"]
    elif user == "p":
        irasbanUser = resp.choicesRPS["paper"]
    else:
        irasbanUser = resp.choicesRPS["rock"]

    computer = comp()
    computer.game(user, irasbanUser)

if userPoint == maxPoint:
    clear()
    print(resp.name)
    print(f"\nGratulálok, Te voltál az első aki megnyert {maxPoint} kört!\n\n>> Pontszámok:\n   A Te pontszámod:  {userPoint}\n   A Gép pontszáma:  {compPoint}\n")
else:
    clear()
    print(resp.name)
    print(f"\nSajnálom, a gép volt az aki elsőnek megnyert {maxPoint} kört!\n\n>> Pontszámok:\n   A Te pontszámod:  {userPoint}\n   A Gép pontszáma:  {compPoint}\n")
