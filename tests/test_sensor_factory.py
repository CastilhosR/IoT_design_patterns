
import pytest
from notifier.subject import SensorPublisher
from sensors.sensor_factory import SensorFactory
from sensors.temperature import TemperatureSensor
from sensors.humidity import HumiditySensor

def test_temperature_sensor_creation():
    pub = SensorPublisher()
    sensor = SensorFactory.create_sensor("temperature", pub)
    assert isinstance(sensor, TemperatureSensor)

def test_humidity_sensor_creation():
    pub = SensorPublisher()
    sensor = SensorFactory.create_sensor("humidity", pub)
    assert isinstance(sensor, HumiditySensor)

def test_invalid_sensor_type():
    pub = SensorPublisher()
    with pytest.raises(ValueError):
        SensorFactory.create_sensor("invalid", pub)
