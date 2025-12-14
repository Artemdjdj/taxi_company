from abc import ABC, abstractmethod

class IDbConnector(ABC):
    @abstractmethod
    def connect(self):
        pass