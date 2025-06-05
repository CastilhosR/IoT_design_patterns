from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, sensor_name: str, value: float):
        pass