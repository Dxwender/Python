totalVista:float=0
pagamentoVista:float=0
contadorVista:int=0

totalPrazo:float=0
pagamentoPrazo:float=0
contadorPrazo:int=0

opcao=input("Digite V para vista/P para prazo/A para parar:")
while opcao=='v' or opcao=='p':
    if opcao == 'v':
        pagamentoVista=eval(input("Digite o valor do pagamento a vista:"))
        totalVista = totalVista + pagamentoVista
        contadorVista=contadorVista+1
    elif opcao == 'p':
        pagamentoPrazo = eval(input("Digite o valor do pagamento a prazo:"))
        totalPrazo = totalPrazo + pagamentoPrazo
        contadorPrazo=contadorPrazo+1
    else:
        break
    opcao = input("Digite V para vista/P para prazo/A para parar")

print("O total de vendas a vista foi: ",totalVista,"/ E a sua media e:",(totalVista/contadorVista))
print("O total de vendas a prazo foi: ",totalPrazo,"/ E a sua media e:",(totalPrazo/contadorPrazo))
print("A soma das vendas a Vista e Prazo são:",(totalVista+totalPrazo))