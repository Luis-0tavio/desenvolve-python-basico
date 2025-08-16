frase=(input("Digite uma frase: ")).lower()
Vog=0
indiceVog=[]
for i in range(len(frase)):
    if frase[i] in "aeiou":
        Vog+=1
        indiceVog+=[i]
print(f"Vogais: {Vog}")
print(f"Índices: {indiceVog}")