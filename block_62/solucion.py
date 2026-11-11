class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def aumentar_cantidad(self, monto):
        if monto <= 0:
            raise ValueError("ERROR: No se puede aumentar.")

        self.cantidad += monto
        
    def __str__(self) -> str:
        return f"""Product: {self.nombre} - Canidad: {self.cantidad}"""

class Contenedor:
    def __init__(self):
        self._contenedor = {}

    def agregar_product(self, producto:Producto):
        if producto.nombre not in self._contenedor:
            self._contenedor[producto.nombre] = producto
        else:
            raise ValueError ("EL producto ya se encuentra registrado")
    
    def consultar_cantidad(self, nombre):
        if nombre in self._contenedor:
            return self._contenedor[nombre].cantidad
        else:
            raise ValueError("El producto no se encuentra.")

    def __str__(self)  -> str:
        texto = ""
        for producto in self._contenedor.values():
            texto += str(producto) + "\n"
        return texto
    
    @property
    def mostrar_contenedor(self):
        return self._contenedor.copy()