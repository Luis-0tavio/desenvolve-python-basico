import random
lista=[]
for i in range(20):
    lista+=[random.randint(-10,10)]
print(f"Original: {lista}")
inicio=0
fim=0
tam=0
for i in range(20):
    if (lista[i]<0):
        for j in range(i,20,1):
            if (lista[j]<0):
                if (tam<(j-i)):
                    tam=j-i+1
                    inicio=i
                    fim=j
            else:
                break
del(lista[inicio:fim+1])
print(f"Editada: {lista}")