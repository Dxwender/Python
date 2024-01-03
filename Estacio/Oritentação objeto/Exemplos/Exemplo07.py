class Veiculo:
    def rodar (self):
        print("Reduz o consumo de combustivel")
class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veiculo utiliza eletecidade")

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()