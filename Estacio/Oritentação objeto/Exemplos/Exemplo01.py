class Pessoa():
    def __init__(self,nome,ender):
        self.nome = nome
        self.set_ender(ender)
        
    def set_nome(self,nome):
        self.set_nome=nome
    def set_ender(self,ender):
        self.ender=ender
    def get_nome(self):
        return self.nome
    def get_ender(self):
        return self.ender

pessoa1 = Pessoa("maria","rua 01234")
pessoa2 = Pessoa("joao","rua 56789")

print((f"Nome: {pessoa1.get_nome()},Endereço:{pessoa1.get_ender()}"))
print((f"Nome: {pessoa2.get_nome()},Endereço:{pessoa2.get_ender()}"))