# from typing import Any

# products:list[Any] =[]

# def create_save_product(id: int, name:str, price: int | float, stock: int):
#     if  not isinstance(id, int):
#         return None

#     if not isinstance(name, str):
#         return None

#     if not isinstance(price, int | float):
#         return None

#     if not isinstance (stock, int):
#         return None

#     for product in products:
#         if id == product["id"]:
#             return None

#     if id < 0 or price < 0 or stock < 0:
#         return None 

#     if name.strip() == "":
#         return None

#     new_product:dict[str, Any] = {
#         "id" : id,
#         "name": name,
#         "price": price,
#         "stock": stock
#     }
 
#     products.append(new_product)
#     return new_product


# def delete_product(products, new_id):
#     found = False

#     for product in products:
#         if new_id == product["id"]:
#             found = True

#             delete = str(input("Are you sure you want to delete it? Y for yes, N for no: ")).upper()

#             if delete == "Y":
#                 products.remove(product)
#                 print("The product has been successfully removed.")
#                 break
#             elif delete == "N":
#                 print("The product has not been deleted.")
#             else:
#                 print("ERROR")

#     if found is not True:
#         print("ERROR: ID not found")

#     return products