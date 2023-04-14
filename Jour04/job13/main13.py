L = [10,20,30,20,10,50,60,40,80,50,40]
n = []
for simp in L:
  if simp not in n:
    n.append(simp)

print(n)