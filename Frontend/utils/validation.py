import re

class Validation():
    def __init__(slef) -> None:
        pass

    def validate_email(self, email):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)
    
    def validate_password(slef, password):
        if len(password) < 8:
            return False
        
        if not any(char.isdigit() for char in password):
            return False
        
        if not re.search("[@_!#$%^&*()<>/\|}{~:]", password):
            return False
        return True
    