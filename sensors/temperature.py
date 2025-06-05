
import random
from .base import Sensor

class TemperatureSensor(Sensor):
    """
    Sensor concreto para leitura de temperatura.
    """
    def read_data(self):
        return round(random.uniform(5.0, 60.0), 2)