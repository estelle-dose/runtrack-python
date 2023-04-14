chaine="abcdefghijklmnopqrstuvwxyz" * 10

n=1

while n <= len(chaine):
    print(chaine[:n])
    chaine=chaine[n:]
    n+=1