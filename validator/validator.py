from abc import ABC, abstractmethod

class IValidator(ABC):
    @abstractmethod
    def validate(self):
        pass

class ValidatorBrand(IValidator):
    def validate(self):
        pass

class ValidatorNumber(IValidator):
    def validate(self):
        pass

class ValidatorModel(IValidator):
    def validate(self):
        pass

class ValidatorMileage(IValidator):
    def validate(self):
        pass

class ValidatorDateOfProducing(IValidator):
    def validate(self):
        pass