mot = input("Entrez un mot sans espace ni caractère spécial : ")
mot = mot.lower()  # convertir le mot en minuscules

# Vérifier que le mot contient uniquement des lettres de l'alphabet
if not mot.isalpha():
    print("Le mot ne doit contenir que des lettres de l'alphabet !")
else:
    # Convertir le mot en une liste de caractères
    liste_mot = list(mot)

    # Parcourir la liste de droite à gauche pour trouver les caractères à déplacer
    for i in range(len(liste_mot)-1, 0, -1):
        if liste_mot[i] < liste_mot[i-1]:
            # Le caractère courant est plus petit que le précédent, on le déplace
            # à sa place dans l'ordre alphabétique
            j = i
            while j < len(liste_mot) and liste_mot[j] < liste_mot[i-1]:
                j += 1
            liste_mot[i-1], liste_mot[j-1] = liste_mot[j-1], liste_mot[i-1]
            # On trie les caractères restants dans l'ordre croissant
            liste_mot[i:] = sorted(liste_mot[i:])
            break

    # Reconstituer le mot à partir de la liste de caractères
    mot_modifie = ''.join(liste_mot)
    print("Le mot modifié est : ", mot_modifie)