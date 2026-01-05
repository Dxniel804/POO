from .veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__ (self, motor, modelo, km_rodado, litros):
        # Chama o __init__ da classe Pai (Veiculo)
        super().__init__(modelo, motor)
        self.km_rodado = km_rodado
        self.litros = litros
    
class Carro(Veiculo):
    def __init__ (self, motor, modelo, km_rodado, litros):
        super().__init__(modelo, motor)
        self.km_rodado = km_rodado
        self.litros = litros

        