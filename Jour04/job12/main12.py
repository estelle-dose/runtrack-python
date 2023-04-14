L = [7, 11, 42, 39, 2]

def tri_liste(liste):
    n = 0
    for i in liste:
        n += 1

    for i in range(n):
        for j in range(i+1, n):
            if liste[j] < liste[i]:
                # Échange les valeurs de liste[i] et liste[j]
                temp = liste[i]
                liste[i] = liste[j]
                liste[j] = temp

tri_liste(L)
print(L)