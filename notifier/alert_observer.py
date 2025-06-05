
from notifier.observer_interface import Observer

class AlertObserver(Observer):
    def update(self, sensor_name, data):
        if sensor_name == "TemperatureSensor" and data > 30:
            print(f"[ALERTA] {sensor_name} muito quente! Valor: {data}")
