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

def create_basic_user(name: str, age: int):
    if not isinstance(name, str):
        return None

    if not isinstance(age, int):
        return None

    if name.strip() == "":
        return None

    if age not in range(1,121):
        return None

    print(f'Nombre: {name} - Edad: {age}')
    print("-" * 25)

create_basic_user("Ana", 24)
create_basic_user("", 24)
create_basic_user(123, 24)
create_basic_user("Ana", "24")
create_basic_user("Ana", -5)
create_basic_user("Ana", 150)


