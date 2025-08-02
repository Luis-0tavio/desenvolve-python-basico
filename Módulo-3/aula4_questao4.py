peso=float(input("Digite o peso do pacote: "))
dist=float(input("Digite a distancia de entrega: "))
if(dist<100):
    valor=peso
elif(dist<300):
    valor=peso*1.5
else:
    valor=peso*2
if(peso>10):
    valor+=10
print("O valor do frete é: ", valor)