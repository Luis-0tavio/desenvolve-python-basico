num = input("Digite o número: ")

if len(num) == 8:
    num = "9" + num

num = num[:5] + "-" + num[5:]

print(f"Número completo: {num}")