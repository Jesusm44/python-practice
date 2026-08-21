from itertools import product
from typing import Any
# def create_products(name, price: int, categoria, stock = 0, status = False):
#     print(f'{name} - {price} - {categoria} - {stock} - {status}')

# create_products(
#     name = "Laptop",
#     price = 360,
#     categoria = "Electronica",
#     stock= 10,
#     status = True
# )

# create_products(
#     name = "Mouse",
#     price = 8,
#     categoria= "Electronica",
# )

# create_products(
#     name = "Cama",
#     price = 2000,
#     categoria= "Hogar",
#     status = False
# )

# def crear_cuenta(nombre, edad, tipo="normal", activa=True):
#     print(f'{nombre} - {edad} - {tipo} - {activa}')

# crear_cuenta(
#     nombre = "Jesus",
#     edad = 24,
#     tipo = "Estudiante",
# )

# crear_cuenta(
#     "Valeria",
#     25,
#     tipo = "Novia",
# )

# def add_product(name, product =[]):
#     product.append(name)
#     return product

# print(
#     add_product(
#         "Maria"
#     )
# )

# print(
#     add_product(
#         "Jose"
#     )
# )

# print(
#     add_product(
#         "Pedro"
#     )
# )

# def register_user(name, data ={}):
#     data["name"] = name
#     return data

# print(register_user("Juan"))
# print(register_user("Maria"))
# print(register_user("Josefina"))

# def register_id(id_user, ids = set()):
#     ids.add(id_user)
#     return ids

# print(register_id(17))
# print(register_id(16))
# print(register_id(18))

# def add_product(name, list_name = None):
#     if list_name is None:
#         list_name = []

#     list_name.append(name)
#     return list_name

# print(add_product("Maria"))
# print(add_product("Juan"))
# print(add_product("Margarita"))

# def register_user(name, data = None):
#     if data is None:
#         data = {}

#     data["name"] = name
#     return data

# print(register_user("Juan"))
# print(register_user("Maria"))
# print(register_user("Josefina"))

# def register_id(id_user, ids = None):
#     if ids is None:
#         ids = set()

#     ids.add(id_user)
#     return ids

# print(register_id(17))
# print(register_id(16))
# print(register_id(18))

# def agregar(valor, datos=[]):

#     datos.append(valor)
#     return datos

# a = agregar(10)
# b = agregar(20)
# c = agregar(30)

# # def procesar( 
#         nombre, edad, correo, telefono, ciudad, pais, activo = True, guardar = True
# ):
#     pass

# roles_user = []

# def create_user(
#     id_user, name, age, email, status = True, roles = None, 
# ):
#     if roles is None:
#         roles = []

#     user = {
#         "id" : id_user,
#         "name": name,
#         "age": age,
#         "email": email,
#         "active": status,
#         "roles": roles
#     }

#     return user

# user_1 = create_user(
#     id_user="u1",
#     name="Jose",
#     age=25,
#     email="jose@email.com"
# )

# user_2 = create_user(
#     id_user="u2",
#     name="Maria",
#     age=28,
#     email="maria@email.com"
# )

# roles = ["admin", "editor"]

# user_3 = create_user(
#     id_user="u3",
#     name="Carlos",
#     age=30,
#     email="carlos@email.com",
#     roles=roles
# )

# user_4 = create_user(
#     id_user="u4",
#     name="Ana",
#     age=22,
#     email="ana@email.com",
#     status=False
# )

# print(user_1)
# print(user_2)
# print(user_3)
# print(user_4)

# grades = [
#     18, 15, 12, 20, 14, 17, 9, 16, 13, 19,
#     11, 8, 15, 18, 20, 10, 14, 17, 12, 16,
#     19, 13, 15, 7, 18, 11, 20, 14, 16, 9,
#     12, 17, 19, 10, 15, 13, 18, 20, 11, 14,
#     16, 8, 17, 12, 19, 15, 13, 10, 18, 20,
#     9, 14, 16, 11, 17, 19, 12, 15, 8, 18,
#     20, 13, 10, 16, 14, 17, 11, 19, 15, 9,
#     12, 18, 20, 13, 16, 8, 14, 17, 11, 19,
#     15, 10, 18, 12, 20, 16, 13, 9, 17, 14,
#     19, 11, 15, 8, 18, 20, 12, 16, 14, 17,
#     10, 19, 13, 15, 18, 11, 20, 9, 16, 14,
#     17, 12, 8, 19, 15, 13, 18, 10, 20, 16,
#     11, 14, 17, 9, 19, 12, 15, 18, 13, 20,
#     16, 10, 14, 17, 8, 19, 11, 15, 20, 13,
#     18, 12, 16, 9, 14, 19, 17, 10, 15, 20,
#     13, 18, 11, 16, 14, 8, 19, 12, 17, 15,
#     20, 10, 13, 18, 16, 9, 14, 19, 11, 17,
#     15, 12, 20, 8, 16, 13, 18, 10, 19, 14,
#     17, 11, 15, 20, 9, 13, 18, 12, 16, 14,
#     19, 8, 17, 11, 20, 15, 10, 18, 13, 16
# ]

# def average_notes(*args):
#     total_len = 0
#     sum_notes = 0

#     for i in args:
#         total_len += 1
#         sum_notes += i

#     average = sum_notes / total_len
#     return average

# print(average_notes(*grades))


# def register_user(**kwargs):

#     for key,value in kwargs.items():
#         if type(value) == str:
#             value = value.capitalize()

#         print(f'{key.capitalize()}: {value}')

#     print("-" * 25)


# register_user(
#     name="Jesus",
#     age=24,
#     city="Guayaquil",
#     profession = "Student"
# )

# register_user(
#     name = "Valeria",
#     age = 26,
#     city = "Guayaquil",
#     profession = "Nutrition"
# )


# register_user(
#     name = "Valentina",
#     age = 19,
#     city = "Guayaquil",
#     proffesion = "Student"
# )

# def known_parameters(nombre, edad, *hobbies, **ubicacion):

#     print(f'''
# Nombre: {nombre.capitalize()}
# Edad: {edad}
# Hobbies: {hobbies}
# Ubicacion: {ubicacion}''')

#     print("-"* 25)


# known_parameters(
#     "Jesus",
#     25,
#     "Programar",
#     "Futbol",
#     "Entrenar",
#     ciudad="Guayaquil",
#     pais="Ecuador"
# )

# grades = [17,14,19,12,16,18,1]

# def lista(a,b,c,d,e,f,g):
#     return (f' Average: {(a + b + c + d + e + f + g) / 7}')

# print(lista(*grades))
# print("-" * 25)

# person = {
#     "nombre" : "Valeria",
#     "ubicacion" : "Guayaquil",
#     "profesion": "Nutricionista",
#     "hobbie": "leer"
# }
# def kwargs(nombre, ubicacion, profesion, hobbie):
#     print("Name:", nombre)
#     print("Ubicacion:", ubicacion)
#     print("Profesion:", profesion)
#     print("Hobbie:", hobbie)
#     print("-" * 25)

# kwargs(**person)

# def create_basic_user(name: str, age: int):
#     if not isinstance(name, str):
#         return None

#     if not isinstance(age, int):
#         return None

#     if name.strip() == "":
#         return None

#     if age not in range(1,121):
#         return None

#     print(f'Nombre: {name} - Edad: {age}')
#     print("-" * 25)

# create_basic_user("Ana", 24)
# create_basic_user("", 24)
# create_basic_user(123, 24)
# create_basic_user("Ana", "24")
# create_basic_user("Ana", -5)
# create_basic_user("Ana", 150)


# users = [
#     {
#         "id": 1,
#         "name": "Ana",
#         "age": 24
#     },
#     {
#         "id": 2,
#         "name": "Luis",
#         "age": 17
#     },
#     {
#         "id": 3,
#         "name": "Carlos",
#         "age": 31
#     },
#     {
#         "id": -5,
#         "name": "",
#         "age": 101
#     }
# ]

# def validate_user(user):
#     if not isinstance(user, dict):
#         return False

#     if "id" not in user:
#         return False

#     if "name" not in user:
#         return False

#     if "age" not in user:
#         return False

#     user_id = user["id"]
#     user_name = user["name"]
#     user_age = user["age"]

#     if not isinstance(user_id, int):
#         return False

#     if not isinstance(user_name, str):
#         return False

#     if not isinstance(user_age, int):
#         return False

#     if user_id < 0:
#         return False

#     if user_name.strip() == "":
#         return False

#     if user_age not in range(1, 101):
#         return False

#     return f"""
# -----------------
# ID:   {user_id}
# Name: {user_name}
# Age:  {user_age}
# -----------------"""

# for user in users:
#     print(validate_user(user))

# from typing import Any
# def validation_user(user:dict[str,Any]) -> bool:

#     if "id" not in user:
#         return False

#     if "name" not in user:
#         return False

#     if "age" not in user:
#         return False

#     if "status" not in user:
#         return False

#     user_id:int  = user["id"]
#     user_name:str  = user["name"]
#     user_age:int  = user["age"]
#     user_status: bool = user["status"]

#     if not isinstance(user_id, int):
#         return False

#     if not isinstance(user_name, str):
#         return False

#     if not isinstance(user_age, int):
#         return False

#     if not isinstance(user_status, bool):
#         return False

#     if user_id < 0:
#         return False

#     if user_name.strip() == "":
#         return False

#     if user_age not in range(1,101):
#         return False

#     return True

# users = [
#     {},
#     {"id": 1},
#     {"id": "1", "name": "Ana", "age": 24, "status": True},
#     {"id": 1, "name": "", "age": 24, "status": True},
#     {"id": 1, "name": "Ana", "age": -4, "status": True},
#     {"id": 1, "name": "Ana", "age": 24, "status": "sí"},
#     {"id": 1, "name": "Ana", "age": 24, "status": True},
#     {"id": 1, "name": "Ana", "age": 24, "status": True}
# ]

# for user in users:
    # print(validation_user(user))


# num_list:list[int] = [2,5,6,7,9,10,25]
# duplicate_numbers:list[int] =list(map(lambda x: x * 2, num_list))
# print(f"The duplicate numbers is: {duplicate_numbers}")

# sum_continous:list[int] = list(map(lambda x: x + 10, num_list))
# print(f'The constant sum the numbers are: {sum_continous}')

# word:str = "Hola, como estas"
# len_string:int = len(word)
# print(f'The leng string is: {len_string}')

# users:list[dict[str,Any]] = [
#     {"id": 1, "name": "Ana", "age": 20},
#     {"id": 2, "name": "Luis", "age": 17},
#     {"id": 3, "name": "Carlos", "age": 25}
# ]

# select_value:list[Any] = list(map(
#     lambda user: user["age"],
#     users
# ))
# print(select_value)

# check_condition:list[Any] = list(filter(
#     lambda user: user["age"] < 18,
#     users
# ))
# print(check_condition)


# products:list[dict[str,Any]] = [
#     {"name": "Laptop", "price": 900},
#     {"name": "Mouse", "price": 25},
#     {"name": "Monitor", "price": 300},
#     {"name": "Teclado", "price": 60}
# ]

# products_ordered_name:list[dict[str,Any]] = sorted(
#     products,
#     key= lambda product: product["name"]
# )

# products_ordered_price:list[dict[str,Any]] = sorted(
#     products,
#     key= lambda product: product["price"]
# )

# products_ordered_lenname:list[dict[str,Any]] = sorted(
#     products,
#     key= lambda product: len(product["name"])
# ) 

# print(products_ordered_name)
# print(products_ordered_price)
# print(products_ordered_lenname)

# def get_name(product:dict[str,Any]):
#     return product["name"]

# name:list[dict[str, Any]] = sorted(
#     products,
#     key= get_name
# )

# def get_price(product:dict[str,Any]):
#     return product["price"]

# price:list[dict[str, Any]] = sorted(
#     products,
#     key= get_price
# )
# def get_len_name(product:dict[str,Any]):
#     return len(product["name"])

# len_name: list[dict[str, Any]] = sorted(
#     products,
#     key= get_len_name
# )

# print(name)
# print(price)
# print(len_name)

# numbers: list[int] = [1, 2, 3, 4, 5]

# duplicate_numbers: list[int] = list(map(
#     lambda x: x * 2,
#     numbers
# ))
# print(duplicate_numbers)

# square:list[int] = list(map(
#     lambda x: x ** 2,
#     numbers
# )) 
# print(square)

# convert_string: list[str] = list(map(
#     lambda x: str(x),
#     numbers
# )) 

# print(convert_string)

# numbers:list[int]= [-5,2,-1,8,0,4,-3]

# positive:filter[int] = filter(
#     lambda x: x > 0,
#     numbers
# )

# negative:list[int]= list(filter(
#     lambda x: x < 0,
#     numbers
# ))

# even_numbers:list[int]= list(filter(
#     lambda x: x % 2 == 0,
#     numbers
# ))

# older_three:list[int] = list(filter(
#     lambda x: x > 3,
#     numbers
# ))

products:list[dict[Any,str|int]] = [
    {"name": "Laptop", "price": 900, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Monitor", "price": 300, "stock": 7},
    {"name": "Keyboard", "price": 60, "stock": 12}
]

# def sort_price(product)-> Any:
#     return product["price"]

# sort_by_price:list[dict[Any,str|int]] = sorted(
#     products,
#     key= sort_price
# )

# def mape_products(product) -> Any:
#     return product["price"]

# show_price:list[Any] = list(map(
#     mape_products, products
# ))

# def fill_products(product) -> Any:
#     return product["stock"]

# stock_products:list[Any]= list(filter(
#     lambda product: product["stock"] > 7,
#     products
# )) 

# sort_price:list[dict[str|int, Any]] = sorted(
#     products,
#     key= lambda product: product["price"],
#     reverse= True
# )

# map_products: list[Any]= list(map(
#     lambda product: product["price"],
#     products
# ))

# filter_product:list[Any] = list(filter(
#     lambda product: product["stock"] > 7,
#     products
# )) 
