import pytest
from bbe.pages.start_page import StartPage
from bbe.pages.cart_page import CartPage
from bbe.pages.checkout_page import CheckoutPage
import time

@pytest.mark.usefixtures("init_driver", "base_url")
class TestCheckoutValidation:

    def test_checkout_validation(self, base_url):
        # Инициализация страниц
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # ID продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"

        # Открытие корзины
        time.sleep(7)
        cart_page.open_cart()

        # Нажатие на кнопку "Оформить заказ"
        cart_page.click_checkout_button()

        # Проверка, что страница оформления заказа открыта
        assert checkout_page.is_checkout_page_opened(), "Checkout page did not open."

        # Ввод данных для оформления заказа
        checkout_page.enter_contact_phone("123456")
        checkout_page.enter_city("Москва")
        checkout_page.enter_comment("Запакуйте квадрат в квадратную коробку, пожалуйста")
        checkout_page.enter_contact_person("Василий Василевский")
        checkout_page.enter_email("qwerty@gmail.com")

        time.sleep(5)
        # Подтверждение заказа
        checkout_page.confirm_order()

        time.sleep(5)
