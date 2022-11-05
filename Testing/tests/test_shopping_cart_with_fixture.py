import sys
import pytest
sys.path.insert(1, "E:\Github\Python - Utils\Testing")

from src.shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart(10)


def test_check_add_item(cart):
    cart.add_item("apple")
    assert cart.get_size() == 1


def test_check_if_item_present(cart):
    cart.add_item("orange")
    assert "orange" in cart.get_items()


def test_max_size(cart):
    for _ in range(10):
        cart.add_item("mango")

    with pytest.raises(OverflowError):
        cart.add_item("mango")
    

def test_total_price(cart):
    cart.add_item("apple")
    cart.add_item("orange")

    assert cart.get_total() == 3
