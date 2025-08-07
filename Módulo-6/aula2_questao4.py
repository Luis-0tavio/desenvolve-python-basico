lista1=[]
lista2=[]
inter=[]

n_ele_1=int(input("Digite a quantidade de elementos da lista 1: "))
for i in range(0,n_ele_1,1):
    lista1+=[int(input())]

n_ele_2=int(input("Digite a quantidade de elementos da lista 2: "))
for i in range(0,n_ele_2,1):
    lista2+=[int(input())]


for i in range(0,(len(lista1)+len(lista2)),1):
    if (len(lista1)>i):
        inter+=[lista1[i]]
    if (len(lista2)>i):
        inter+=[lista2[i]]

print(f"Lista intercalada: {inter}")
    