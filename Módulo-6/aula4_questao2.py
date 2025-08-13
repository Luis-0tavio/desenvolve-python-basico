frase=input("Digite uma frase: ").lower()
vogais = sorted([letra for letra in frase if letra in "aeiou" ])
consoantes= [letra1 for letra1 in frase if letra1 in "bcdfghjklmnpqrstvwxyz" ]
print(vogais)
print(consoantes)