# users = {}

# usuario["name"] = "Jesus"
# usuario["age"] = 25
# usuario["country"] = "Ecuador"

# print(usuario)

# users = {"name": "Juan"}

# users["name"] ; users["edad"]
# users.get("name") ; users.get("edad")


# users = {"nombre" : "Juan" , "age": 25}

# users["age"] = 16

# if "email" not in users:
#     users["email"] = "yimejia44@gmail.com"

# del users["nombre"]

# print(users)


# data = ["Juan", 25, "Ecuador"]
# keys = ["name", "age", "country"]

# dict_data = {}

# for i in range(len(data)):
#     dict_data[keys[i]] = data[i]

# print(dict_data)


# users = {"Nombre": "Juan",
#            "edad" : 25,
#            "country" : "Ecuador"}

# for key in users:
#     print(key)

# users = {"Nombre": "Juan",
#            "edad" : 25,
#            "country" : "Ecuador"}

# for key in users:
#     value = users[key]
#     print(f'{key} → {value}')

# users = {"Nombre": "Juan",
#            "edad" : 25,
#            "country" : "Ecuador"}

# for key in users:
#     if key == "edad":
#         value = users[key]
#         print(value)


# users = {"Nombre": "Juan",
#            "edad" : 25,
#            "country" : "Ecuador"}


# for key in users:
#     if key == "country":
#         continue
#     else:
#         value = users[key]
#         print(value)


# users = {"Nombre": "Juan",
#            "edad" : 25,
#            "country" : "Ecuador"}

# found = False

# for key in users:
#     if key == "email":
#         found = True

# if found:
#     print("existe")
# else:
#     print("no existe")



# users = {"Nombre": "Juan",
#            "edad" : 25,
#            "country" : "Ecuador"}

# count = 0

# for key in users:
#     count += 1

# print(f'The number of keys counted is: {count}')


# data = {"a" : 1,
#         "b" : 2,
#         "c" : 3,
#         "d" : 4}

# for key in data:
#     if key == "a" or key == "c":
#         print(key)


# data = {"a": 1,
#         "b": 2,
#         "c": 3,
#         "d": 4
#         }

# for key in data:
#     value = data[key]
#     print(f'{key}: {value}')


# users = {
#     "Name": "Juan",
#     "Age": 25,
#     "Country": "Ecuador"
#     }

# count = 0

# dic_keys = users.keys()
# print(dic_keys)


# for key in users.keys():
#     values = users[key]
#     print(f'{key} → {values}')

# if "Age" in users.keys():
#     print("There exists")
# else:
#     print("It doesn't exist.")

# for key in users.keys():
#     count += 1

# print(count).


# data = {
#     "a": 1,
#     "b": 2,
#     "c": 3
#     }

# for key in data.keys():
#     if key != "b":
#         print(f'The key elements that should not be ignored are: {key}')      


# users = {
#     "name": "Juan",
#     "age": 25,
#     "country": "Ecuador"
# }

# value = users.values()
# print(value)

# for value in users.values():
#     print(value)

# if "Juan" in users.values():
#     print("There exists")
# else:
#     print("It doesn't exist.")

# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }

# total_values = 0
# over_Fifteen = []

# for value in data.values():
#     if value > 15:
#         over_Fifteen.append(value)
#     total_values += value

# print(total_values)
# print(over_Fifteen)


# users = {
#     "name": "Juan",
#     "age": 25,
#     "country" : "Ecuador"
# }

# for key, value in users.items():
#     print(f'{key} → {value}')

#     if value == "Juan":
#         print(key)

#     if key == "age":
#         print(value)


# data = {
#     "a" : 10,
#     "b" : 20,
#     "c" : 30
# }

# total_values = 0

# for key, value in data.items():
#     total_values += value

# print(f'The total sum are: {total_values}')

# for key, value in data.items():
#     if value > 15:
#         print(f'{key}: {value}')
        

# usuarios = [
#     {"name": "Juan", "age": 25},
#     {"name": "Maria", "age": 30}
# ]


# products = [
#     {"name" :"laptop", "price": 789},
#     {"name" : "Iphone", "price" : 1500},
#     {"name" : "Air-fryer", "price" : 56}
# ]


# productos = [
#     {"nombre": "Laptop", "precio": 1200},
#     {"nombre": "Mouse", "precio": 25}
# ]

# for product in productos:
#     print(product["nombre"])


# users = {"name": "Juan"}

# if "age" in users:
#     print("There exists.")
# else:
#     print("It doesn't exist.")


# users = {}

# if "age" not in users:
#     users["age"] = 0

# users["age"] += 1


# users = {"name" : "Juan",
#          "age" : 25
#          }

# if "age" in users:
#     users["age"] = 30

# print(users)


# user = {}

# user["age"] = user.get("age",0)
# print(user)

# user = {"active": True, 
#         "balance": 100
#         }

# if user.get("active"):
#     user["balance"] -= 10
# else:
#     print("User not active")

# print(user)


# count = {}
# datas = ["a", "b", "a", "c", "b", "a"]


# for data in datas:
#     count[data] = count.get(data,0) + 1

# print(count)


# base = {"activo": True}

# a = base
# b = base

# a["activo"] = False

# print(b["activo"])


# usuarios = [1]
# base = {"activo": False}

# for i in range(3):
#     usuarios.append(base)

# print(usuarios)