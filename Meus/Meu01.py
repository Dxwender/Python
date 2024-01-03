numero1: int
numero2: int
numero3: int

resultado: int

print("Digite um numero")
numero=eval(input())

print("Digite outro numero")
numero2=eval(input())

print("Digite o numero para comparacao")
numero3=eval(input())

resultado=numero+numero2
resultado+=1
print("A soma e: ", resultado)

if resultado<numero3 :
    print("O numereo e menor que o numero de comparacao")
if resultado==numero3 :
    print("O numero e igual ao numero de comparacao")
if resultado>numero3 :
    print("O numero e maior ao numero de comparacao")