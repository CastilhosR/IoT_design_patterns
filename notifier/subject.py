
class SensorPublisher:
    """
    Sujeito do padrao Observer. Gerencia e notifica observers.
    """
    def __init__(self):
        self.observers = []

    def register(self, observer):
        print(f"[LOG] Registrando observer: {observer.__class__.__name__}")
        self.observers.append(observer)

    def notify_observers(self, sensor_name, data):
        print(f"[LOG] Notificando observers para {sensor_name}")
        for observer in self.observers:
            observer.update(sensor_name, data)
