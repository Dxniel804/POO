from models.tipo_veiculo import Caminhao, Carro
from models.motorista import Motorista
from models.veiculo import Veiculo

motorista01 = Motorista("Daniel")
motorista02 = Motorista("Marcelo")

caminhao01 = Caminhao(500, 'Mercedes Benz', 100, 20)
carro01 = Carro(1000, 'Audi', 1000, 30)

# AGREGAÇÃO
carro01.atribuir_motorista(motorista01)
caminhao01.atribuir_motorista(motorista02)

# POLIMORFISMO
print(f'Veiculo: {carro01.ver_modelo}, {carro01.calcular_combustivel()}')
print(caminhao01.calcular_combustivel())

# MÉTODO STATIC
print(f"Total de veículos na frota: {Veiculo.total_veiculos()}")

# ENCAPSULAMENTO
print(carro01.ver_modelo())
