def mots_plus_longs(chaine, n):
    mots = []
    mot = ""
    for c in chaine:
        if c != " ":
            mot += c
        else:
            if len(mot) > n:
                mots += [mot]
            mot = ""
    if len(mot) > n:
        mots += [mot]
    return mots

chaine = "Le ciel est bleu aujourd'hui"
n = 3

liste_mots = mots_plus_longs(chaine, n)
print(liste_mots)