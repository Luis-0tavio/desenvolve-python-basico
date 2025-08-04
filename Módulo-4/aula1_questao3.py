n1=int(input("Digite um numero n1: "))
n2=int(input("Digite um numero n2: "))
n3=int(input("Digite um numero n3: "))
m=(n1+n2+n3)/3
if (m>=60):
    print("Aprovado")
elif(m>=40):
    print("Recuperação")
else:
    print("Reprovado") 
print("Fim")