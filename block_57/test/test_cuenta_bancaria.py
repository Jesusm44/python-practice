import pytest
from block_57.cuenta_bancaria import CuentaBancaria

def test_saldo_inicial():
    usuario_1 = CuentaBancaria("Juan")
    mostrar_saldo = usuario_1.saldo
    assert mostrar_saldo == 0


def test_deposito_fondos():
    usuario_1 = CuentaBancaria("Juan")
    usuario_1.aumentar_saldo(12)

    assert usuario_1.saldo == 12

def test_retiro_de_fondos():
    usuario_uno = CuentaBancaria("Maria")
    usuario_uno.aumentar_saldo(75)
    usuario_uno.disminuir_saldo(12)

    assert usuario_uno.saldo == 63

def test_retiro_sin_fondos():
    usuario_1 = CuentaBancaria("Juan")
    with pytest.raises(ValueError):
        usuario_1.disminuir_saldo(12)

    assert usuario_1.saldo == 0
