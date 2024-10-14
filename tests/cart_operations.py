import time
import pytest
from bbe.pages.start_page import StartPage
from bbe.pages.cart_page import CartPage

@pytest.mark.usefixtures("init_driver", "base_url")
class TestRemoveFromCart:

    def test_remove_product_from_cart(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # Открытие корзины
        cart_page.open_cart()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление 2 единиц продукта в корзину
        cart_page.add_product_to_cart(product_id, quantity=2)


        # Проверка, что товар добавлен в корзину
        assert cart_page.is_product_added_to_cart(product_id), "Product was not added to cart"

        time.sleep(5)
        self.driver.refresh()


        # Проверка, что количество товара в корзине 2
        quantity_in_cart = cart_page.get_product_quantity()
        print(f"Количество товара в корзине: {quantity_in_cart}")  # Для отладки
        assert quantity_in_cart == "2", f"Expected quantity '2', but got '{quantity_in_cart}'."

        # Удаление продукта из корзины
        cart_page.remove_product(product_id)

        # Проверка, что продукт удален из корзины
        assert cart_page.is_cart_empty(), "Product was not removed from the cart"
