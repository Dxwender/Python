acumuladorHotDog:int=0
acumuladorHamburguer:int=0
acumuladorCheeseburguer:int=0
acumuladorRefrigerante:int=0

acumuladorquantidadeHotDog:int=0
acumuladorquantidadeHamburguer:int=0
acumuladorquantidadeCheeseburguer:int=0
acumuladorquantidadeRefrigerante:int=0

print("Produtos:\n100-HotDog\n101-Hambúrguer\n102-Cheeseburguer\n103-Refrigerante\n0-Conta\n=======")
produtos=eval(input('Digite o seu produto:'))
print("=======")
while produtos>=100 and produtos<=104:
    if produtos==100:
        print("Hot Dog:")
        quantidadeHotDog=eval(input("Digite a quantidade de Hot Dog por favor:"))
        acumuladorquantidadeHotDog=acumuladorquantidadeHotDog+quantidadeHotDog
        totalHotdog=quantidadeHotDog*1.2
        acumuladorHotDog=acumuladorHotDog+totalHotdog
        print("=======\nProdutos:\n100-HotDog\n101-Hambúrguer\n102-Cheeseburguer\n103-Refrigerante\n0-Conta\n=======")

    elif produtos==102:
        print("Hambúrguer:")
        quantidadeHamburguer = eval(input("Digite a quantidade de Hot Dog por favor:"))
        acumuladorquantidadeHamburguer=acumuladorquantidadeHamburguer+quantidadeHamburguer
        totalHamburguer = quantidadeHamburguer * 1.2
        acumuladorHamburguer = acumuladorHamburguer+totalHamburguer
        print("=======\nProdutos:\n100-HotDog\n101-Hambúrguer\n102-Cheeseburguer\n103-Refrigerante\n0-Conta\n=======")

    elif produtos==103:
        print("Cheeseburguer")
        quantidadeCheeseburguer = eval(input("Digite a quantidade de Hot Dog por favor:"))
        acumuladorquantidadeCheeseburguer=acumuladorquantidadeCheeseburguer+quantidadeCheeseburguer
        totalCheeseburguer = quantidadeCheeseburguer * 1.3
        acumuladorCheeseburguer = acumuladorCheeseburguer+totalCheeseburguer
        print("=======\nProdutos:\n100-HotDog\n101-Hambúrguer\n102-Cheeseburguer\n103-Refrigerante\n0-Conta\n=======")

    elif produtos==104:
        print("Refrigerante")
        quantidadeRefrigerante = eval(input("Digite a quantidade de Hot Dog por favor:"))
        acumuladorquantidadeRefrigerante=acumuladorquantidadeRefrigerante+quantidadeRefrigerante
        totalRefrigerante = quantidadeRefrigerante * 1.3
        acumuladorRefrigerante = acumuladorRefrigerante + totalRefrigerante
        print("=======\nProdutos:\n100-HotDog\n101-Hambúrguer\n102-Cheeseburguer\n103-Refrigerante\n0-Conta\n=======")

    produtos = eval(input('Digite o seu produto:'))
    print("=======")
print("Nota fiscal:")
print("Produto---Quantidade comprada---Valor---")
print("Hambúrguer---",acumuladorHotDog,"---",acumuladorquantidadeHotDog)
print("Cheeseburguer---",acumuladorCheeseburguer,"---",acumuladorquantidadeCheeseburguer)
print("Refrigerante---",acumuladorRefrigerante,"---",acumuladorquantidadeRefrigerante)
print("Total       ---",(acumuladorHotDog+acumuladorHamburguer+acumuladorCheeseburguer+acumuladorRefrigerante),
                   "---",(acumuladorquantidadeCheeseburguer+acumuladorquantidadeHamburguer+acumuladorquantidadeCheeseburguer+acumuladorquantidadeRefrigerante))