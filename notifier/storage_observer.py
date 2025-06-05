import csv
import os
from datetime import datetime
from notifier.observer_interface import Observer

class StorageObserver(Observer):
    def __init__(self, filename="sensor_data.csv"):
        self.filename = filename
        # Verifica se o arquivo já existe; se não, escreve o cabeçalho
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "sensor_name", "value"])

    def update(self, sensor_name, value):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[Storage] {sensor_name} => armazenado valor: {value}")
        # Escreve no arquivo CSV
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, sensor_name, value])
