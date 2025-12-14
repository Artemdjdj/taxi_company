from abc import ABC, abstractmethod


class IQueryManager(ABC):
    @abstractmethod
    def execute(self, **kwargs):
        pass

class CreateCar(IQueryManager):
    def execute(self, **kwargs):
        pass

class GetCars(IQueryManager):
    def execute(self, **kwargs):
        pass
