import pytest
from bbe.pages.start_page import StartPage


@pytest.mark.usefixtures("init_driver", "base_url")
class TestAddToCart:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
