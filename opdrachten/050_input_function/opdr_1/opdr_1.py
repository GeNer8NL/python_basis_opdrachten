# Opdracht 1 input function
# Naam student:
# Groep:


# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

Zijde1 = float(input("Geef de lengte van de eerste zijde: "))
Zijde2 = float(input("Geef de lengte van de tweede zijde: "))
eind = Zijde1 ** 2 + Zijde2 ** 2
antwoord = math.sqrt(eind)
afgerond = round(antwoord, 2)
print("De lengte van de schuine zijde is", afgerond)
