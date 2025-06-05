
class DummyObserver:
    def __init__(self):
        self.notified = False

    def update(self, sensor_name, data):
        self.notified = True

from notifier.subject import SensorPublisher

def test_observer_is_notified():
    pub = SensorPublisher()
    obs = DummyObserver()
    pub.register(obs)
    pub.notify_observers("TestSensor", 42)
    assert obs.notified
