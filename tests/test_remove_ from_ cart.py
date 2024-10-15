import pytest
from pages.start_page import StartPage
from pages.cart_page import CartPage
import time

@pytest.mark.usefixtures("init_driver", "base_url")
class TestRemoveFromCart:

    def test_remove_product_from_cart(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"

        # Открытие корзины
        time.sleep(6)
        cart_page.open_cart()

        # Удаление продукта из корзины
        cart_page.remove_product(product_id)

        # Проверка, что продукт удален из корзины
        assert cart_page.is_cart_empty(), "Product was not removed from the cart"
