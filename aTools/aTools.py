def cls():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def pinput(message:str, unit:str=""):
    x = input(message)
    x = x.strip()
    if x.startswith(unit):
        x = x.removeprefix(unit)
    elif x.endswith(unit):
        x = x.removesuffix(unit)
    try:
        x = int(x)
    except ValueError:
        try:
            x = float(x)
        except ValueError:
            try:
                x = list(x)
                y = []
                for i in x:
                    if i != "," and i != "[" and i != "]":
                        y.append(i)
                x = y
            except ValueError:
                try:
                    x = dict(x)
                except ValueError:
                    pass
    return x