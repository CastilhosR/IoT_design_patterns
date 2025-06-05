
from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    Classe base abstrata para sensores.
    Aplica o padrao Bridge ao separar a logica comum de coleta da implementacao concreta.
    """
    def __init__(self, name, publisher):
        self.name = name
        self.publisher = publisher

    @abstractmethod
    def read_data(self):
        pass

    def collect(self):
        data = self.read_data()
        print(f"[LOG] {self.name} leu valor: {data}")
        self.publisher.notify_observers(self.name, data)
