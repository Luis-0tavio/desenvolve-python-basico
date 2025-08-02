genero=input("Digite seu gênero(M ou F) : ")
idade=int(input("Digite sua idade: "))
tmp_serv=int(input("Digite seu tempo de serviço(anos): "))

pode_aposentar= ((genero  == "F") and idade>60) or ((genero  == "M") and idade>65) or tmp_serv>=30 or (idade>=60 and tmp_serv>=25)
print("Pode aposentar? ",pode_aposentar)