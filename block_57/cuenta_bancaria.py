class CuentaBancaria:
    def __init__(self,usuario) -> None:
        self.usuario = usuario
        self._saldo = 0

    def aumentar_saldo(self, monto):
        if monto <= 0:
            raise ValueError("El monto ingresado no puede menor a 0")
        
        self._saldo += monto

    def disminuir_saldo(self, monto):
        if monto <= 0:
            raise ValueError("El monto ingresado no puede menor a 0")

        nuevo_monto = self._saldo - monto

        if nuevo_monto < 0:
            raise ValueError("El saldo en tu cuenta no puede ser naegativo.")

        self._saldo = nuevo_monto

    @property
    def saldo(self):
        return self._saldo