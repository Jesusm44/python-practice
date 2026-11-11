class Termostato:
    def __init__(self, temperatura) -> None:
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura_objetivo

    @temperatura.setter
    def temperatura(self,nueva_temparuta):
        if not (15 <= nueva_temparuta <= 22):
            raise ValueError("La nueva temperatura no esta dentro del rango.")

        self._temperatura_objetivo = nueva_temparuta