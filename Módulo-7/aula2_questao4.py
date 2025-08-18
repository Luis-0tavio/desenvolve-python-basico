def validador_senha(senha):
    ma=False
    mi=False
    n=False
    s=False
    tam=False
    if len(senha)<8:
            return False
    for letra in senha:
        if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ma=True
        if letra in "abcdefghijklmnopqrstuvwxyz":
            mi=True
        if letra in "1234567890":
            n=True
        if letra in "@#$!&*":
            s=True
        
    return(ma and mi and n and s)

# Exemplo de uso:

senha1 = "Senha123@"

senha2 = "senhafraca"

senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True

print(validador_senha(senha2))  # Saída esperada: False

print(validador_senha(senha3))  # Saída esperada: False