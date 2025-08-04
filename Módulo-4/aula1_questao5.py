n=int(input("Digite a quantidade de respondentes: "))
soma=0
i=0
while (i<n):
    i+=1
    soma+=int(input(f"Digite a idade do respondente {i}: "))
    
print(f"A média das idades é: {soma/n}")