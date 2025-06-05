
import random
from .base import Sensor

class HumiditySensor(Sensor):
    """
    Sensor concreto para leitura de umidade.
    """
    def read_data(self):
        return round(random.uniform(10.0, 99.0), 2)
