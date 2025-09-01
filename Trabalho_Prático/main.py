import os
#-------------------------------------------------------------ADMIN--------------------------------------------------------------------------------
#Transforma o arquivo num dicionário com os usuarios
def ler_usuarios():
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.csv")),'r',encoding="utf-8") as f:
        usuarios={}
        users=f.readlines()
        for user in users:
            user=user.replace("\n","").split(",")
            usuarios[user[0]] = ((user[1]), user[2])

    return usuarios
#Adiciona um usuario
def adiciona_usuario(nome,senha,cargo):
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.csv")),'a',encoding="utf-8") as f:
        f.write(f"{nome},{senha},{cargo}\n")
        print(f"Usuario \"{nome}\" - {cargo} criado com sucesso!")
#Remove um usuario
def remove_usuario(nome):
    users=ler_usuarios()
    del users[nome]

    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.csv")),'w',encoding="utf-8") as f:
        f.write("")
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.csv")),'a',encoding="utf-8") as f:
        for user,info in users.items():
            f.write(f"{user},{info[0]},{info[1]}\n")
#Edita um usuario
def edita_usuario(nome,senha,cargo):
    users=ler_usuarios()
    users[nome]=(senha,cargo)

    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.csv")),'w',encoding="utf-8") as f:
        f.write("")
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.csv")),'a',encoding="utf-8") as f:
        for user,info in users.items():
            f.write(f"{user},{info[0]},{info[1]}\n")
#Verifica se um usuário existe
def usuario_existe(nome):
    produtos=ler_usuarios()
    if nome not in produtos:
        return False
    else:
        return True
#--------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------GERENTE------------------------------------------------------------------------------
#Transforma o arquivo num dicionário com os produtos
def ler_produtos():
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.csv")),'r',encoding="utf-8") as f:
        produtos={}
        produto=f.readlines()
        for tipo in produto:
            tipo=tipo.strip().replace("\n","").split(",")
            produtos[tipo[0]] = (int(tipo[1]), float(tipo[2]))

    return produtos
#Adiciona um produto
def adiciona_produto(nome,qnt,prec):
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.csv")),'a',encoding="utf-8") as f:
        f.write(f"{nome},{qnt},{prec}\n")
        print(f"Produto \"{nome}\" - {qnt} - {prec} criado com sucesso!")
#Remove um produto
def remove_produto(nome):
    users=ler_produtos()
    del users[nome]

    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.csv")),'w',encoding="utf-8") as f:
        f.write("")
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.csv")),'a',encoding="utf-8") as f:
        for user,info in users.items():
            f.write(f"{user},{info[0]},{info[1]}\n")
#Edita um produto
def edita_produto(nome,qnt,prec):
    users=ler_produtos()
    users[nome]=(qnt,prec)

    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.csv")),'w',encoding="utf-8") as f:
        f.write("")
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos.csv")),'a',encoding="utf-8") as f:
        for prodto,info in users.items():
            f.write(f"{prodto},{info[0]},{info[1]}\n")
#Verifica se um produto existe
def produto_existe(nome):
    produtos=ler_produtos()
    if nome not in produtos:
        return False
    else:
        return True
#Verifica se tem a quantidade do produto
def tem_quantidade(nome,qnt):
    produtos=ler_produtos()
    if (produtos[nome][0]-qnt)>=0:
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------FUNCIONARIOS---------------------------------------------------------------------------
#Realiza uma venda
def realiza_venda(nome,qnt,user):
    produtos=ler_produtos()
    edita_produto(nome,produtos[nome][0]-qnt,produtos[nome][1])
    with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "log-vendas.txt")),'a',encoding="utf-8") as f:
        f.write(f"Usuário:{user} Produto: {nome} Quantidade: {qnt}\n")
#----------------------------------------------------------------------------------------------------------------------------------------------------
#Login
def login(user,key):
    users=ler_usuarios()
    if user not in users:
        return False,0
    else:
        if users[user][0]==key:
            return True,users[user][1]
        else:
            return False,0
#----------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Gerenciar funcionários
def gerenciar_funcionarios():
    while True:
                print( BOLD+BLUE + "---------Gerenciar funcionários----------" + RESET)
                print(BOLD+YELLOW+ "1 - Adicionar funcionário"+ RESET)
                print(BOLD+YELLOW+ "2 - Remover funcionário "+ RESET)
                print(BOLD+YELLOW+ "3 - Editar funcionário "+ RESET)
                print(BOLD+YELLOW+ "4 - Ver todos funcionários "+ RESET)
                print(BOLD+YELLOW+ "5 - Voltar ao menu principal "+ RESET)
                opc1=int(input( BOLD+ "Digite a opção desejada: "+RESET))

                if   opc1==1:
                    while True:
                        print( BOLD+BLUE + "---------Adicionar funcionário----------" + RESET)
                        print(BOLD+YELLOW+ "1 - Adicionar funcionário "+ RESET)
                        print(BOLD+YELLOW+ "2 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        if opc2==1:
                            while True:
                                
                                while True:

                                    nome=input("Digite o nome do funcinário: ")
                                    if usuario_existe(nome):
                                        print("Usuário já existe! Tente outro nome")
                                    else:
                                        break

                                while True:
                                    cargo=input("Digite o cargo do funcionário: ")
                                    if cargo=="admin" or cargo=="gerente" or cargo=="funcionario":
                                        break
                                    else:
                                        print(BOLD+RED+"Cargo inexistente! Digite um dos cargos válidos: (admin,gerente ou funcionario) "+RESET)

                                while True:
                                    key=input("Digite a senha: ")
                                    key_confirm=input("Confirme a senha: ")
                                    if key!=key_confirm:
                                        print("As senhas não coincidem!")
                                    else:
                                        break
                                adiciona_usuario(nome,key,cargo)
                                print("Usuário adicionário!")
                                sure=input(f"Deseja adicionar outro usuário?(s/n) ").lower()
                                if sure=="n":
                                    break
                        else:
                            break
                elif opc1==2:
                    while True:
                        print( BOLD+BLUE + "---------Remover funcionário----------" + RESET)
                        print(BOLD+YELLOW+ "1 - Remover funcionário "+ RESET)
                        print(BOLD+YELLOW+ "2 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        if opc2==1:
                            while True:
                                nome=input("Digite o nome do funcinário: ")
                                if usuario_existe(nome):
                                    sure=input(f"Tem certeza que deseja remover o usuário {nome}? As alterações não podem ser desfeitas!(s/n) ").lower()
                                    if sure=="s":
                                        remove_usuario(nome)
                                        print("Usuário removido!")
                                        sure=input(f"Deseja remover outro usuário?(s/n) ").lower()
                                        if sure=="n":
                                            break
                                else:
                                    sure=(input("Usuário não encontrado! Deseja listar ver a lista de usuários?(s/n) ")).lower()
                                    if sure=="s":
                                        users=ler_usuarios()
                                        for nome, info in users.items():
                                            print(f"Nome: {nome} Cargo: {info[1]}")
                                    else:
                                        break
                        else:
                            break
                elif opc1==3:
                    while True:
                        print( BOLD+BLUE + "---------Editar funcionário----------" + RESET)
                        print(BOLD+YELLOW+ "1 - Editar funcionário (senha e cargo) "+ RESET)
                        print(BOLD+YELLOW+ "2 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        if opc2==1:
                            while True:
                                while True:
                                    nome=input("Digite o nome do funcinário: ")
                                    if usuario_existe(nome):
                                        key=input("Digite a nova senha: ")
                                        cargo=input("Digite o novo cargo: ")
                                        sure=(input(f"Tem certeza que deseja editar o usuário {nome}? As alterações não podem ser desfeitas!(s/n) ")).lower()
                                        if sure=="s":
                                            edita_usuario(nome,key,cargo)
                                            print("Usuário editado!")
                                            sure=(input(f"Deseja editar outro usuário?(s/n) ")).lower()
                                            if sure=="n":
                                                break
                                        else:
                                            break
                                        break
                                    else:
                                        sure=(input("Usuário não encontrado! Deseja listar ver a lista de usuários?(s/n) ")).lower()
                                        if sure=="s":
                                            users=ler_usuarios()
                                            for nome, info in users.items():
                                                print(f"Nome: {nome} Cargo: {info[1]}")
                                        else:
                                            break
                                break
                                        
                        else:
                            break
                elif opc1==4:
                    print( BOLD+BLUE + "-------Ver todos funcionários-------" + RESET)
                    users=ler_usuarios()
                    for pessoa,info in users.items():
                        print(f"Nome: {pessoa} - Senha: {info[0]} - Cargo: {info[1]}")
                else:
                    break       
#Gerenciar estoque
def gerenciar_estoque():
    while True:
                print( BOLD+BLUE + "---------Gerenciar estoque----------" + RESET)
                print(BOLD+YELLOW+ "1 - Adicionar produto"+ RESET)
                print(BOLD+YELLOW+ "2 - Remover produto "+ RESET)
                print(BOLD+YELLOW+ "3 - Editar produto "+ RESET)
                print(BOLD+YELLOW+ "4 - Ver todos produtos "+ RESET)
                print(BOLD+YELLOW+ "5 - Voltar ao menu principal "+ RESET)
                opc1=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                
                if   opc1==1:
                    while True:
                        print( BOLD+BLUE + "---------Adicionar produto----------" + RESET)
                        print(BOLD+YELLOW+ "1 - Adicionar produto "+ RESET)
                        print(BOLD+YELLOW+ "2 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        if opc2==1:
                            while True:
                                    nome=input("Digite o nome do produto: ")
                                    if produto_existe(nome):
                                        print("Produto já existe! Tente outro nome")
                                    else:
                                        break
                            qnt=int(input("Digite o quantidade do produto: "))
                            preco=float(input("Digite o preço do produto: "))
                            adiciona_produto(nome,qnt,preco)
                            print("Produto adicionado!")
                            sure=input(f"Deseja adicionar outro produto?(s/n) ").lower()
                            if sure=="n":
                                break
                        else:
                            break
                elif opc1==2:
                    while True:
                        print( BOLD+BLUE + "---------Remover produto----------" + RESET)
                        print(BOLD+YELLOW+ "1 - Remover produto "+ RESET)
                        print(BOLD+YELLOW+ "2 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        if opc2==1:
                            while True:
                                nome=input("Digite o nome do produto: ")
                                if produto_existe(nome):
                                    sure=input(f"Tem certeza que deseja remover o produto {nome}? As alterações não podem ser desfeitas!(s/n) ").lower()
                                    if sure=="s":
                                        remove_produto(nome)
                                        print("Produto removido!")
                                        sure=input(f"Deseja remover outro produto?(s/n) ").lower()
                                        if sure=="n":
                                            break

                                else:
                                    print("Produto não encontrado!")
                                    prod_disp=input("Deseja ver a lista de produtos?(s/n) ")
                                    if prod_disp=="s":
                                        users=ler_produtos()
                                        users=dict(sorted(ler_produtos().items()))
                                        for user,info in users.items():
                                            print(f"Nome: {user} - Quantidade: {info[0]} - Preço: {info[1]}")
                                        break
                                    else:
                                        break
                        if opc2==2:
                            break
                elif opc1==3:
                    while True:
                        print( BOLD+BLUE + "----------Editar produto-----------" + RESET)
                        print(BOLD+YELLOW+ "1 - Editar produto (quantidade e preço) "+ RESET)
                        print(BOLD+YELLOW+ "2 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        if opc2==1:
                            while True:
                                while True:
                                    nome=input("Digite o nome do produto: ")
                                    if produto_existe(nome):
                                        qnt=int(input("Digite a nova quantidade: "))
                                        preco=float(input("Digite o novo preço: "))
                                        sure=(input(f"Tem certeza que deseja editar o produto {nome}? As alterações não podem ser desfeitas!(s/n) ")).lower()
                                        if sure=="s":
                                            edita_produto(nome,qnt,preco)
                                            print("Produto editado!")
                                            sure=(input(f"Deseja editar outro produto?(s/n) ")).lower()
                                            if sure=="n":
                                                break
                                        else:
                                            break
                                    else:
                                        print("Produto não encontrado!")
                                        prod_disp=input("Deseja ver a lista de produtos?(s/n) ")
                                        if prod_disp=="s":
                                            users=ler_produtos()
                                            users=dict(sorted(ler_produtos().items()))
                                            for user,info in users.items():
                                                print(f"Nome: {user} - Quantidade: {info[0]} - Preço: {info[1]}")
                                            break
                                        else:
                                            break
                                    
                                break
                        else:
                            break               
                elif opc1==4:
                    while True:
                        print( BOLD+BLUE + "-------Ver todos produtos-------" + RESET)
                        print(BOLD+YELLOW+ "1 - Ordenados ordem alfabética "+ RESET)
                        print(BOLD+YELLOW+ "2 - Ordenados por preço "+ RESET)
                        print(BOLD+YELLOW+ "3 - Voltar "+ RESET)
                        opc2=int(input( BOLD+ "Digite a opção desejada: "+RESET))
                        users=ler_produtos()
                        if opc2==1:
                            users=dict(sorted(users.items()))
                        elif opc2==2:
                            users=dict(sorted(users.items(), key=lambda item: item[1][1]))
                        else:
                            break
                        for user,info in users.items():
                            print(f"Nome: {user} - Quantidade: {info[0]} - Preço: {info[1]}")
                
                else:
                    break
#Realizar venda
def venda(user):
    while True:
                print( BOLD+BLUE + "-----------Realizar venda------------" + RESET)
                print(BOLD+YELLOW+ "1 - Realizar venda"+ RESET)
                print(BOLD+YELLOW+ "2 - Voltar ao menu principal "+ RESET)
                opc1=int(input( BOLD+ "Digite a opção desejada: "+RESET))

                if opc1==1:
                    while True:
                        carrinho=0
                        print( BOLD+BLUE + "-----------Realizar venda------------" + RESET)
                        while True:
                            nome=input("Digite o nome do produto: ")
                            if produto_existe(nome):
                                qnt=int(input("Digite a quantidade do produto: "))
                                if tem_quantidade(nome,qnt):
                                    produtos=ler_produtos()
                                    carrinho+=produtos[nome][1]*qnt
                                    print(f"Total da compra: {carrinho}")
                                    realiza_venda(nome,qnt,user)
                                    cont=(input(f"Deseja adicionar outro produto à compra?(s/n) ")).lower()
                                    if cont=="n":
                                        print(f"O total da compra é: {carrinho:.2f}")
                                        break

                                else:
                                    produtos=ler_produtos()
                                    print(f"Quantidade do produto ultrapassa a quantidade no estoque, a quantidade disponível é {produtos[nome][0]}")
                            else:
                                print("Produto não encontrado!")
                                prod_disp=input("Deseja ver a lista de produtos?(s/n) ")
                                if prod_disp=="s":
                                    users=ler_produtos()
                                    users=dict(sorted(ler_produtos().items()))
                                    for user,info in users.items():
                                        print(f"Nome: {user} - Quantidade: {info[0]} - Preço: {info[1]}")
                                    break
                                else:
                                    break
                        break    
                else:
                    break
#----------------------------------------------------------------------------------------------------------------------------------------------------

#Personalização
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

#Login
while True:
    print( BOLD+BLUE + "------------------Login---------------------" + RESET)
    user=input(BOLD+GREEN+"Digite o nome de usuário: "+RESET)
    key=(input(BOLD+GREEN+"Digite a senha: "+RESET))
    verif,cargo=login(user,key)
    if verif:
        print(BOLD+BLUE+"------------Login Bem Sucedido!-------------"+RESET)
        break
    else:
        print(BOLD+RED +"-------Usuário ou senha incorretos!---------"+RESET)

#Login como admin
if cargo=="admin":
    while True:
        #Menu principal
        print( BOLD+BLUE + "------------------Menu----------------------" + RESET)
        print(BOLD+YELLOW+ "1 - Gerenciar funcionários "+ RESET)
        print(BOLD+YELLOW+ "2 - Gerenciar estoque "+ RESET)
        print(BOLD+YELLOW+ "3 - Realizar venda "+ RESET)
        print(BOLD+YELLOW+ "4 - Sair "+ RESET)
        opc=int(input( BOLD+ "Digite a opção desejada: "+RESET))

        if opc==1:
            gerenciar_funcionarios()
        elif opc==2:
            gerenciar_estoque()
        elif opc==3:
            venda(user)
        else:
            break

#Login como gerente
elif cargo=="gerente":
    while True:
        print( BOLD+BLUE + "------------------Menu----------------------" + RESET)
        print(BOLD+YELLOW+ "1 - Gerenciar estoque "+ RESET)
        print(BOLD+YELLOW+ "2 - Realizar venda "+ RESET)
        print(BOLD+YELLOW+ "3 - Sair "+ RESET)
        opc=int(input(BOLD+ "Digite a opção desejada: "+RESET))

        if opc==1:
            gerenciar_estoque()
        elif opc==2:
            venda(user)
        else:
            break

#Login como funcionário
else:
    while True:
        print( BOLD+BLUE + "------------------Menu----------------------" + RESET)
        print(BOLD+YELLOW+ "1 - Realizar venda "+ RESET)
        print(BOLD+YELLOW+ "2 - Sair "+ RESET)
        opc=int(input(BOLD+ "Digite a opção desejada: "+RESET))

        if opc==1:
            venda(user)
        else:
            break

print(BOLD+RED+ "Encerrando programa..."+RESET)