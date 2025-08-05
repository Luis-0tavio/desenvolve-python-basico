import random
n_rand=random.randint(1,10)
n=int(input("Adivinhe o número entre 1 e 10: "))
while (n!=n_rand):
    if(n>n_rand):
        print("Muito alto, tente novamente!")
    elif(n<n_rand):
        print("Muito baixo, tente novamente!")
    n=int(input("Adivinhe o número entre 1 e 10: "))    
print(f"Correto! O número é: {n_rand}")