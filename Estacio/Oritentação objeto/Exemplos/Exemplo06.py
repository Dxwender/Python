class Argentina():
    def capital (self):
        print("Buenos Aires é a capital da Argentina.")
    def lingua_oficial(self):
        print("O espanhou e a lingua ofical da Argentina")
class Bananil():
    def capital(self):
        print("Brasilia e capital do Bostil")
    def lingua_oficial(self):
        print("O macaques e a lingua oficial Baninil")

obj_arg=Argentina()
obj_bra=Bananil()
for pais in (obj_arg,obj_bra):
    pais.capital()
    pais.lingua_oficial()