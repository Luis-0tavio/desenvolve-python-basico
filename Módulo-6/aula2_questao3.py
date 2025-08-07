import random
lista1=[]
lista2=[]
interseccao=[]

for i in range(0,20,1):
    lista1+=[random.randint(0,50)]
    lista2+=[random.randint(0,50)]

for i in range(0,50,1):
    if ((lista1.count(i)>0)and(lista2.count(i)>0)):
        interseccao+=[i]

print("lista1 - ",lista1)
print("lista2 - ",lista2)
print("Interseccao - ",interseccao)

print(f"Contagem:")
for i in range(0,len(interseccao),1):
    print(f"{interseccao[i]}: (lista1={lista1.count(interseccao[i])}, lista2={lista2.count(interseccao[i])})")