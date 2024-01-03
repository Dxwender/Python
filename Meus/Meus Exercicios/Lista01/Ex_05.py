#Variaveis
valorHoras:float
quantidadeHoras: float
salarioBruto:float
rouboSindicato:float
vcnaoteraInss:float
rouboRenda:float=0
roubodeGarantia:float

#Entrada
valorHoras=eval(input("Por favor digite o valor da hora:"))
quantidadeHoras=eval(input("Por favor a quantidade de horas:"))

#Regras/Operacoes
#Salario Bruto
salarioBruto=valorHoras*quantidadeHoras

#Sindicato vagabundo
rouboSindicato=((salarioBruto*0.03)-salarioBruto)+salarioBruto

#Roubo de renda
if salarioBruto <900:
    print("Isento")
elif salarioBruto>=900 and salarioBruto<1500:
    rouboRenda=((salarioBruto*0.05)-salarioBruto)+salarioBruto
elif salarioBruto>=1500 and salarioBruto<2500:
    rouboRenda=((salarioBruto*0.1)-salarioBruto)+salarioBruto
else:
    rouboRenda=((salarioBruto*0.2)-salarioBruto)+salarioBruto
#INSS
vcnaoteraInss = ((salarioBruto*0.1)-salarioBruto)+salarioBruto
#FGTS esmola
roubodeGarantia=((salarioBruto*0.11)-salarioBruto)+salarioBruto

#Resultados
print("======Recibo do assualto=======")
print("Salario bruto","(",valorHoras,"*",quantidadeHoras,")","          :R$",salarioBruto)
print("(-) Roubo de renda(5%)              :R$",rouboRenda)
print("(-) Voce não vai tera INSS(10%)     :R$",vcnaoteraInss)
print("(-) Vagabundos do Sindicato(3%)     :R$",rouboSindicato)
print("Roubo de garantia(11%)              :R$",roubodeGarantia)
print("Total do roubo                      :R$",rouboRenda+valorHoras+roubodeGarantia)
print("Resto chamado salario liquido       :R$",salarioBruto-(rouboRenda+valorHoras+roubodeGarantia))