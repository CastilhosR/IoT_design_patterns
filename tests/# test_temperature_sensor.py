# tests/test_temperature_sensor.py
from sensors.temperature import TemperatureSensor
from notifier.subject import SensorPublisher

def test_temperature_sensor_read_data():
    publisher = SensorPublisher()
    sensor = TemperatureSensor("Temp", publisher)
    value = sensor.read_data()
    assert isinstance(value, float)
