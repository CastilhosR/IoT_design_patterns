
class StorageObserver:
    def update(self, sensor_name, data):
        print(f"[Storage] {sensor_name} => armazenado valor: {data}")
