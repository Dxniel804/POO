from abc import ABC, abstractmethod
from .motor import Motor
from .motorista import Motorista

class Veiculo:
    total_veiculo = 0

    def __init__(self, modelo, cilindradas):
        # O Motor é criado dentro do __init__ do Carro (Composição)
        self.motor = Motor(cilindradas)
        self.__modelo = modelo
        Veiculo.total_veiculo += 1

    def ver_modelo(self):
        return self.__modelo
    
    # Associação
    def atribuir_motorista(self, motorista_obj):
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
        if len(nome_modelo) > 3:
            self.__modelo = nome_modelo
        else:
            print("Nome do modulo tem que ter mais de 3 letras!")
    
    @staticmethod
    def total_veiculos():
        return f"{Veiculo.total_veiculo}"


    @abstractmethod
    def calcular_combustivel(self):
        pass

