import pytest
from pages.start_page import StartPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

@pytest.mark.usefixtures("init_driver", "base_url")
class TestCheckoutEmptyValidation:

    def test_checkout_empty_validation(self, base_url):
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

        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажимаем кнопку "Подтвердить заказ"
        checkout_page.confirm_order()

        # Проверяе, что сообщения об ошибке для обязательных полей появились
        assert checkout_page.is_error_displayed_for_field("Населенный пункт"), "No error displayed for 'Населенный пункт'"
        assert checkout_page.is_error_displayed_for_field("Контактное лицо"), "No error displayed for 'Контактное лицо'"

        time.sleep(5)
