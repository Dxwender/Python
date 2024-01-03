class Veiculo:
    def __int__(self,nome,velocidade_max,quilometro_litro):
        self.nome = nome
        self.velocidade_max= velocidade_max
        self.quilometro_litro = quilometro_litro
    def capacidadae_assentos(self,capacidade):
        print(f"A capacidade maxima de assentos do veiculo {self.nome} é {capacidade}")
    def toStr(self):
        print(f"nome = {self.nome}")
        print(f"velocidade_max={self.velocidade_max}")
        print(f"Quilometro percorridos por litro= {self.quilometro_litro}")
class Onibus(Veiculo):
    def capacidadae_assentos(self,capacidade=70):
        return super().capacidadae_assentos(capacidade=70)

onibus_escolar = Onibus("Scania",120,80)
onibus_escolar.toStr()
onibus_escolar.capacidadae_assentos()