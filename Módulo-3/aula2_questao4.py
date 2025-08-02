classe=input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pf=int(input("Digite os pontos de força (de 1 a 20): "))
pm=int(input("Digite os pontos de magia (de 1 a 20): "))

g= (classe == "guerreiro") and ((pf >= 15) and (pm <= 10))
m= (classe == "mago") and ((pf <= 10) and (pm >= 15))
a= (classe == "arqueiro") and (5 < pf <= 15) and (5 < pm <= 15)

valido= g or m or a

print("Pontos de atributo consistentes com a classe escolhida: ", valido)