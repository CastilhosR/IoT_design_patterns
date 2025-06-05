from notifier.subject import SensorPublisher
from notifier.storage_observer import StorageObserver
from notifier.dashboard_observer import DashboardObserver
from notifier.alert_observer import AlertObserver
from sensors.sensor_factory import SensorFactory
import time

def main():
    print("[LOG] Inicializando sistema de monitoramento de sensores...\n")
    publisher = SensorPublisher()
    publisher.register(StorageObserver())
    publisher.register(DashboardObserver())
    publisher.register(AlertObserver())

    temp_sensor = SensorFactory.create_sensor("temperature", publisher)
    hum_sensor = SensorFactory.create_sensor("humidity", publisher)

    for rodada in range(15):
        print(f"\n\n--- Coletando dados --- rodada {rodada +1}")
        temp_sensor.collect()
        hum_sensor.collect()
        time.sleep(3)

if __name__ == "__main__":
    main()