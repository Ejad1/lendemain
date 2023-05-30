import os

print("Bienvenu sur le programme d'affichage du jour prochain")
# Liste contenant les mois de l'année
MOIS = {
    "Janvier": 31,
    "Février": 28,
    "Mars": 31,
    "Avril": 30,
    "Mai": 31,
    "Juin": 30,
    "Juillet": 31,
    "Août": 31,
    "Septembre": 30,
    "Octobre": 31,
    "Novembre": 30,
    "Décembre": 31,
}


# Fonction vérifiant le jour entré par l'utilisateur
def verifi_jour(max):
    jour = input("Veuillez entrer le jour : ")
    if jour.isdigit():
        jour = int(jour)
        if jour <= 0:
            print("Vous n'avez pas entrer un jour valide")
            return verifi_jour(max)
        if jour > max:
            print("Le jour entré est supérieur à la limite des jours du mois")
            return verifi_jour(max)
        else:
            return jour
    else:
        print("Vous n'avez pas entrer un nombre valide pour le jour")
        return verifi_jour(max)


# Fonction vérifiant l'année entré par l'utilisateur
def verifi_annee():
    annee = input("Veuillez entrer l'année : ")
    if not annee.isdigit():
        print("Vous n'avez pas entrer une année valide")
        return verifi_annee()
    else:
        return annee


# Fonction vérifiant le mois entré par l'utilisateur
def verifi_mois():
    mois = input("Entrer le mois: ")
    mois = mois.capitalize()
    if mois in MOIS:
        return mois
    else:
        print("Vous n'avez pas entré un mois valide")
        return verifi_mois()


# Boucle permettant à l'utilisateur de recommencer
rep = "O"
while rep == "O":
    annee = int(verifi_annee())
    mois = verifi_mois()
    max = MOIS[mois]
    jour = int(verifi_jour(max))

    # Affichage du jour entré
    print(f"\nLe jour entré est {jour} {mois} {annee} \n")

    # Affichage du jour suivant en distinguant les cas
    if jour < max:
        print("Le jour suivant est : ", jour + 1, mois, annee, "\n")
    else:
        if mois == "Décembre":
            print("Le jour suivant est : 1er Janvier ", annee + 1, "\n")
        else:
            indice = 0
            trouve = -2023
            for i in MOIS:
                indice += 1
                if mois == i:
                    trouve = indice
                if indice == trouve + 1:
                    mois_chercher = i
                    print("Le jour suivant est : 1er ", mois_chercher, annee, "\n")
                    break

    rep = input(
        "Voulez-vous continuer ? (entrez O pour oui et tout autre chose pour quitter) : "
    )
    rep = rep.upper()


os.system("pause")
