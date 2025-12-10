from carros import Carro
from carro_esportivo import CarroEsportivo
from carro_inteligente import CarroInteligente
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\nTestanto {carro.__class__.__name__}:")
    carro.exibe_velocidade()
    carro.acelera()

if __name__ == "__mainn__":
    carro_inteligente = CarroInteligente(10)
    print("carro inteligente")
    carro_inteligente.estaciona()
    test_drive(carro_inteligente)
    print()

    carro_esportivo = CarroEsportivo(50)
    print("carro esportivo")
    carro_esportivo.turbo()
    test_drive(carro_esportivo)
    print()

    carro_corrida = CarroCorrida(100)
    print("carro corrida")
    test_drive(carro_corrida) 
    print()
