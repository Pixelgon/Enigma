# -----------------------------------------------------------
# Enigma: testovaci uloha
# Vytvoril Matej Matejka
# -----------------------------------------------------------


# Sifrovani x desifrovani
def cypher(message, dic):
    for char, initial in dic.items():
        message = message.replace(char, initial)
        return message


# Overeni slovniku
def verify(dic):
    prunik = dic.keys() & dic.values()
    sjednoceni = dic.keys() | dic.values()
    if len(prunik) == len(sjednoceni):
        return True
    return False


# Nacteni vstupu
name = str(input("Zadejte název souboru(cely): "))
file = open(name, "r")
filedic = {}
ukon = int(input("Zadejte co chcete dělat(1 sifrovat, 2 desifrovat, 3 overit, 4 ukončit): "))

# Sifrovani
if ukon == 1:
    for x in file:
        key, value = x.split()
        filedic[key] = value
    file.close()
    text = str(input("Zadejte text: "))
    print(f"Zašifrovaný text je: {cypher(text, filedic)}")
# Desifrovani
if ukon == 2:
    for x in file:
        value, key = x.split()
        filedic[key] = value
    file.close()
    text = str(input("Zadejte text: "))
    print(f"Dešifrovaný texte je: {cypher(text, filedic)}")
# Overeni slovniku
if ukon == 3:
    for x in file:
        key, value = x.split()
        filedic[key] = value
    file.close()
    if verify(filedic):
        print("Slovník je v pořádku")
    else:
        print("Slovník je vadný")
exit()
