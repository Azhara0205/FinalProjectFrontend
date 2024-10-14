from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.cart_button_locator = (By.XPATH, "/html/body/div[2]/header/div/div/div[1]/div/div[3]/a[1]/span")
        self.remove_button_locator = (By.XPATH, "/html/body/div[2]/main/div[2]/div/form/div[1]/div/div[5]/button")
        self.empty_cart_message_locator = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div")
        self.increment_quantity_button_locator = "/html/body/div[2]/main/div[2]/div/form/div[1]/div/div[3]/div/button[2]"
        self.add_to_cart_button_locator = "/html/body/div[2]/main/div[3]/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[4]/div/div[2]/div/button"
        self.checkout_button_locator = (By.XPATH, '/html/body/div[2]/main/div[2]/div/form/div[2]/div/div[2]/button')


    def open_cart(self):
        # Открывает корзину, нажав на кнопку открытия корзины
        self.driver.find_element(*self.cart_button_locator).click()

    def add_product_to_cart(self, product_id, quantity=1):
        # Добавляет товар в корзину и задает количество
        add_to_cart_button_locator = self.add_to_cart_button_locator.format(product_id)

        try:
            add_button = self.driver.find_element(By.XPATH, add_to_cart_button_locator)
            add_button.click()

            if quantity > 1:
                increment_button_locator = self.increment_quantity_button_locator.format(product_id)
                for _ in range(quantity - 1):
                    increment_button = self.driver.find_element(By.XPATH, increment_button_locator)
                    increment_button.click()

            print(f"Товар с ID {product_id} добавлен в корзину с количеством {quantity}.")
        except NoSuchElementException:
            print(f"Продукт с ID {product_id} или его элементы не найдены.")

    def remove_product(self, product_id):
        # Удаляет продукт
        try:
            remove_button = self.driver.find_element(By.XPATH, f"//form[@data-product-id='{product_id}']//button")
            remove_button.click()
        except NoSuchElementException:
            print(f"Кнопка удаления для товара с ID {product_id} не найдена.")

    def is_product_added_to_cart(self, product_id):
        # Проверяет, добавлен ли продукт в корзину
        product_locator = f"//form[@data-product-id='{product_id}']"
        try:
            self.driver.find_element(By.XPATH, product_locator)
            return True
        except NoSuchElementException:
            return False

    def get_product_quantity(self):
        # Получает количество товара
        quantity_input_locator = "/html/body/div[2]/main/div[2]/div/form/div[1]/div/div[3]/div/input"
        try:
            quantity_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, quantity_input_locator)))
            return quantity_input.get_attribute("value")  # Возвращаем значение как строку
        except NoSuchElementException:
            print("Не удалось найти поле количества товара.")
            return None
        except TimeoutException:
            print("Время ожидания истекло для поля количества товара.")
            return None

    def is_cart_empty(self):
         # Проверяет, пуста ли корзина
        try:
            self.driver.find_element(*self.empty_cart_message_locator)
            return True
        except NoSuchElementException:
            return False

    def click_checkout_button(self):
        # Нажимает на кнопку 'Оформить заказ
        try:
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.checkout_button_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", checkout_button)
            checkout_button.click()
            print("Кнопка 'Оформить заказ' успешно нажата.")
        except TimeoutException:
            print("Кнопка 'Оформить заказ' не была найдена или недоступна для нажатия.")

