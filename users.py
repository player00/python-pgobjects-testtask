class User:

    
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

VALID_USER_1 = User("seleniumisgood@mail.com", "123456")
