# Opdracht 3 input functie
# Naam student: Arjan Mast
# Groep: ITX1

# Hier komt je code...
def get_input():
    print("We willen nu graag uw 5 favoriete steden weten")
    stad1 = input("Noem een stad naar keuze: ")
    stad2 = input("Noem nog een stad naar keuze: ")
    stad3 = input("Noem nog een stad naar keuze: ")
    stad4 = input("Noem nog een stad naar keuze: ")
    stad5 = input("Noem een laatste stad naar keuze: ")
    steden= sorted([stad1,stad2,stad3,stad4,stad5], reverse=True)
    print("zijn dit uw steden?",steden )
get_input()
def Eind():
    confirm = input("Type Y als u wilt doorgaan, Typ N als u terug wilt gaan")
    while True:
        if confirm == "Y":
            print("Veel plezier")
            break
        else:
            return get_input(), Eind()
Eind()
