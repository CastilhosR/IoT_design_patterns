
from .temperature import TemperatureSensor
from .humidity import HumiditySensor

class SensorFactory:
    """
    Factory Method para instanciar sensores com base no tipo.
    """
    @staticmethod
    def create_sensor(sensor_type, publisher):
        print(f"[LOG] Criando sensor do tipo: {sensor_type}")
        if sensor_type == "temperature":
            return TemperatureSensor("TemperatureSensor", publisher)
        elif sensor_type == "humidity":
            return HumiditySensor("HumiditySensor", publisher)
        else:
            raise ValueError("Sensor invalido")
