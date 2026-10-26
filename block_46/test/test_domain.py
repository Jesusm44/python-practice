from itertools import product

import pytest
from block_20.inventory_creator import product_register
from block_46.products import Products
from block_46.services import increase_product_stock, decrease_product_stock,search_product,register_products

def test_product():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )

    assert new_product.code == "A127" 

def test_consult():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )
    new_product.consult_stock()

    assert new_product.consult_stock() == 17

def test_add_stock():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )
    new_product.add_stock(170)
    assert new_product.stock == 187

def test_add_stock_invalid():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )
    with pytest.raises(ValueError):
        new_product.add_stock(-1)
    assert new_product.stock == 17

    with pytest.raises(ValueError):
        new_product.add_stock(0)

def test_substrack_stock():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )
    new_product.reduce_stock(15)
    assert new_product.stock == 2

def test_substrack_stock_invalid():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )
    with pytest.raises(ValueError):
        new_product.reduce_stock(18)
    assert new_product.stock == 17


def test_substrack_stock_invalid_negative():
    new_product = Products(
        code = "A127",
        name="Keyboard",
        stock=17
    )
    with pytest.raises(ValueError):
        new_product.reduce_stock(-1)

products = {}

def test_rgister_products():
    new_product = register_products(
        products=products,
        code="A123",
        name="CPU",
        stock=15
    )

    assert "A123" in products
    assert isinstance(products["A123"], Products)
    assert products["A123"].stock == 15

def test_decrease_product_stock():
    products = {}

    register_products(
        products=products,
        code="A123",
        name="CPU",
        stock=15
    )
    with pytest.raises(ValueError):
        decrease_product_stock(
            products=products,
            code="A123",
            quantity=18
        )

    assert products["A123"].stock == 15





