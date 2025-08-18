data=input("Digite uma data de nascimento (dd/mm/aaaa): ")
meses=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes=int(data[3:5])-1
print(f"Você nasceu em {data[0:2]} de {meses[mes]} de {data[-4:]}.")