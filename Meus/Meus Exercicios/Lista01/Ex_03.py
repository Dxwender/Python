angulo01= eval(input("Digite o primeiro numero"))
angulo02=eval(input("Digite o segundo angulo"))
angulo03=eval(input("Digite o segundo numero"))

if angulo01==90 or angulo02==90 or angulo03==90:
    print("E um triangulo retangulo")
elif angulo01>90 or angulo02>90 or angulo03>90 :
    print("E triangulo obtuso")
else:
    print("E um trianagulo agudo")