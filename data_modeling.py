# data = [
#     ["Juan", "25"],
#     ["Maria", " 30 "],
#     ["Luis", "abc"],
#     ["Ana"],
#     []
# ]

# keys = ["name", "age"]

# valid_users = []


# for d in data:

#     new_dict = {"name" : None, "age" : None}

#     if isinstance(d,list):

#         if len(d) >= 1:
#             new_dict["name"] = d[0]

#         if len(d) >= 2:
#             if isinstance(d[1],str):
#                 value = d[1].strip()
#                 if value.isdigit():
#                     new_value = int(value)
#                     new_dict["age"] = d[1]
#                 else:
#                     new_dict["age"] = None
#             else:
#                 new_dict["age"] = d[1]

#         valid_users.append(new_dict)

# print(valid_users)


# users = [
#     {"id": "u1", "name": "Juan", "age": 25},
#     {"id": "u2", "name": "", "age": 30},
#     {"id": "u3", "name": "Maria", "age": -5},
#     {"id": None, "name": "Pedro", "age": 20}
# ]

# invalid_users = []
# valid_users = []

# for user in users:

#     if user["id"] == None:
#         invalid_users.append(user)

#     elif user["name"] == "":
#         invalid_users.append(user)

#     elif user["age"] <= 0:
#         invalid_users.append(user)

#     else:
#         valid_users.append(user)

# print(valid_users)
# print(invalid_users)


# users = [
#     {"id": "u1", "name": "Juan", "age": 25},
#     {"id": "u2", "name": "", "age": 30},
#     {"id": "u3", "name": "Maria", "age": -5},
#     {"id": None, "name": "Pedro", "age": 20},
#     {"id": None, "name": "", "age": 26}
# ]


# valid_users = []
# invalid_users = []

# for user in users:

#     invalid_dicts = {
#             "data" : user,
#             "errors" : []
#         }

#     if user["id"] == None:
#         invalid_dicts["errors"].append("Missing id")


#     if user["name"] == "":
#         invalid_dicts["errors"].append("error name")

#     if user["age"] <= 0:
#         invalid_dicts["errors"].append("Invalid age")

#     invalid_users.append(invalid_dicts)

# print(invalid_users)


# users = [
#     {"id": "u1", "name": "Juan"},
#     {"id": "u2", "name": "Maria"},
#     {"id": "u1", "name": "Pedro"}
# ]

# ids = set()

# valid_users = []

# for user in users:
#     if user["id"] not in ids:
#         ids.add(user["id"])
#         valid_users.append(user)

# print(valid_users)


# users = [
#     {"name": "Juan", "age": 17},
#     {"name": "Maria", "age": 25},
#     {"name": "Pedro", "age": 30}
# ]

# age_valid = []
# for user in users:
#     if user["age"] > 25:
#         break
#     if user["age"] > 18:
#         age_valid.append(user)
#     else:
#         continue


# data = [
#     ["Juan", "25"],
#     ["Maria", "30"],
#     ["Juan", "25"]
# ]

# normalized_users = []

# for d in data:

#     data_dict = {"name" : None, "age" : None}

#     if len(d) >= 1:
#         data_dict["name"] = d[0]

#     if len(d) >= 2:
#         if isinstance(d[1],str):
#             value = d[1].strip()
#             if value.isdigit():
#                 f_value = int(value)
#                 data_dict["age"] = f_value
#             else:
#                 data_dict["age"] = None
#         else:
#             data_dict["age"] = d[1]

#     normalized_users.append(data_dict)

# name_users = set()
# age_users = set()
# valid_users = []
# invalid_useres = []


# for user in normalized_users:

#     dict_internal = {
#         "user": user,
#         "errors" :[]
#     }




#     if user["name"] in name_users and user["age"] in age_users:
#         dict_internal["errors"] = "ERROR: Name duplicate"
#         invalid_useres.append(dict_internal)

#     else:
#         if user["name"] == "":
#             dict_internal["errors"] = "No name Error"
#         if user["age"] <= 0:
#             dict_internal["errors"] = "Error: age inavlid"
#         name_users.add(user["name"])
#         age_users.add(user["age"])
#         valid_users.append(user)




# print(invalid_useres)


# users = [
#     {"id" : "u1", "name" : "Marcos", "age" : 25},
#     {"id" : "u2", "name" : "Michael", "age" : 37},
#     {"id" : "u3", "name" : "Julietta", "age" : 29}
# ]


# for user in users:
#     print(user)


# users = [
#     {"id": 1, "name": "Ana", "age": 20},
#     {"id": 2, "name": "Luis", "age": 25},
#     {"id": 3, "name": "Carlos", "age": 17}
# ]

# for user in users:

#     print(user["name"])

#     if user["age"] > 18:
#         print(user)
    
# new_user = {"id": 4, "name": "Mike", "age": 32}

# users.append(new_user)

# for user in users:

#     if user["id"] == 4:
#         print("User added successfully")


# users = [
#     {"id": 1, "username": "john_doe"},
#     {"id": 2, "username": "jane_smith"},
#     {"id": 2, "username": "alex_jones"},
#     {"id": 3, "username": "john_doe"},
#     {"id": 4, "username": "mike_brown"},
#     {"id": 1, "username": "emma_wilson"}
# ]


# valid_users = []
# ids = set()


# for user in users:

#     if user["id"] not in ids:
#         ids.add(user["id"])
#         valid_users.append(user)
#     else:
#         print(f'Error: repeat user {user}')


# products = [
#     {"id": 1, "name": "Laptop", "price": 900},
#     {"id": 2, "name": "Mouse", "price": 25},
#     {"id": 3, "name": "Teclado", "price": 50}
# ]

# filter_list = []

# for product in products:

#     if product["priece"] > 100:
#         filter_list.append(product)


users = []

ids = set()

while True:

    print("option 1. add user")
    print("option 2. Found id")
    print("option 3. Modify age")
    print("option 4. Modify name")
    print("option 5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        user_id = int(input("id is: "))
    
        if user_id in ids:
            print("ERROR: the id already exists")
        else:
            name = input("name: ")
            age = int(input("age: "))

            user = {
                "id" : user_id,
                "name" : name,
                "age" : age
            }

            users.append(user)
            ids.add(user_id)

            print("Saved user")
    
    elif option == "2":
        search_id = int(input("Enter the id: "))

        found = False

        for user in users:
            if user["id"] == search_id:
                print("User found")
                modifi = input("you want to modify it: yes / no")

                if modifi == "yes":
                    age_name = input("Option 1: Modify age, Option 2: Modify name")
                else:
                    continue
                found = True
                break
            if not found:
                print("The user does not exist.")



    elif option == "5":
        print("Exit...")
        break

    else:
        print("Invalid opcion")
            


    

