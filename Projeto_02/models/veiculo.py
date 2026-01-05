from abc import ABC, abstractmethod
from .motor import Motor
from .motorista import Motorista

class Veiculo:
    total_veiculo = 0

    def __init__(self, modelo, cilindradas):
        # O Motor é criado dentro do __init__ do Carro (Composição)
        self.motor = Motor(cilindradas)
        self.modelo = modelo
        Veiculo.total_veiculo += 1

    def __str__(self):
        return f"Veículo: {self.modelo}, Motor: {self.motor.cilindradas}cc"
    
    # Associação
    # Python sabe que motorista_obj DEVE ser da classe Motorista
    def atribuir_motorista(self, motorista_obj: Motorista) -> None:
        if isinstance(motorista_obj, Motorista):
            self.nome_motorista = motorista_obj
            print(f"{motorista_obj.nome_motorista} agora está dirigindo o {self.modelo}.")
        else:
            print("Objeto inválido. Esperava-se uma instância de Motorista.")

    # GETTER
    @property
    def modelo(self):
        return self.__modelo

    # SETTER
    @modelo.setter
    def modelo(self, nome_modelo):
        if len(nome_modelo) <= 3:
            raise ValueError("O nome do modelo deve ter mais de 3 caracteres.")
        self.__modelo = nome_modelo
       
    
    @staticmethod
    def total_veiculos():
        return f"{Veiculo.total_veiculo}"

    @abstractmethod
    def calcular_combustivel(self):
        consumo = self.km_rodado / self.litros
        return f"Consumo de combustivel: {consumo}"

