# revue des concepts de programmation
# 2021-11-09
# contexte - menu de choix

# CONSTANTES ##########################
Meal = True
TITRE = "Menu alimentaire"
BEAUTIFUL = " ~~~~~~~~~ "
choix = [
    "shawarma", 
    "lahme b3ajin", 
    "kafta",
    "farouj"
    ]

## afficher le menu
print(BEAUTIFUL + TITRE + BEAUTIFUL)
print()
for i in range(0, len(choix)) :
    print(f"{i} - {choix[i]}")

## prendre le choix de l'utilisateur


while Meal:
    print("Comment puis-je vous servir (Insérer le numéro associé au plat/écrivez le nom du plat/ ou insérer q pour quitter")
    choice = input("Je veux:").lower()
    print()
    if choice== "0" or choice== "shawarma":
        print("MMMMMM SHAWARMAAAA.. Quoi d'autre:")
    elif choice == "1" or choice== "lahme b3ajin":
        print("MMMMMM SAHTEIN... Quoi d'autre:")
    elif choice == "2" or choice== "kafta":
        print("MMMMMM SAHTEIN... Quoi d'autre:")
    elif choice == "3" or choice== "farouj":
        print("MMMMMM SAHTEIN... Quoi d'autre:")
    else:
        print("Bon appetit")
        Meal= False
        