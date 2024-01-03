# Classe Salario
class Salario:
    def __init__(self,base,bonus):
        self.base = base
        self.bonus = bonus
    def salario_anual (self):
        return (self.base*12)+self.bonus

# Classe Empregado
class Empregado:
    def __int__(self,nome,idade,salario):
        self.nome = nome
        self.idade = idade
        self.salario_empregado = salario #Agregaçao
    def salario_total(self):
        return self.salario_agregado.salario_anual()



salario = Salario(100000,700)
emp = Empregado('Musachi' , 36 , salario)
print(emp.salario_total())