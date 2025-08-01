larg=int(input("Digite a largura do terreno:"))
comp=int(input("Digite o comprimento do terreno:"))
prec=float(input("Digite o preço do m² do terreno:"))
#calculo da area do terreno
area_m2 = comp * larg
#calculo do preco do terreno
preco_total = prec * area_m2
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
