import os, random, json
from string import Template as template

with open(f"{os.path.dirname(__file__)}/responses.json", "r", encoding="utf-8") as f:
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

lang_input = input("Kérlek válaszd ki a nyelvet / Please choose the language:\n    >> Magyar (hu) | English (en) <<    ")

if lang_input.lower() in ["magyar","hu"]:
    lang = "hu"
elif lang_input.lower() in ["english","en"]:
    lang = "en"
elif lang_input.lower() not in langList:
    lang="undefined"
    msg_response = template(responses["hu"]["errors"]["lang_errors"]).substitute(
        langList=", ".join(langList)
    )
    clear()
    print(msg_response)
    exit()
else:
    print(responses["undefined"]["errors"]["unexpected"])
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

clear()
print(resp.name)
maxPoint = int(input(resp.max_points))

if maxPoint <= 0:
    print(resp.max_points_too_low)
    exit()
elif maxPoint > 100:
    print(resp.max_points_too_high)
    exit()

class comp:
    def __init__(self):
        self.choice = random.choice(choiceLIST)
        if lang == "hu":
            self.irasban = {"k": "kő", "p": "papír", "o": "olló"}[self.choice]
        elif lang == "en":
            self.irasban = {"k": "rock", "p": "paper", "o": "scissors"}[self.choice]

    def game(self):
        global userPoint, compPoint, continueQuestion

        if user == self.choice:
            result_template = responses[lang]["outcome"]["draw"]
        elif (user == "k" and self.choice == "o") or \
             (user == "p" and self.choice == "k") or \
             (user == "o" and self.choice == "p"):
            result_template = responses[lang]["outcome"]["win"]
        else:
            result_template = responses[lang]["outcome"]["lose"]


        clear()
        print(resp.name)

        if (user == "k" and self.choice == "o") or \
           (user == "p" and self.choice == "k") or \
           (user == "o" and self.choice == "p"):
            userPoint += 1
        elif user != self.choice:
            compPoint += 1

        msg_response = template(result_template).safe_substitute(
            irasbanUser=irasbanUser,
            computerChoice=self.irasban,
            userPoint=userPoint,
            compPoint=compPoint
        )
        print(msg_response)

        continueQuestion = input(responses[lang]["outcome"]["continueQuestion"])
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
    computer.game()

clear()
print(resp.name)
if userPoint == maxPoint:
    result_template = responses[lang]["overall_outcome"]["userWin"]
else:
    result_template = responses[lang]["overall_outcome"]["userLose"]

msg_response = template(result_template).safe_substitute(
    userPoint=userPoint,
    compPoint=compPoint,
    maxPoint=maxPoint
)

print(msg_response)