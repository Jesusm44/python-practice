from pydoc import text


class Libro:
    def __init__(self,autor, titulo) -> None:
        if not isinstance(autor, str):
            raise ValueError("El autor no es valido")
        
        if not isinstance(titulo, str):
            raise ValueError("El titulo es valido.")

        if not autor.strip():
            raise ValueError("EL autor no es valido.")

        if not (titulo.strip() and len(titulo.strip()) >= 2):
            raise ValueError("EL autor no es valido.")

        self.autor = autor
        self.titulo = titulo

    def __str__(self) -> str:
        return f"{self.autor} — {self.titulo}"

class Biblioteca:
    def __init__(self) -> None:
        self._libros = {}

    def agregar_libro(self, libro:Libro):
        if isinstance (libro, Libro):
            if libro.autor in self._libros:
                for libro_registrado in self._libros[libro.autor]:
                    if libro_registrado.titulo == libro.titulo:
                        raise ValueError("El titulo ya esta registrado.")
                self._libros[libro.autor].append(libro)
            else:
                self._libros[libro.autor] = [libro]

    def buscar_libro(self,autor:str, titulo:str):
        if autor in self._libros:
            for libro_registrado in self._libros[autor]:
                if libro_registrado.titulo == titulo:
                    return libro_registrado
            raise ValueError(f"El {titulo} no se encuentra")
        else:
            raise ValueError("EL libro no existe.")
    
    @property
    def consultar_libros(self):
        return str(self)

    def __str__(self):
        texto = ""
        for libros in self._libros.values():
            for libro in libros:
                texto += str(libro) + "\n"
        return texto 


libro_1 = Libro(
    autor="Fredirick William",
    titulo="Atrapados"
)

libro_2 = Libro(
    autor="Fredirick William",
    titulo="La resistencia"
)
biblioteca = Biblioteca()

biblioteca.agregar_libro(libro_1)
biblioteca.agregar_libro(libro_2)
print(biblioteca.buscar_libro("Fredirick William", "La resistencia"))

consulta = biblioteca.consultar_libros
print(consulta)

