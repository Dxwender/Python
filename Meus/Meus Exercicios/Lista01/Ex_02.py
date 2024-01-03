lado1 = eval(input("Digite o primeiro lado"))
lado2 = eval(input("Digite o segundo lado"))
lado3 = eval(input("Digite o terceiro lado"))

if lado1==lado2==lado3:
    print("E um triangulo equilatero")
elif lado1==lado2 or lado2==lado3 or lado3==lado1:
    print("E um triangulo Isoceles")
else:
    print("E um triangulo Escaleno")