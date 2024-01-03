nota : int=0

while nota >=1 or nota<=10 :
    nota = eval(input("Por favor digite sua nota:"))
    if   nota >= 7 and nota<=10:
        print("Voce esta aprovado")
    elif nota >=5 and nota<7 :
        print("Voce esta de recuperaçao.")
    elif nota >=1 and nota< 5 :
        print("Voce esta reprovado")
    else:
        print("Error")
        break