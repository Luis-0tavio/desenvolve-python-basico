import random
import math
n=int(input("Digite o numero de valores aleatórios: "))
soma=0

for i in range(0,n,1):
    soma+=random.randint(0,100)
print(round((math.sqrt(soma)),2))