frase=(input("Digite uma frase: ")).lower()
lista_pal=frase.split(" ")
frase_obj=sorted(input("Digite a palavra objetivo: "))
anag=[]
for palavra in lista_pal:
    if sorted(palavra) == frase_obj:
        anag+=[palavra]
print(anag)