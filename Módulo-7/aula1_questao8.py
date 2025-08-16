CPF=input("Digite um CPF na forma XXX.XXX.XXX-XX: ")

CPF=CPF.replace(".", "").replace("-", "") # 012/345/678/9 10

#Primeiro digito verificador
soma=0
multp=10
for i in range(len(CPF)):
    if i==9:
        break
    soma+=(int(CPF[i])*multp)
    multp-=1

if soma%11<2:
    PDV=0
else:
    PDV=(11-(soma%11))

if int(CPF[-2])!=PDV:
    print("Inválido!")
    quit()

#Segundo dígito verificador
soma=0
multp=11
for i in range(len(CPF)):
    if i==10:
        break
    soma+=(int(CPF[i])*multp)
    multp-=1
    
if soma%11<2:
    SDV=0
else:
    SDV=(11-(soma%11))

if int(CPF[-1])!=SDV:
    print("Inválido!")
    quit()

print("Válido")