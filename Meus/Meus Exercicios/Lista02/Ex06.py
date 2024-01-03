candito1:int=0
candito2:int=0
candito3:int=0
nulo:int=0
branco:int=0

voto:int
voto=eval(input("===Digite qualquer numero para começar==="))
while voto>=1 and voto<=5:
    voto = eval(input("===Por favor digite seu voto:\n1-Cândito 1\n2-Cândito 2\n3-Cândito 3"
                                                   "\n4-Nulo\n5-Branco\n0-Contagem\nVoto:"))
    if voto==1:
        candito1=candito1+1
        print("===Voce voltou no Cândito 1===")
    elif voto==2:
        candito2 = candito2 + 1
        print("===Voce voltou no Cândito 2===")
    elif voto==3:
        candito3 = candito3 + 1
        print("===Voce voltou no Cândito 3===")
    elif voto==4:
        nulo = nulo + 1
        print("===Voce voltou em Nulo===")
    elif voto==5:
        branco = branco + 1
        print("===Voce voltou em Branco===")
    else:
        totalCanditos=(candito1+candito2+candito3)

        porcetagemBranco= totalCanditos/(branco*100)
        porcetagemNulo=totalCanditos/(nulo*100)


        print("===\nContagem de votos\nCandiato 1:",candito1,"\nCandito 2:",candito2,"\nCandito 3:",candito3,
                                "\nNulo:",nulo,"\nBranco:",branco,"\nPorcentagem votos Brancos:",porcetagemBranco,
                                "\nPorcentagem voto Nulo:",porcetagemNulo,"\n===")