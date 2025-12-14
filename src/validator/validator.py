from abc import ABC, abstractmethod
from src.settings.re_user_patterns import user_patterns as up
import re
class IValidator(ABC):
    @abstractmethod
    def validate(self,val_object:str)->bool:
        pass

class ValidatorBrand(IValidator):
    def validate(self,val_object:str)->bool:
        pass

class ValidatorNumber(IValidator):
    def validate(self, val_object:str)->bool:
        return bool(re.match(up['car_number'], val_object))

class ValidatorModel(IValidator):
    def validate(self):
        pass

class ValidatorMileage(IValidator):
    def validate(self):
        pass

class ValidatorDateOfProducing(IValidator):
    def validate(self):
        pass