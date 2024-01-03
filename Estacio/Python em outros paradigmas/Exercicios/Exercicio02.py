lista_numeros =[9.56783,7.57568,3.00914,6.2321]

lista_precisao=[2,2,3,3]

arrendomento = lambda x,y : round(x,y)

resultado = list(map(arrendomento,lista_numeros,lista_precisao))

print(resultado)