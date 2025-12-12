# CARRO - POLIFORMISMO 
esse repositório tem o conceito de Herança na Programação Orientada a Objetos (POO) em Python, criando diferentes tipos de carros a partir de uma classe base (`Carro`)

# UML 
<img width="1183" height="580" alt="Captura de tela 2025-12-12 094253" src="https://github.com/user-attachments/assets/c1b5ebe5-e87c-46b4-8929-7cfb4f1de812" />

# funcionalidade de cada classe
A classe `Carro` gerencia a velocidade e as ações básicas de um veículo.

* `__init__(self, velocidade_inicial)`: Inicializa o carro com a velocidade de partida.
* `acelera(self)`: Aumenta a velocidade em **1 Km/h**.
* `freia(self)`: Diminui a velocidade em **1 Km/h**.
* `exibe_velocidade(self)`: Imprime a velocidade atual.

Classes Derivadas (Herança)

As classes derivadas herdam todas as funcionalidades de `Carro` e adicionam ou modificam comportamentos específicos:

| Classe | Herança / Polimorfismo | Comportamento Único |
| :--- | :--- | :--- |
| `CarroInteligente` | Herda e adiciona `estaciona()` | Imprime "Estacionando automaticamente...". |
| `CarroEsportivo` | Herda e adiciona `Turbo()` | Aumenta a velocidade em **10 Km/h**. |
| `CarroCorrida` | **Sobrescreve `acelera()`** | Acelera em **5 Km/h** (em vez de 1 Km/h). |

# Como Executar

O arquivo principal para demonstração é o `main.py`.

1.  Certifique-se de que todos os arquivos Python (`carros.py`, `carro_inteligente.py`, `carro_esportivo.py`, `carro_corrida.py` e `main.py`) estão no mesmo diretório.
2.  Execute o arquivo principal a partir do terminal:

    ```bash
    python main.py
    ```
 Saída Esperada

O script `main.py` realiza um *test drive* com cada tipo de carro, demonstrando a herança (`acelera`) e os métodos especializados (como `estaciona` e `turbo`).
