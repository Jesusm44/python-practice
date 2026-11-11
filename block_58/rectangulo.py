class Rectangulo:
    def __init__(self,ancho, alto) -> None:
        if ancho < 0 or alto < 0:
            raise ValueError("EL ancho y el alto no pueden ser negativos.")

        self._ancho:int = ancho
        self._alto:int = alto

    @property
    def ancho(self) -> int:
        return self._ancho

    @property
    def alto(self) -> int:
        return self._alto

    @ancho.setter
    def ancho(self, nuevo_ancho:int):
        if nuevo_ancho < 0:
            raise ValueError("El nuevo ancho no puede ser negativo.")

        self._ancho = nuevo_ancho

    @alto.setter
    def alto(self, nuevo_alto:int):
        if nuevo_alto < 0:
            raise ValueError("El nuevo alto no puede ser negativo.")

        self._alto = nuevo_alto

    @property
    def calcular_area(self) -> int:
        area: int = self._ancho * self._alto
        return area

rectangulo: Rectangulo = Rectangulo(17, 21)
print(rectangulo.ancho)
print(rectangulo.alto)
print(rectangulo.calcular_area)
