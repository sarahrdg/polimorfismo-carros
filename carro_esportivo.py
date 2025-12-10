from carros import Carro

class CarroEsportivo(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def Turbo(self):
        self.velocidade +=10
        print("turbo ativado! a velocidade aumentou em 10Km/h")
    
    
