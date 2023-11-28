# Opdracht 2 berekeningen
# Naam student: Arjan Mast
# Groep: ITX1

# Hier komt je code...

# Deze code kon veel efficienter dan een vaste waarde. Daarom heb ik een interactieve calculator gemaakt


Eenheid = input("In welke eenheid rekenen we? Voor Celsius type C. Voor Fahrenheit type F: ")

if Eenheid == "C":
    c = int (input("Temperatuur in Celsius: "))
    Celsius = (c*9/5) + 32
    round(Celsius)
    print("dat is", round(Celsius), "Graden Fahrenheit")
elif Eenheid == "F" :
    f = int (input("Temperatuur in Fahrenheit: "))
    Fahrenheit = (f-32) * 5/9
    print("dat is", round(Fahrenheit), "Graden Celsius")
else:
    print("Ik begrijp U niet. Probeer het een hoofdletter")




