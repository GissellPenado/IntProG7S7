numero=input("Dime un numero: ")

numeros=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
repetidos=[0, 0, 0, 0, 0, 0, 0, 0, 0]
for digito in numero:
    if digito == "0":
        repetidos[0] +=1
    elif digito == "1":
        repetidos[1] +=1
    elif digito == "2":
        repetidos[2] +=1
    elif digito == "3":
        repetidos[3] +=1    
    elif digito == "4":
        repetidos[4] +=1
    elif digito == "5":
        repetidos[5] +=1
    elif digito == "6":
        repetidos[6] +=1
    elif digito == "7":
        repetidos[7] +=1
    elif digito == "8":
        repetidos[8] +=1
    elif digito == "9":
        repetidos[9] +=1
    
for i, j in zip(numeros, repetidos):
    print(i,j)