frase=input("Digite uma frase: ").lower()

for vogal in "aeiou":
    frase = frase.replace(vogal, "*")
    
print(f"Frase modificada: {frase}")