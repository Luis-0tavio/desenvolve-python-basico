import random
def encrypt(nomes):
    nomes_cript=[]
    novo_nome=""
    cod=random.randint(0,10)
    for nome in nomes:
        
        for letra in nome:
            novo_codigo = ord(letra) + cod
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            novo_nome += chr(novo_codigo)
        
        nomes_cript+=[novo_nome]
        novo_nome=""
    return nomes_cript,cod

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript,cod=encrypt(nomes)
print(f"Chave de criptografia = {cod}\nnomes_cript = {nomes_cript}")