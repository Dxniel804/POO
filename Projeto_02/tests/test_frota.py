import pytest
from models.tipo_veiculo import Carro, Caminhao
from models.motorista import Motorista
from models.veiculo import Veiculo

# FIXTURES: Servem para "preparar o terreno". Você cria o objeto uma vez e usa em vários testes.

@pytest.fixture
def meu_carro():
    return Carro(1000, "Audi", 100, 10)

@pytest.fixture
def meu_motorista():
    return Motorista("Daniel")

# -- TESTES UNITÁRIOS --
def test_agregacao_motorista(meu_carro, meu_motorista):
    """Garante que o motorista é vinculado corretamente ao carro"""
    # Agir
    meu_carro.atribuir_motorista(meu_motorista)
    
    # Afirmar (Associação/Agregação)
    # Verificamos se o objeto dentro do carro é o mesmo objeto Daniel
    assert meu_carro.nome_motorista == meu_motorista
    assert meu_carro.nome_motorista.nome_motorista == "Daniel"

def test_composicao_motor(meu_carro):
    """Garante que o motor foi criado internamente (Composição)"""
    assert meu_carro.motor.cilindradas == 1000