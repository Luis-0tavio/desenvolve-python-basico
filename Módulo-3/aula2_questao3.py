idade=int(input("Digite sua idade: "))
ja_jogou=bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
qnts_venceu=int(input("Quantos jogos já venceu? "))
pode_entrar= (16>idade>18) and ja_jogou and qnts_venceu>=1
print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_entrar}")