import os

linha=[]

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "meus_livros.csv")),'a',encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")

    for i in range(10):
        linha+=[input(f"Digite o título do livro {i+1}: ")]
        linha+=[input(f"Digite o autor do livro {i+1}: ")]
        linha+=[input(f"Digite o ano de publicação do livro {i+1}: ")]
        linha+=[input(f"Digite o número de páginas do livro {i+1}: ")+"\n"]
        f.write(",".join(linha))
        linha=[]
    