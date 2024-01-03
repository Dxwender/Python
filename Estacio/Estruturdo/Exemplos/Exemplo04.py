unidadesProduto: int=0


while unidadesProduto>=1 or unidadesProduto<=100 :
  unidadesProduto = eval(input("Digite as unidades que desja comprar"))
  if unidadesProduto >= 20 and unidadesProduto<=100:
        print("Voce tera o desconto de 20% e vai pagar",unidadesProduto*10-(unidadesProduto*0.02))
  elif unidadesProduto >=11 and unidadesProduto<20 :
        print("Voce tera o desconto de 10% e vai pagar",unidadesProduto*10-(unidadesProduto*0.01))
  elif unidadesProduto >=1 and unidadesProduto< 11 :
        print("Voce não tera o desconto e vai pagar",unidadesProduto*10)
  else:
        print("Error")
        break
