import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))

caminho = os.path.join(pasta_atual, "frase.txt")
frase = input("Digite uma frase: ")
with open(caminho, "w", encoding="utf-8") as f:
    f.write(frase)

print("Frase salva em ", caminho)