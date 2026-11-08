
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DemoRegistrationPage:
    REGISTER_LINK = (By.CSS_SELECTOR, "a.ico-register")
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    RESULT_MESSAGE = (By.CSS_SELECTOR, "div.result")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTER_LINK).click()

    def _fill(self, locator, value):
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(value)

    def fill_first_name(self, value):
        self._fill(self.FIRST_NAME_INPUT, value)

    def fill_last_name(self, value):
        self._fill(self.LAST_NAME_INPUT, value)

    def fill_email(self, value):
        self._fill(self.EMAIL_INPUT, value)

    def fill_password(self, value):
        self._fill(self.PASSWORD_INPUT, value)

    def fill_confirm_password(self, value):
        self._fill(self.CONFIRM_PASSWORD_INPUT, value)

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def get_result_text(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    self.RESULT_MESSAGE
                )
            ).text
        except TimeoutException:
            return ""
