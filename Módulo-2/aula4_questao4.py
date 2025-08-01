reais=(int(input("Digite o valor: ")))
print(f"{int(reais/100)} nota(s) de R$100,00")
reais=reais%100
print(f"{int(reais/50)} nota(s) de R$50,00")
reais=reais%50
print(f"{int(reais/20)} nota(s) de R$20,00")
reais=reais%20
print(f"{int(reais/10)} nota(s) de R$10,00")
reais=reais%10
print(f"{int(reais/5)} nota(s) de R$5,00")
reais=reais%5
print(f"{int(reais/2)} nota(s) de R$2,00")
reais=reais%2
print(f"{reais} nota(s) de R$1,00")