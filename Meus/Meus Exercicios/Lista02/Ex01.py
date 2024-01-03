idade:int

ate15anos:int=0
somaate15anos:int=0
mediaate15anos:int=0

entre16e30:int=0
somaentre16e30:int=0
mediaentre16e30:int=0

entre31e45:int=0
somaentre31e45:int=0
mediaentre31e45:int=0

entre46e60:int=0
somaentre46e60:int=0
mediaentre46e60:int=0

maior60:int=0
somaacima60anos:int=0
mediaacima60anos:int=0

for i in range (5):
    idade=eval(input("Digite sua idade"))
    if idade<=15:
       ate15anos=ate15anos+1
       somaate15anos=somaate15anos+idade
       mediaate15anos=somaate15anos//ate15anos

    elif idade>=16 and idade<30:
        entre16e30=entre16e30+1
        somaentre16e30 = somaentre16e30 + idade
        mediaentre16e30 = somaentre16e30 // entre16e30

    elif idade>=31 and idade<45:
        entre31e45=entre31e45+1
        somaentre31e45 = somaentre31e45 + idade
        mediaentre31e45 = somaentre31e45 // entre31e45

    elif idade>=46 and idade<60:
        entre46e60=entre46e60+1
        somaentre46e60 = somaentre46e60 + idade
        mediaentre46e60 = somaentre46e60 // entre46e60

    else:
        maior60=maior60+1
        somaacima60anos = somaacima60anos + idade
        mediaacima60anos = somaacima60anos // maior60


print("Pessoas com idade ate 15 anos:",ate15anos,"/A media de idade e:",mediaate15anos)
print("Pessoas com idade entre 16 anos e 30 anos",entre16e30,"/A media de idade e:",mediaentre16e30)
print("Pessoas com idade entre 31 anos e 45 anos",entre31e45,"/A media de idade e:",mediaentre31e45)
print("Pessoas com idade entre 46 anos e 60 anos",entre46e60,"/A media de idade e:",mediaentre46e60)
print("Pessoas com idade acima 60 anos ",maior60,"/A media de idade e:",mediaacima60anos)