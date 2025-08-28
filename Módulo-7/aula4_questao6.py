import os
import csv

ranking=[]

with open((os.path.join(os.path.dirname(os.path.abspath(__file__)), "spotify-2023.csv")), encoding='latin-1') as f:
    leitor = csv.reader(f)   
    next(leitor)
    
    for linha in leitor:
        if 2012<=int(linha[3]) and int(linha[3])<=2022:
            ranking+=[[linha[0],linha[1],linha[2],int(linha[3]),int(linha[8])]]
    
    ranking=sorted(ranking, key=lambda x: x[4],reverse=True) 
    
    for linha in ranking[:10]:
        print(linha)

#Tive que alterar um valor no arquivo spotify-2023.csv, pois estava com o número de streams "corrompido"