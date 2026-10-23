# class Tank:
#     def __init__(self, capacity, current_amount):
#         if capacity <= 0:
#             raise ValueError("Invalid capacity")
        
#         if not(0<= current_amount <= capacity):
#             raise ValueError("Invalid initial amount")
        
#         self.capacity = capacity
#         self.current_amount = current_amount

#     def add(self, liters):
#         if liters <= 0:
#             raise ValueError("Liters must be positive")

#         new_capacity = self.current_amount + liters

#         if new_capacity > self.capacity:
#             raise ValueError("Maximum capacity exceeded")
#         self.current_amount = new_capacity

#     def extract(self, liters):
#         if liters <= 0:
#             raise ValueError("Liters must be positive")
#         extract_capacity = self.current_amount - liters

#         if extract_capacity < 0:
#             raise ValueError("Not enough water")
#         self.current_amount = extract_capacity

class Deposito:    
    def __init__(self, capacidad, cantidad_actual):
        if capacidad <= 0:
            raise ValueError("Capacidad inválida")
        if cantidad_actual < 0 or cantidad_actual > capacidad:
            raise ValueError("Cantidad inicial inválida")
        self.capacidad = capacidad
        self.cantidad_actual = cantidad_actual

    def agregar(self, litros):
        self.cantidad_actual += litros
        if litros <= 0:
            raise ValueError("Los litros deben ser positivos")
        if self.cantidad_actual > self.capacidad:
            raise ValueError("Se supera la capacidad máxima")
            return self.cantidad_actual

    def extraer(self, litros):
        self.cantidad_actual -= litros
        if litros <= 0:
            raise ValueError("Los litros deben ser positivos")
        if self.cantidad_actual < 0:
            raise ValueError("No hay suficiente agua")
        return self.cantidad_actual