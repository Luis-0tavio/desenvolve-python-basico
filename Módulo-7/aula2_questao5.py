import random
def embaralhar_palavras(frase):

    lista=frase.split(" ")
    embrlha=[]
    lista_mod=[]
    for palavra in lista:
        if len(palavra)>3:
            for letra in palavra[1:-1]:
                embrlha+=[letra]
            random.shuffle(embrlha)
            palavra=palavra[0]+"".join(embrlha)+palavra[-1]
            embrlha=[]
            lista_mod+=[palavra]
        else:
            lista_mod+=[palavra]

    return " ".join(lista_mod)

# Exemplo de uso:

frase = "Python é uma linguagem de programação"

resultado = embaralhar_palavras(frase)

print(resultado)

# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"