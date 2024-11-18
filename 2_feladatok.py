def feladat_1():
    sztring = "IMSERED EZTA SZAMOT"
    sztring[0] = "i"

    lista = ["I", "s", "m", "e", "r", "e", "d"]
    print(lista)
    lista[0] = "1"
    print(lista)

def feladat_2():
    while True:
        u_input = input("Kérlek adj meg egy mondatot, vagy ha befejeznéd üss entert! ")
        if u_input[-1] == ".":
            print("Eu a mondat kijelentő! ")
        if u_input[-1] == "!":
            print("Ez a mondat felszólító/felkiáltó/óhajtó!w ")
        if u_input[-1] == "?":
            print("Ez a mondat kérdő! ")
        else:
            print("Nincs mondatvégi írásjel! ")


feladat_2()