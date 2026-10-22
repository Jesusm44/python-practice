class User:
    def __init__(self,name, email):
        if not isinstance(name, str):
            raise ValueError("ERROR: Name not valid")
        
        if not name.strip():
            raise ValueError("ERROR: Name not valid")
        
        name = name.strip()

        if len(name) < 3:
            raise ValueError("ERROR: Name not valid")

        if not isinstance(email, str):
            raise ValueError("ERROR: The email can only be str")

        if not email.strip():
            raise ValueError("ERROR: The email cannot be empty")
        
        if "@" not in email:
            raise ValueError("ERROR: The email address does not have @")
        
        self.name = name
        self.email = email

    @classmethod
    def from_email(cls,text):
        parts = text.split("@")

        name = str(parts[0])
        email = text

        return cls(name,email)


user_one = User("Maria", "mariperez@gmail.com")
user_from_email = user_one.from_email("mariperez@gmail.com")

user_one = User(1234, "markperezgmail.com")
user_from_email = user_one.from_email("mariperez@gmail.com")

user_one = User("Maria", "")
user_from_email = user_one.from_email("")

print(user_from_email.name)
print(user_from_email.email)