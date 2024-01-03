texto: int
numero: int
numero2: int
resultado: int =0

# intput-recebe textos idependente do que for
print("Digite o seu nome")
nome= input ()
print("-=-=-=-=-")

#eval+input- recebe textos idependente do que for
print("Digite o primeio numero")

numero=eval(input())
print("Digite o segundo numero")

numero2=eval(input())

resultado=numero+numero2

print("=-=-=-=-")
print("O seu nome",nome)
print("O resultado e ",resultado)

if resultado >5:
    print("O resultado e maior que 5")
if resultado==5:
    print("O resultado e igual a 5")
if resultado<5:
    print("O resultado e menor que 5")
if resultado==0:
    print("O resultado e igual a 0")
