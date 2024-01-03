peso: float
altura: float
imc:float

print("Digite o seu peso")
peso=eval(input())

print("Digite a sua altura")
altura=eval(input())

imc=peso/altura**2

if imc<18.5:
    print("Seu IMC e: ",imc,"e voce esta abaixo do peso")
else:
    if imc >= 18.6 and imc < 24.9:
        print("Seu IMC e: ", imc, "e voce esta no peso ideal")
    