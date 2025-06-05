
# Projeto de Monitoramento de Sensores IoT

Este projeto foi desenvolvido com fins didáticos para demonstrar a aplicação de **padrões de projeto** (Design Patterns) em Python. Ele simula um sistema de coleta e notificação de dados de sensores (temperatura e umidade), aplicando três tipos principais de padrões:

---

##  Padrões de Projeto Aplicados

### 1. Factory Method (Padrão Criacional)
- **Onde:** `sensors/sensor_factory.py`
- **Descrição:** Cria instâncias de sensores (`TemperatureSensor`, `HumiditySensor`) com base em uma string de entrada.
- **Benefício:** Desacopla a lógica de criação da lógica de uso dos sensores.

```python
SensorFactory.create_sensor("temperature", publisher)
```

---

### 2. Bridge (Padrão Estrutural)
- **Onde:** `sensors/base.py` e `sensors/temperature.py` / `humidity.py`
- **Descrição:** O sensor base (`Sensor`) define a estrutura comum com um método `collect`, enquanto as subclasses implementam a lógica específica de `read_data`.
- **Benefício:** Separa abstração (Sensor e seu ciclo de coleta) da implementação concreta (tipo de dado lido), facilitando extensão.

---

### 3. Observer (Padrão Comportamental)
- **Onde:** `notifier/subject.py`, `notifier/storage_observer.py`, `dashboard_observer.py`, `alert_observer.py`
- **Descrição:** Quando um sensor coleta um dado, o `SensorPublisher` notifica todos os observers registrados, que então reagem à nova leitura.
- **Benefício:** Permite múltiplas reações (armazenamento, visualização, alertas) sem acoplamento à lógica de coleta.

---

##  Estrutura de Diretórios

```
.
├── sensors/                # Sensores e a fábrica de sensores
│   ├── base.py             # Classe abstrata de Sensor (Bridge)
│   ├── temperature.py      # Sensor de temperatura
│   ├── humidity.py         # Sensor de umidade
│   └── sensor_factory.py   # Criação de sensores (Factory)
│
├── notifier/               # Observadores e Publisher (Observer)
│   ├── subject.py          # Sujeito: gerencia observers
│   ├── storage_observer.py
│   ├── dashboard_observer.py
│   └── alert_observer.py
│
├── tests/                  # Testes com pytest
│   ├── test_sensor_factory.py
│   └── test_observer_notification.py
│
├── scripts/                # Scripts de instalação, execução e teste
│   ├── install.sh
│   ├── run.sh
│   └── test.sh
│
├── main.py                 # Execução principal
└── README.md               # Este arquivo
```

---

## ▶ Como Executar

### 1. Instalar dependências
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

### 2. Rodar a simulação
```bash
chmod +x scripts/run.sh
./scripts/run.sh
```

### 3. Rodar testes automatizados
```bash
chmod +x scripts/test.sh
./scripts/test.sh
```

---

##  Exemplos de Saída (prints)

```
[LOG] Inicializando sistema de monitoramento de sensores...
[LOG] Criando sensor do tipo: temperature
[LOG] Criando sensor do tipo: humidity
[LOG] Registrando observer: StorageObserver
[LOG] Registrando observer: DashboardObserver
[LOG] Registrando observer: AlertObserver

[LOG] TemperatureSensor leu valor: 33.1
[LOG] Notificando observers para TemperatureSensor
[Storage] TemperatureSensor => armazenado valor: 33.1
[Dashboard] TemperatureSensor => valor atualizado: 33.1
[ALERTA] TemperatureSensor muito quente! Valor: 33.1
```

---

##  Possíveis Extensões

- Armazenar dados em banco SQLite
- Adicionar novos sensores (luminosidade, pressão)
- Adicionar interface gráfica com Streamlit ou Tkinter
- Persistir dados com JSON ou arquivos .csv

---

##  Requisitos

- Python 3.8+
- pytest (para testes)

---

##  Observações pessoais:

Tem sido bem dificil compreender a relevancia desse ou daquele padrão de projeto, principalmente em ambiente de desenvolvimento Python cujo codigo, por definição, é enxuto. 


Nesse contexto, incluir linhas a mais de codigo vai contra o "Zen do Python".


Portanto, no meu interessante ponto de vista ... trata-se um código 'não pythônico' e um tanto macarrônico. ;-)

