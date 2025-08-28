import os
import random

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "gabarito_forca.txt")),'r',encoding="utf-8") as f:
    palavra=f.readlines()
    palavra=palavra[random.randint(0,9)]

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "gabarito_enforcado.txt")),'r',encoding="utf-8") as f:
    linhas= f.readlines()
    estagio=[linhas[0:5],linhas[5:10],linhas[10:15],linhas[15:20],linhas[20:25],linhas[25:30],linhas[30:35]]

temletra = False
erros=1
for linha in estagio[0]:
    print(linha)
progresso=["_"] * (len(palavra.strip()))

while (erros<7):
    
    print("".join(progresso))
    char=input("Digite uma letra: ")
    for i in range(len(palavra)):
        if char==palavra[i]:
            progresso[i]=palavra[i]
            temletra=True
    if not temletra: 
        for linha in estagio[erros]:
            print(linha)
        erros+=1
    if erros==7:
        print(f"A paravra era: {palavra.strip()}\nVocê perdeu!")
        quit()
    if "".join(progresso) == palavra.strip():
        print(f"A paravra era: {palavra}\nVocê ganhou!")
        quit()
    temletra=False
