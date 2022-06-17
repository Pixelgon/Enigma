name = str(input("Zadejte název souboru(cely): "))
file = open(name, "r")
filedic = {}
ukon = int(input("Zadejte co chcete dělat(1 sifrovat, 2 desifrovat, 3 overit):"))


def cypher(text, filedic):
    for char, initial in filedic.items():
        text = text.replace(char, initial)
    return text

def overeni_klicu(dic):


if ukon == 1:
    for x in file:
        key, value = x.split()
        filedic[key] = value
    file.close()
    text = str(input("Zadejte text:"))
    print("Zašifrovaný text je:", cypher(text, filedic))
    exit()
if ukon == 2:
    for x in file:
        value, key = x.split()
        filedic[key] = value
    file.close()
    text = str(input("Zadejte text: "))
    print("Dešifrovaný texte je:", cypher(text, filedic))
    exit()
if ukon == 3:
    print(overeni_klicu(filedic))
    exit()