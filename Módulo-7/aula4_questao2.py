import os 

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "frase.txt")),'r',encoding="utf-8") as f:
    frase=f.read()
    frase=frase.replace(",","").replace(".","")

frase=frase.split(" ")
with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "palavras.txt")),'w',encoding="utf-8") as f:
    for palavra in frase:
        f.write(palavra)
        print(palavra)
