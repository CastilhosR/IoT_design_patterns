from notifier.observer_interface import Observer

class DashboardObserver(Observer):
    def update(self, sensor_name, data):
        print(f"[Dashboard] {sensor_name} => valor atualizado: {data}")
