# from typing import Any

# users:list[Any] =[]

# def create_save_user(id: int, name:str, age: int):
#     if  not isinstance(id, int):
#         return None

#     if not isinstance(name, str):
#         return None

#     if not isinstance(age, int):
#         return None

#     for user in users:
#         if id == user["id"]:
#             return None

#     if id < 0 or age < 0:
#         return None 

#     if name.strip() == "":
#         return None

#     new_user:dict[str, Any] = {
#         "id" : id,
#         "name": name,
#         "age":age
#     }
 
#     users.append(new_user)
#     return new_user


# def delete_user(users, user_id):
#     found = False

#     for user in users:
#         if user_id == user["id"]:
#             found = True

#             delete = str(input("Are you sure you want to delete it? Y for yes, N for no: ")).upper()

#             if delete == "Y":
#                 users.remove(user)
#                 print("The user has been successfully removed.")
#                 break
#             elif delete == "N":
#                 print("The user has not been deleted.")
#             else:
#                 print("ERROR")

#     if found is not True:
#         print("ERROR: ID not found")

#     return users

print("usuarios fue importado")
