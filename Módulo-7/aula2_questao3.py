FOriginal = input("Digite uma frase (digite \"fim\" para encerrar): ").lower()

while FOriginal != "fim":
    
    frase = FOriginal
    for letra in " !?:;,":
        frase = frase.replace(letra, "")

    if frase == frase[::-1]:
        print(f"\"{FOriginal}\" é palíndromo!")
    else:
        print(f"\"{FOriginal}\" não é palíndromo!")

    FOriginal = input("Digite uma frase (digite \"fim\" para encerrar): ").lower()