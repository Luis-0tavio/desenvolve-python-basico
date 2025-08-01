input("Digite o nome do produto 1: ")
p1=float(input("Digite o preço unitário do produto 1: "))
p1=p1*(int(input("Digite a quantidade do produto 1: ")))

input("Digite o nome do produto 2: ")
p2=float(input("Digite o preço unitário do produto 2: "))
p2=p2*(int(input("Digite a quantidade do produto 2: ")))

input("Digite o nome do produto 3: ")
p3=float(input("Digite o preço unitário do produto 3: "))
p3=p3*(int(input("Digite a quantidade do produto 3: ")))
print(f"Total: R${(p1+p2+p3):,.2f}")