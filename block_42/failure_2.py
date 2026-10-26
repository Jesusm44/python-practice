# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_domain(self):
#         return self.email.split("@", 1)[1]

#     @staticmethod 
#     def change_name(user, new_name):
#         user.name = new_name

#     def from_email(self, email):
#         if "@" not in email:
#             raise ValueError("Invalid email")
#         name = email.split("@", 1)[0]
#         return User(name, email)

#     @staticmethod
#     def is_valid_email(email):
#         return (
#             isinstance(email, str) and email.count("@") == 1
#             and not email.startswith("@") and not email.endswith("@")
#         )

#Refactorization
class User:
    def __init__(self,name,email) -> None:
        if not isinstance(name,str):
            raise ValueError
        
        if not name.strip():
            raise ValueError("ERROR: The name cannot be empty")

        if len(name.strip()) < 3:
            raise ValueError("ERROR: The name cannot be empty")

        if not (
            isinstance(email, str)
            and email.count("@") == 1
            and not email.startswith("@")
            and not email.endswith("@")
        ):
            raise ValueError("Your email is not valid")

        self.name = name
        self.email = email
    
    def change_name(self, new_name):
        self.name = new_name

    @staticmethod
    def get_domain(email):
        return email.split("@", 1)[1]

    @staticmethod
    def is_valid_email(email):
        return (
            isinstance(email, str) and email.count("@") == 1
            and not email.startswith("@") and not email.endswith("@")
        )
    
    @classmethod
    def from_email(cls,email):
        if not cls.is_valid_email:
            raise ValueError("Your email is not valid")
        
        name = email.split("@", 1)[0]
        return cls(name,email)







