dia:int
mes:int
ano:int

dia=eval(input("Por favor digite o Dia:"))
mes=eval(input("Por favor digite o Mes:"))
ano=eval(input("Por favor digite o Ano:"))

if dia<1 or dia>31:
    print("Dia invalido")
elif mes<1 or mes>12:
    print("Mes invalido ")
elif ano<1940 or ano>2023:
    print("Ano invalido")
else:
    print("Data valida")