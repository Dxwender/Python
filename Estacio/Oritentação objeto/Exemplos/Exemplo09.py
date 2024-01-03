class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro
    def toStr(self):
        print(f'nome= {self.nome}')
        print(f'velocidade_max {self.velocidade_max}')
        print(f'Quilometro percorridos por litro {self.quilometro_litro}')
modelo_carro = Veiculo("fusca",180, 10)
modelo_carro.toStr()
