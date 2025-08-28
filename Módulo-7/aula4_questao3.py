import os 

n_lin=0
maior_n=0
linha_maior=""
mencao=0

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "estomago.txt")),'r',encoding="utf-8") as f:
    for i in range(20):
        print(f.readline().strip())

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "estomago.txt")),'r',encoding="utf-8") as f:
    linhas=f.readlines()
    for linha in linhas:
        n_lin+=1
        if len(linha)>maior_n:
            maior_n=len(linha)
            linha_maior=linha
    print(f"\nO número de linhas é: {n_lin}")

    print(f"\nA maior linha é: {linha_maior}")

    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "estomago.txt")),'r',encoding="utf-8") as f:
        for linha in f:
        
            linha = linha.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ")

            palavras = linha.lower().split()  # divide em palavras
            for palavra in palavras:
                if palavra == "nonato":
                    mencao += 1
                if palavra == "íria":
                    mencao += 1

    print(f"O número de menções de \"Nonato\" ou \"Íria\" é: {mencao}")