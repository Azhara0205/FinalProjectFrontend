from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
    checkout_header_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/div[1]/div")
    contact_phone_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/form/div[1]/div[1]/div/input")
    city_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/form/div[1]/div[2]/div[2]/div[1]/input")
    comment_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/form/div[1]/div[6]/div/textarea")
    contact_person_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/form/div[1]/div[8]/div[2]/div[1]/input")
    email_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/form/div[1]/div[8]/div[2]/div[2]/input")
    confirm_order_button_locator = (By.XPATH, "/html/body/div[1]/main/div/div/div/div/form/button")

    city_error_locator = (By.XPATH, '//*[@id="delivery_address"]/div[2]/div[1]/div')
    contact_person_error_locator = (By.XPATH, '//*[@id="tabs-person"]/div[1]/div')


    def is_checkout_page_opened(self):
        header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.checkout_header_locator)
        )
        return header.is_displayed()

    def enter_contact_phone(self, phone):
        self.driver.find_element(*self.contact_phone_locator).send_keys(phone)

    def enter_city(self, city):
        self.driver.find_element(*self.city_locator).send_keys(city)

    def enter_comment(self, comment):
        self.driver.find_element(*self.comment_locator).send_keys(comment)

    def enter_contact_person(self, contact_person):
        self.driver.find_element(*self.contact_person_locator).send_keys(contact_person)

    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def confirm_order(self):
        self.driver.find_element(*self.confirm_order_button_locator).click()

    def is_city_error_displayed(self):
        return self._is_error_displayed(self.city_error_locator)

    def is_contact_person_error_displayed(self):
        return self._is_error_displayed(self.contact_person_error_locator)

    def is_contact_phone_error_displayed(self):
        return self._is_error_displayed(self.contact_phone_error_locator)

    def _is_error_displayed(self, locator):
        try:
            error_message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
            return error_message.is_displayed()
        except TimeoutException:
            return False

    def is_error_displayed_for_field(self, field_name):
        # Проверяет, отображается ли ошибка для обязательного поля
        if field_name == "Населенный пункт":
            return self.is_city_error_displayed()
        elif field_name == "Контактное лицо":
            return self.is_contact_person_error_displayed()
        elif field_name == "Контактный телефон":
            return self.is_contact_phone_error_displayed()
        else:
            raise ValueError(f"Unknown field: {field_name}")
