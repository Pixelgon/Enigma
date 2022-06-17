name = str(input("Zadejte název souboru(cely): "))
file = open(name, "r")
filedic = {}
ukon = int(input("Zadejte co chcete dělat(1 sifrovat, 2 desifrovat, 3 overit):"))

for x in file:
    key, value = x.split()
    filedic[key] = value

def cypher(text, filedic, file):
    for char, initial in filedic.items():
        text = text.replace(char.lower(), initial)
    file.close()
    return text

if ukon == 1:
    text = str(input("Zadejte text: "))
    print(cypher(text, filedic, file))
if ukon == 2:
    text = str(input("Zadejte text: "))
    filedic.reverse()
    print(cypher(text, filedic, file))
if ukon == 3:
    exit()