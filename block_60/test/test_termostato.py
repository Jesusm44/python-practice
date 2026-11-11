import pytest
from block_60.termostato import Termostato

def test_limite_minimo():
    termostato = Termostato(15)
    assert termostato._temperatura_objetivo == 15

def test_limite_maximo():
    termostato = Termostato(22)
    assert termostato._temperatura_objetivo == 22

def test_temperatura_intermida():
    termostato = Termostato(19)
    assert termostato._temperatura_objetivo == 19

def test_valor_inferior_invalido():
    termostato = Termostato(15)
    with pytest.raises(ValueError):
        termostato.temperatura = 14
    assert termostato._temperatura_objetivo == 15

def test_valor_superior_invalido():
    termostato = Termostato(22)
    with pytest.raises(ValueError):
        termostato.temperatura = 24
    assert termostato._temperatura_objetivo == 22