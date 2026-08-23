from os import error
from typing import Any, Literal

# users:list[dict[str|int, Any]] = []

# def register_user(users, 
#     id:int, 
#     name:str, 
#     age:int,
#     roles= None, 
#     activate:bool = True
# )-> Any:
    
#     if roles is None:
#         roles= []

#     if not isinstance(id, int):
#         return False

#     if not isinstance(name, str):
#         return False
    
#     if not isinstance(age, int):
#         return False
    
#     if not isinstance(activate, bool):
#         return False

#     if id not in range(0, 101):
#         return False

#     if name.strip() == "":
#         return False

#     if age not in range(1,101):
#         return False

#     new_user:dict[str|int, Any] = {
#         "id" : id,
#         "name": name,
#         "age" : age,
#         "roles": roles,
#         "activate": activate
#     }
#     users.append(new_user)

#     return users

# user_one:Any = register_user(users, 10, "Juan", 25)

# user_two: Any = register_user(
#     users= users,
#     id = 52,
#     name = "Valeria",
#     age = 63,
#     roles=["caminar", "Trotar", "nadar"],
#     activate= True
# )

# print(user_two)


# users:list[dict[str|int,Any]] = []

# def add_users(
#     users,
#     id: int, 
#     name: str,
#     age:int,
#     *roles, 
#     **ubicacion
# ) :
#     """function that helps us know how to add a user"""
#     if not isinstance(id,int):
#         return False

#     if not isinstance(name,str):
#         return False

#     if not isinstance(age, int):
#         return False

#     if id not in range(1,21):
#         return False

#     if name.strip() == "":
#         return False

#     if age not in range(1,101):
#         return False

#     new_user :dict[str|int,Any]= {
#         "id" : id,
#         "name": name,
#         "age": age,
#         "roles": roles,
#         "ubicacion": ubicacion
#     }
#     users.append(new_user)

#     return users

# user_one:Any | Literal[False] = add_users (
#     users,
#     19,
#     "Juan Josse",
#     21,
#     "Administrador",
#     "Gerente",
#     pais= "Ecuador",
#     ciudad = "Quito",
#     ip= "192.168.1.1"
# )

# print(user_one)

# datos_usuario:list[Any] = ["Carlos", 24, "Quito"]

# def procces_data(name:str, age:int, city: str)-> str | Literal[False]:
#     if not isinstance(name, str):
#         return False

#     if not isinstance(age,int):
#         return False

#     if not isinstance(city, str):
#         return False


#     if name.strip() == "":
#         return False

#     if age not in range(0,101):
#         return False

#     if city.strip() == "":
#         return False

#     return f"""
# Name: {name}
# Age:  {age}
# City: {city}
# """

# print(procces_data(*datos_usuario))

# datos_usuario_one:dict[str,Any] = {
#     "name": "Carlos",
#     "age": 24,
#     "city": "Quito"
# }

# print(procces_data(**datos_usuario_one))

# products:list[dict[str,Any]] = [
#     {"id": 1, "name": "Laptop", "price": 900, "stock": 5},
#     {"id": 2, "name": "Mouse", "price": 25, "stock": 20},
#     {"id": 3, "name": "Monitor", "price": 300, "stock": 7},
#     {"id": 4, "name": "Teclado", "price": 60, "stock": 10}
# ]

# sorted_price:Any = sorted(
#     products,
#     key= lambda prodcut: prodcut["price"]
# )

# sorted_stock:Any = sorted(
#     products,
#     key=lambda product: product["stock"]
# )

# sorted_len_name:Any = sorted(
#     products,
#     key= lambda product: len(product["name"])
# )

# users:list[dict[str,Any]] = [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 24,
#         "activate": True
#     },
#     {
#         "id": 2,
#         "name": "Luis",
#         "age": 17,
#         "activate": False
#     }
# ]

# """Function that helps us process a user"""
# def process_user(id:int, name:str, age:int, activate:bool) -> dict[str, Any] | Literal[False]:

#     if not isinstance(id, int):
#         return False

#     if not isinstance(name,str):
#         return False

#     if not isinstance(age,int):
#         return False

#     if not isinstance(activate,bool):
#         return False

#     if id not in range(1,101):
#         return False

#     if name.strip() == "":
#         return False

#     if age not in range(1,101):
#         return False

#     new_user:dict [str,Any]= {
#         "id": id,
#         "name": name,
#         "age": age,
#         "activate": activate
#     }
#     return new_user


# """After processing users, we save it"""
# def save_user(users, new_user) -> Any:
#     user:dict[str,Any] | Literal[False] = process_user(**new_user)

#     if user:
#         users.append(user)
#     return users


# def show_user(users):
#     position = int(input("Enter the position: "))

#     if position < 0 or position >= len(users):
#         return ("ERROR: Position does not exist")

#     return users[position]


# def send_user(users):
#     position = int(input("Enter the position: "))

#     if position < 0 or position >= len(users):
#         return ("ERROR: Position does not exist")

#     return f'sending user... {users[position]["name"]}'


# user_one:dict[str,Any] ={
#         "id": 5,
#         "name": "Jose",
#         "age": 17,
#         "activate": True
# }

# nuevo_useres:Any = save_user(
#     users=users,
#     new_user= user_one
# )

# print(save_user(users,user_one))

# users = [
#     {"id": 1, "name": "Ana", "age": 24},
#     {"id": 2, "name": "Luis", "age": 17},
#     {"id": 3, "name": "Carlos", "age": 31}
# ]

# def register_user(user):

#     if "name" not in user:
#         return False

#     if "age" not in user:
#         return False

#     if not isinstance(user["name"], str):
#         return False

#     if not isinstance(user["age"], int):
#         return False

#     if user["name"] == "":
#         return False

#     if user["age"] < 0:
#         return False

#     return user

# def update_user(users, position,**update):

#     if position < 0 or position >= len(users):
#         return "ERROR: Position not found"

#     validated_update = register_user(update)

#     if not validated_update:
#         return "ERROR: Update no valid"

#     user = users[position]

#     for key, value in validated_update.items():
#         user[key] = value

#     return user


# update_user(
#     users=users,
#     position = 0,
#     name="Juan",
#     age=25
# )

# print(users)














