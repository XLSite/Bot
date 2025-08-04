class Validator:
    def validate(self, data):
        if len(data):
            return True
        else:
            return False
        
class EmailValidator(Validator):
    def validate(self, data):
        if super().validate():
            return '@' in data

class PhoneValidator(Validator):
    def validate(self, data):
        if super().validate():
            return data.is_digit() and len(data) == 11