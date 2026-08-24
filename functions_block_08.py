from re import search
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

products:list[dict[str|int, Any]] = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 900,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 25,
        "stock": 20
    },
    {
        "id": 3,
        "name": "Monitor",
        "price": 300,
        "stock": 7
    },
] 

def id_search(products,id:int) -> Any | None:
    if not isinstance(id, int):
        print("ERROR:ID is not a number")
        return None

    if id < 0:
        print("ERROR:ID connaot be less than 0")
        return None

    for product in products:
        if product["id"] == id:
            return product

    print("ERROR:ID not found.")
    return None

def name_search(products, name:str) -> Any | None:
    if not isinstance(name,str):
        print("ERROR:Name is not a text")
        return None
    
    if name.strip() == "":
        print("ERROR:The product name can never be empty.")

    for product in products:
        if product["name"] == name.capitalize():
            return product

    print("ERROR:Name not found")

def minimun_price(products) -> None:
    minimun = None

    for product in products:
        if minimun is None or minimun > product["price"]:
            minimun = product["price"]

    return minimun

def minimun_stock(products) -> None:
    minimum = None

    for product in products:
        if minimum is None or minimum > product["stock"]:
            minimum = product["stock"] 

    return minimum

def add_product(products, id,name,price,stock) -> None:
    new_id = id_search(products,id)
    new_name = name_search(products, name)

    if new_id or new_name:
        return None

    if new_id is None and new_name is None:

        if not isinstance(price, (int, float)):
            return None

        if price < 0:
            return None

        if not isinstance(stock, int):
            return None

        if stock < 0:
            return None

        new_product ={
            "id": id,
            "name": name,
            "price": price,
            "stock": stock
        }
        print("Product successfully added")
        products.append(new_product)

def sold_out(products) -> Any:
    found = False
    e
    for product in products:
        if product["stock"] == 0:
            print(f"The product: {product} It's out of stock")
            found=  True

    return found

def sort_products(products) -> list[Any] | None:
    option = int(input("""
1. Sort by price
2. Sort by stock
3. Sort by name
Choose one option: """))

    if option == 1:
        sort = sorted(
            products,
            key=lambda product: product["price"]
        )
        return sort

    elif option == 2:
        sort = sorted(
            products,
            key=lambda product: product["stock"]
        )
        return sort

    elif option == 3:
        sort = sorted(
            products,
            key=lambda product: product["name"]
        )   
        return sort

    else:
        return None

def resume_inventory(products) -> dict[str, Any]:
    amount:int = len(products)
    total:int|float = 0

    for product in products:
        total += product["price"] * product["stock"]

    return {
        "amount": amount,
        "value": total
    }

def print_products(products) -> None:
    for product in products:
        id:int = product["id"]
        name:str = product["name"]
        price:int|float = product["price"]
        stock:int = product["stock"]

        print(f"""
ID:    {id}
Name:  {name}
Pirce: {price}
Stock: {stock} 
---------------""")

while True:
    options = int(input(f"""
Choose the following options:
1. Search for a product by ID. 
2. Search for a product by name. 
3. Show minimum price. 
4. Show minimum stock. 
5. Add product. 
6. Product out of stock. 
7. Sort products.  
8. Resume inventory.
9. Print Products
10 Exit: """))

    if options == 1:
        fount_id = int(input("Enter an ID: "))

        search_id:Any | None = id_search(products, fount_id)
        if search_id is not None:
            print(f"ID found")
    elif options == 2: 
        found_name = str(input("Enter the name: ")).capitalize()

        search_name = name_search(products,found_name.capitalize())
        if search_name is not None:
            print(f'Name found')
    elif options == 3:
        print(f'The minimum price of the products is: {minimun_price(products)}')
    elif options == 4:
        print(f'The minimum stock of the products is: {minimun_stock(products)}')
    elif options == 5:
        new_id = int(input("Enter the ID you wish to add: "))
        new_name = str(input("Enter the name you want to add:" ))
        new_price = int(input("Enter the price you wish to add: "))
        new_stock = int(input("Enter the stock you wish to add: "))

        add_product(products,new_id,new_name,new_price, new_stock)
    elif options == 6:
        finish = sold_out(products)
        if not finish:
            print("There are no out-of-stock products.")
    elif options == 7:
        print("Entering option 7...")
        print(sort_products(products))
    elif options == 8:
        print(resume_inventory(products))
    elif options == 9:
        print_products(products)
    elif options == 10:
        print("Exit...")
        break
    else:
        print("Invalid option...")