import datetime

data_atual = datetime.datetime.now()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print("Data:",data_em_texto)
horario= data_atual.strftime('%H:%M')
print("Hora: ",horario)