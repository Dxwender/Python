contagemMasculino:int=0
idadetotalMasclino:int=0
contagenmenoridadeMasculino:int=0
contagenmaioridadeMasculino:int=0
contagemgeralidadeMasculino:int=0
somaidadeMasculino:int=0
mediaidadeMasculino:float=0

contagemalturaMasculino:int=0
somaalturaMasculino:float=0


mediapesoMasculino:float=0
contagempesoMasculino:int=0
contagempessoasacima90Masculino:int=0
somapesoMasculino:float=0

contagemFeminino:int=0
idadetotalFeminino:int=0
contagenmenoridadeFeminino:int=0
contagenmaioridadeFeminino:int=0
contagemgeralidadeFeminino:int=0
somaidadeFeminino:int=0
mediaidadeFeminino:float=0

contagemalturaFeminino:int=0
somaalturaFeminino:float=0


mediapesoFeminino:float=0
contagempesoFeminino:int=0
contagempessoasacima90Feminino:int=0
somapesoFeminino:float=0

pessoasMaiorIdade:int=0
pessoasMenorIdade:int=0
mediatotalIdade:float=0
mediatotalAltura:float=0
mediageralPeso:float=0

i=0
genero=input("Digite M-Masculino/F-Feminino")
while i < 2:
    if genero=='m':
        print("Masculino:")
        idadeMasculino=eval(input("Por favor digite a sua idade"))
        if idadeMasculino>=18:
            contagenmaioridadeMasculino=contagenmaioridadeMasculino+1
        else:
            contagenmenoridadeMasculino = contagenmenoridadeMasculino+1

        idadetotalMasclino=contagenmaioridadeMasculino+contagenmenoridadeMasculino
        contagemgeralidadeMasculino=somaidadeMasculino+idadeMasculino

        alturaMasculino=eval(input("Por favor digite sua altura"))
        somaalturaMasculino=somaalturaMasculino+alturaMasculino
        contagemalturaMasculino=contagemalturaMasculino+1


        pesoMasculino=eval(input("Por favor digite seu peso"))
        contagempesoMasculino=contagempesoMasculino+1
        if pesoMasculino>90:
            contagempessoasacima90Masculino=pesoMasculino+1
        somapesoMasculina=somapesoMasculino+pesoMasculino

    elif genero=='f':

        print("Feminino:")
        idadeFeminino=eval(input("Por favor digite a sua idade"))
        if idadeFeminino>=18:
            contagenmaioridadeFeminino=contagenmaioridadeFeminino+1
        else:
            contagenmenoridadeFeminino = contagenmenoridadeFeminino+1

        idadetotalFeminino=contagenmaioridadeFeminino+contagenmenoridadeFeminino
        contagemgeralidadeFeminino=somaidadeFeminino+idadeFeminino

        alturaFeminino=eval(input("Por favor digite sua altura"))
        somaalturaFeminino=somaalturaFeminino+alturaFeminino
        contagemalturaFeminino=contagemalturaFeminino+1


        pesoFeminino=eval(input("Por favor digite seu peso"))
        contagempesoFeminino=contagempesoFeminino+1
        if pesoFeminino>90:
            contagempessoasacima90Feminino=pesoFeminino+1
        somapesoFeminino=somapesoFeminino+pesoFeminino

    else:
        break
    genero = input("Digite M-Masculino/F-Feminino")
    i=i+1

mediaidadeMasculino=idadetotalMasclino/idadetotalMasclino
mediaalturaMasculina=somaalturaMasculino/contagemgeralidadeMasculino
mediapesoMasculino=somapesoMasculino/contagempesoMasculino

mediaidadeFeminino=idadetotalFeminino/idadetotalFeminino
mediaalturaFeminino=somaalturaFeminino/contagemgeralidadeFeminino
mediapesoFeminino=somapesoFeminino/contagempesoFeminino

pessoasMaiorIdade=contagenmaioridadeMasculino+contagenmaioridadeFeminino
pessoasMenorIdade=contagenmenoridadeMasculino+contagenmenoridadeFeminino
mediatotalIdade=(mediaalturaMasculina+mediaalturaFeminino)/2
mediatotalAltura=(mediaalturaMasculina+mediaalturaFeminino)/2
mediageralPeso=(mediapesoMasculino+mediapesoFeminino)/2
pessoasacima90=contagempessoasacima90Masculino+contagempessoasacima90Feminino


print("======Ficha Masculina======")
print("Numero de pessoas masculinas:",contagemgeralidadeMasculino)
print("Numero de homens maiores de idade:",contagenmaioridadeMasculino)
print("Numero de homens menores de idade:",contagenmenoridadeMasculino)
print("Media de idade masculina:",mediaidadeMasculino)
print("Media de altura masculina",mediaalturaMasculina)
print("Media de peso masculino:",mediapesoMasculino)
print("Numero de homens a ter mais de 90Kg:",contagempessoasacima90Masculino)
print("======Ficha Feminina======")
print("Numero de pessoas femininas:",contagemgeralidadeFeminino)
print("Numero de homens maiores de idade:",contagenmaioridadeFeminino)
print("Numero de homens menores de idade:",contagenmenoridadeFeminino)
print("Media de idade femininas:",mediaidadeFeminino)
print("Media de altura feminina:",mediaalturaFeminino)
print("Media de peso femininas:",mediapesoFeminino)
print("Numero de homens a ter mais de 90Kg:",contagempessoasacima90Feminino)
print("======Ficha Unisex======")
print("Numero total de pessoas maiores de idade:",pessoasMaiorIdade)
print("Numero total de pessoas menores de idade",pessoasMenorIdade)
print("A media geral de idade e:",mediatotalIdade)
print("Media geral de altura:",mediatotalAltura)
print("Media geral de peso",mediageralPeso)
print("Quantidade de pessoas acima do peso:",pessoasacima90)
print("Media total de peso",mediageralPeso)