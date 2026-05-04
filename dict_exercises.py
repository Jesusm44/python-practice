# user = {"name" : "frank",
#          "age" : 26,
#          "condition" : True
#          }

# if user["condition"]:

#     user["name"] = "Johan"
#     user["age"] = 23

#     if "country" not in user:
#         user["country"] = "Ecuador"


# print(user)


# product = { "name" : "splint",
#            "stock": 5,
#            "price": 70,
#            "availability" : True
#            }

# if product["availability"]:
#     if "name" in product:
#         product["name"] = "crutch"

# print(product)


# products = [
#     {"name" : "laptop", "priece" : 750, "condition" : True, "stock" : 9 },
#     {"name" : "cpu", "priece" : 230, "condition" : False, "stock" : 0 },
#     {"name" : "pantalla", "priece" : 750, "condition" : True, "stock" : 3 }
# ]

# for product in products:
#     if product["name"] == "laptop" or product["name"] == "pantalla" or product["name"] == "cpu":

#         if product["stock"] > 0:
#             product["stock"] -= 3

#         if product["stock"] <= 0 :
#             product["condition"] = False

#     if product["name"] == "cpu":
#         if product["stock"] == 0:
#             product["stock"] +=  1

#         if product["stock"] != 0:
#             product["condition"] = True

# print(products)


# data = [
#     {"name": "Juan", "age": 25},
#     {"name": "Maria"},
#     {"age": 30},
#     {"name": "Peter", "age": 20}
# ]

# invalid_data = []
# valid_data = []

# for dat in data:
#     if dat.get("name") and dat.get("age"):
#         valid_data.append(dat)
#     else:
#         invalid_data.append(dat)

# print(valid_data)
# print(invalid_data)


# users = [
#     {"name": "Juan", "balance": 100, "condition" : True},
#     {"name": "Maria", "balance": 50, "condition" : True},
#     {"name": "Peter", "condition" : False}
# ]


# for user in users:
#     if user.get("condition"):
#         if "balance" in user:
#             user["balance"] -= 10
#         print(f'{user}')
#     else:
#         print(f'Error: {user.get("name")} account blocked')


# data = [
#     {"name": "Juan", "age": 25},
#     {"name": "Maria"},
#     {"age": 30},
#     {"name": "Peter", "age": 20}
# ]

# valid_data = []
# invalid_data = []


# for dat in data:
#     if "name" in dat and "age" in dat:
#         valid_data.append(dat)
#     else:
#         invalid_data.append(dat)

# for dat in invalid_data:

#     if "name" not in dat:
#         name = input ("Enter name: ")
#         dat["name"] = name

#     if "age" not in dat:
#         age = int (input ("Enter age: "))
#         dat["age"] = age

#     valid_data.append(dat)



# print(valid_data)


# data = [10, "hola", 5, "mundo", -2, "python", 0, "farid"]

# data_number = {}
# data_name = {}
# new_names = {}
# new_numbers = {}

# count_names = 0
# count_numbers = 0

# for i in range(len(data)):
#     if isinstance(data[i], str):
#         data_name[i] = data[i]
#     else:
#         data_number[i] = data [i]

# for key in data_name:

#     new_names[f'name_{count_names}'] = data_name[key]
#     count_names += 1


# for key in data_number:

#     new_numbers[f'number {count_numbers}'] = data_number[key]
#     count_numbers += 1



# print(new_names)
# print(new_numbers)


# users = [
#     {"name": "Juan", "balance": 100, "condition" : True},
#     {"name": "Maria", "balance": 50, "condition" : True},
#     {"name": "Peter", "condition" : False},
#     {"name" : "Marcos", "balance" : 1500, "condition" : True},
#     {"name" : "Stefani", "balance" : 250, "condition" : True}
# ]

# for user in users:

#     withdrawal = int(input("enter withdrawal: "))

#     if user.get("condition"):

#         if user["balance"] - withdrawal  < 0:
#             user["balance"] -= withdrawal
#             print("ERROR: You do not have sufficient funds to withdraw.")

#         elif user["balance"] - withdrawal  > 0:
#             user["balance"] -= withdrawal
#             print(f'Withdrawal made')
#     else:
#         print(f'Error: {user.get("name")} account blocked')

# print(users)

# data = [
#     {"name": "Juan", "age": 25},
#     {"name": "Maria"},
#     {"name": "Juan", "age": 30},
#     {"age": 20}
# ]


# valid_users = []
# seen_names = set()


# valid_users = []
# seen_names = set()

# for user in data:

#     if "name" not in user:
#         user["name"] = input("Enter name: ")

#     if "age" not in user:
#         user["age"] = int(input("Enter age: "))

#     if user["age"] < 0 or user["age"] > 100:
#         print(f"Invalid age for {user['name']}")
#         continue

#     if user["name"] in seen_names:
#         print(f"Duplicate user: {user['name']}")
#         continue

#     seen_names.add(user["name"])
#     valid_users.append(user)

# print(valid_users)


# pharmacy = [{"name": "amoxicillin", "stock": 60, "priece" : 0.50},
#             {"name": "ibuprofen", "stock": 120, "priece" : 0.30},
#             {"name": "losartan", "stock": 10, "priece" : 0.25}
#             ]

# for product in pharmacy:
#     if "name" in product:
#         print(product["name"])


# data = [
#     {"name": "Juan", "age": 25},
#     {"name": "Maria"},
#     {"name": "Juan", "age": 30},
#     {"age": 20}
# ]

# set_data = set()
# valid_data = []

# for dat in data:

#     if "name" not in dat:
#         continue

#     if dat["name"] not in set_data:
#         set_data.add(dat["name"])
#         valid_data.append(dat)

# print(valid_data)


# usuarios = [
#     {"id": "u1", "nombre": "Juan", "edad": 20},
#     {"id": "u2", "nombre": "Ana", "edad": 25},
#     {"id": "u3", "nombre": "Pedro", "edad": 30},
#     {"id": "u4", "nombre": "Lucia", "edad": 22},
#     {"id": "u5", "nombre": "Carlos", "edad": 28}
# ]


# ids = set()
# valid_data = []
# invalid_data = []


# new_users = [
#     {"id": "u6", "nombre": "Juan", "edad": 20},
#     {"id": "u2", "nombre": "Ana", "edad": 25},
#     {"id": "u7", "nombre": "Michael", "edad": 86}
# ]


# for user in usuarios:
#     if user["id"] not in ids:
#         ids.add(user["id"])
#         valid_data.append(user)
#     else:
#         continue


# for user in new_users:
#     if user["id"] in ids:
#         invalid_data.append(user)
#     else:
#         ids.add(user["id"])
#         valid_data.append(user)


# print(valid_data)


# users = [
#     {
#         "name": "Juan",
#         "age": 25,
#         "hobbies": ["futbol", "leer", "programar"]
#     },
#     {
#         "name": "Maria",
#         "age": 30,
#         "hobbies": ["correr", "dibujar"]
#     }
# ]


# print(users[0]["hobbies"][1])
# print(users[1]["name"])


# empresa = {
#     "nombre": "TechCorp",
#     "empleados": [
#         {
#             "nombre": "Juan",
#             "skills": ["python", "sql"]
#         },
#         {
#             "nombre": "Maria",
#             "skills": ["javascript", "react"]
#         }
#     ]
# }

# print(empresa["empleados"][0]["skills"][0])


# for empleado in empresa["empleados"]:
#     print(empleado["nombre"])


# usuarios = [
#     {
#         "nombre": "Pedro",
#         "hobbies": ["leer"]
#     }
# ]

# usuarios[0]["nombre"] = "Pedro Gomez"
# usuarios[0]["hobbies"].append("Programar")

# print(usuarios)


# sistema = {
#     "usuarios": [
#         {
#             "id": "u1",
#             "datos": {
#                 "nombre": "Juan",
#                 "edad": 25
#             }
#         },
#         {
#             "id": "u2",
#             "datos": {
#                 "nombre": "Maria",
#                 "edad": 30
#             }
#         }
#     ]
# }


# print(
#     f'La edad de {sistema["usuarios"][1]["datos"]["nombre"]} es: '
#     f'{sistema["usuarios"][1]["datos"]["edad"]}'
# )


# sistema["usuarios"][0]["datos"]["edad"] = 26

# print(sistema)


# tienda = {
#     "productos": [
#         {
#             "nombre": "Laptop",
#             "precios": [1000, 1200, 1100]
#         },
#         {
#             "nombre": "Mouse",
#             "precios": [20, 25]
#         }
#     ]
# }

# print(f'El precio mas reciente de la lapto es: {tienda["productos"][0]["precios"][-1]}')

# tienda["productos"][1]["precios"].append(30)

# print(tienda)


# usuario = {
#     "nombre": "Juan",
#     "direccion": {
#         "ciudad": "Quito",
#         "pais": "Ecuador"
#     }
# }

# print(usuario["direccion"]["ciudad"])


# usuarios = [
#     {
#         "nombre": "Juan",
#         "hobbies": ["futbol", "leer"]
#     }
# ]

# print(usuarios[0]["hobbies"][1])


# sistema = {
#     "usuarios": [
#         {
#             "datos": {
#                 "nombre": "Juan",
#                 "edad": 25
#             }
#         }
#     ]
# }

# print(f'La edad es: {sistema["usuarios"][0]["datos"]["edad"]}')

# sistema["usuarios"][0]["datos"]["nombre"] = "Jose Maria"

# print(sistema)



# ordering_system = [
#     {
#         "id": "u1",
#         "client" : "Juan Soto",
#         "products" :
#         [
#             {
#             "name" : "Mouse",
#             "priece" : 10,
#             "amount" : 3
#             },
#             {
#             "name" : "keyboard",
#             "priece" : 30,
#             "amount" : 2
#             }
#         ]
#     }
# ]

# print(ordering_system)


# data = {
#     "usuarios" : 
#     [
#         {
#             "nombre" : "Juan", 
#             "edad" : 25, 
#             "activo" : None
#         },
#         {
#             "nombre" : "Maria",
#             "edad" : None,
#             "activo" : None
#         },
#         {
#             "nombre" : "Pedro",
#             "edad" : None,
#             "activo" : True
#         },
#         {
#             "nombre" : "Luis",
#             "edad" : None,
#             "activo" : None
#         }
#     ]
# } 

# print(data)

# usuarios = []
# usuarios.append(["juan", "maria"])
# usuarios.append({"edad" : 25, "color" : "rojo"})
# usuarios.append(["margarita", True])

# print(usuarios)

# usuarios = [
#     {
#         "nombre" : "Juan",
#         "edad" : 25,
#         "color_favorito" : "rojo",
#         "activo" : False
#     },
#     {
#         "nombre" : "Mapache",
#         "edad" : 12,
#         "color_favorito" : "azul diamante",
#         "activo" : False
#     },
#     {
#         "nombre" : "Margarita",
#         "edad" : 16,
#         "color_favorito" : "rosado",
#         "activo" : True
#     }
# ]


# customer_orders = [
#     {
#         "id" : "u1",
#         "cliente" : "Jesus",
#         "productos" :[
#             {
#                 "nombre" : "paracetamol",
#                 "precio" : 0.2,
#                 "cantidad" : 10
#             },
#             {
#                 "nombre" : "omeprazol",
#                 "precio" : 0.50,
#                 "cantidad" : 2
#             }
#             ],
#         "estado" : "enviando"
#     }
# ]


# print(customer_orders)


# usuario = {
#     "nombre": "",
#     "edad": -10,
#     "id": "u1"
# }

# for key, value in usuario.items():

#     if usuario["nombre"] == "":
#         new_name = input("Error: nombre vacio, ingrese un nuevo nombre: ")
#         usuario["nombre"] = new_name
#     else:
#         continue

#     if usuario["edad"] < 0:
#         new_edad = int(input("La edad es negativa, no pueden existir edades negativas. Ingresa" \
#                         "una nueva edad: "))
#         usuario["edad"] = new_edad

#     if usuario['id'] == "":
#         print("ERROR: VUELVA A INTENTARLO")
    
# print(usuario)


# usuarios = [
#     {"id": "u1", "nombre": "Juan"},
#     {"id": "u1", "nombre": "Maria"}
# ]

# ids = set()
# valid_user = []

# i = 0 

# for user in usuarios:

#     if user["id"] not in ids:
#         ids.add(user["id"])
#         valid_user.append(user)

#     else:
#         new_id = input(
#             f'ERROR: id repetido {user["id"]} en posición {i}. Nuevo id: '
#         )

#         user["id"] = new_id
#         ids.add(new_id)
#         valid_user.append(user)

#     i += 1  

# print(valid_user)


# users_datas = [
#     {
#         "id" : "u1",
#         "nombre" : "Margarita",
#         "apellido" : "Soto",
#         "edad" : 19,
#         "color_favorito" : "Morado"
#     },
#     {
#         "id" : "u2",
#         "nombre" : "Jose",
#         "apellido" : "Landaeta",
#         "edad" : 21,
#         "color_favorito" : "Rojo"
#     },
#     {
#         "id" : "u3",
#         "nombre" : "Valeria",
#         "apellido" : "Alcivar",
#         "edad" : 26,
#         "color_favorito" : "Rosado Pastel"
#     },
#     {
#         "id" : "u4",
#         "nombre" : "Miguel",
#         "apellido" : "Cabrera",
#         "edad" : 24,
#         "color_favorito" : "Azul Navy"
#     }
# ]

# set_ids = set()
# valids_data = []
# invalid_data = []
# i = 0

# for user in users_datas:
    
#     if user["id"] not in  set_ids:

#         if user["nombre"] == "":
#             nuevo_nombre = input("ERROR: Nombre vacio, Ingrese uno nuevo: ")
#             user["nombre"] = nuevo_nombre
#         elif user["apellido"] == "":
#             nuevo_apellido = input("ERROR: Apellido vacio, Ingresa uno nuevo: ")
#             user["apellido"] == nuevo_apellido

#         if user["edad"] <= 0:
#             nueva_edad = int(input("ERROR: la edad no puede ser negativa, Ingrese una nueva edad: "))
#             user["edad"] = nueva_edad
        
#         set_ids.add(user["id"])
#         valids_data.append(user["id"])

#     else:
#         nueva_id = input("ERROR id reptida. Ingrese una nueva id: ")
#         user["id"] = nueva_id
#         set_ids.add(nueva_id)
        

# print(users_datas)
            

# entrada = [
#     {"id": "u1", "nombre": "Juan", "edad": 25},
#     {"id": "u2", "nombre": "", "edad": 30},
#     {"id": "u1", "nombre": "Pedro", "edad": -5},
#     {"nombre": "Maria", "edad": 20}
# ]        

# ids = set()

# entrada_valida = []
# entrada_invalida = []

# count = 1


# for data in entrada:

#     if "id" in data:
#         if data["id"] in ids: 
#             print(f'ERROR: el usuario {count}, tiene un id repetido')
#             entrada_invalida.append(data)
#         if data["nombre"] == "":
#             print(f'ERROR: el usuario {count}, no tiene nombre ')
#             entrada_invalida.append(data)
#         if data["edad"] <= 0:
#             print(f'ERROR: el usuario {count}, tiene una edad inadecuada ')
#             entrada_invalida.append(data)
#         else:
#             print(f'El usuario {count}, ha sido agregado exitosamente')
#             ids.add(data["id"])
#             entrada_valida.append(data)
    
#     else:
#         print(f'ERROR: No hay id en el usuario {count}, se agregara a invalidos')
#         entrada_invalida.append(data)


#     count += 1


# usuarios = [
#     {"id": "u1", "edad": 20},
#     {"id": "u2", "edad": 30},
#     {"id": "u3", "edad": 25}
# ]

# usuarios_mayores = []


# for usuario in usuarios:

#     if usuario["edad"] > 25:
#         usuarios_mayores.append(usuario)
    
#     if usuario["id"] == "u2":
#         print(f'El usuario con id u2 es: {usuario}')
#         break

# usuarios = [
#     {"id": "u1", "edad": 15},
#     {"id": "u2", "edad": 30},
#     {"id": "u3", "edad": 40}
# ]


# for usuario in usuarios:

#     count = 1

#     if usuario["edad"] < 18:
#         continue

#     if usuario["edad"] > 25:
#         count += 1
#         print(f'Encontramos el primer usuario mayor a 25 en la posicion, '
#               f'{count} y  es {usuario}')
#         break


# usuarios = [
#     {"id": 1, "edad": 15},
#     {"id": 2, "edad": 17},
#     {"id": 3, "edad": 17},
#     {"id": 4, "edad": 18},
#     {"id": 5, "edad": 21},
#     {"id": 6, "edad": 30},
#     {"id": 7, "edad": 15}
# ]


# for usuario in usuarios:

#     if usuario["edad"] >= 18:
        
#         print(f'Usuario encontrado, el id el usuario es: '
#               f'{usuario["id"]}')
        # break
        

# datos = [
#     ["Juan", 25],
#     {"nombre": "Maria"},
#     {"id": "u2"}
# ]

# claves = ["id","nombre" , "edad"]

# nuevos_valores = []
# valores_invalidos = []
# valores_validos = []


# for dato in datos:

#     if isinstance(dato, list):
#         if len(dato) >= 2:
#             nuevo_dict = {"id" : None, claves[1] : dato[0], claves[2] : dato[1]}
#             nuevos_valores.append(nuevo_dict)

#     elif isinstance (dato, dict):
#         nuevo_2 = {}
#         for clave in claves:
#             if clave in dato:
#                 nuevo_2[clave] = dato[clave]
#             else:
#                 nuevo_2[clave] = None
        
#         nuevos_valores.append(nuevo_2)


# for valor in nuevos_valores:
#     es_valido = True 


#     if valor["id"] is None:
#         es_valido = False

#     if valor["nombre"] is None or valor["nombre"] == "":
#         es_valido = False

#     if valor["edad"] is None or valor["edad"] < 0:
#         es_valido = False

#     if es_valido:
#         valores_validos.append(valor)
#     else:
#         valores_invalidos.append(valor)    