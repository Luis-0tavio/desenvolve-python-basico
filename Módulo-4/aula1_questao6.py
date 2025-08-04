n_exp=int(input("Digite o número de experimentos realizados: "))
c=0
r=0
s=0
i=0
while(i<n_exp):
    i+=1
    qnt=int(input(f"Digite a quantia de cobaias do experimento {i}: "))
    tipo=input(f"Digite o tipo das cobaias do experimento {i}: ")
    if(tipo == 'C'):
        c+=qnt
    elif(tipo == 'R'):
        r+=qnt
    else:
        s+=qnt
print(f"Total: {c+r+s} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {c*100/(c+r+s):.2f} %")
print(f"Percentual de ratos: {r*100/(c+r+s):.2f} %")
print(f"Percentual de sapos: {s*100/(c+r+s):.2f} %")