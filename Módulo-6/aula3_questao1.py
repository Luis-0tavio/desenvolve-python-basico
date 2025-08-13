print("Digite mais de 4 números: ( \"0\" para parar a inserção)")
lista=[]
x=int(input())
lista+=[x]
x=int(input())
lista+=[x]
x=int(input())
lista+=[x]
x=int(input())
lista+=[x]
while(x!=0):
    x=int(input())
    if (x==0):
        break
    else:
        lista+=[x]
print(f"A lista original é: {lista}")
print(f"Os três primeiros elementos são: {lista[:3]}")
print(f"Os 2 últimos elementos são: {lista[-2:]}")
print(f"A lista invertida (do fim para o começo) é: {lista[::-1]}")
print(f"Os elementos de índice par (0, 2, 4 … ) são: {lista[::2]}")
print(f"Os elementos de índice ímpar (1, 3, 5, … ) são: {lista[1::2]}")