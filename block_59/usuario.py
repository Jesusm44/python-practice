class UsuarioVideojuego:
    carcater_especial = "@#%_-"
    def __init__(self,name,nickname, password) -> None:
        if len(name.strip()) < 3:
            raise ValueError("EL nombre no puede tener menos de 3 caracteres.")

        if not nickname.strop():
            raise ValueError("EL nicknmae no puede estar vacio.")

        if len(password) < 3:
            raise ValueError("La contrasena no puede ser menor a 3 digitos")

        if not any(caracter in self.carcater_especial for caracter in password):
            raise ValueError ("La contrasena debe incluir un carcater especial :@, #, %, _, -")

        self._name:str = name
        self.__password:str = password
        self.nickname:str = nickname