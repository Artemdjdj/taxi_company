from src.validator.validator import ValidatorNumber

def test_validator():
    validator_number = ValidatorNumber()
    assert validator_number.validate("1234AB-7") == True