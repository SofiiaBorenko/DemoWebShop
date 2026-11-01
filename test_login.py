
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://demowebshop.tricentis.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "Email"))
        )

        password_field = self.driver.find_element(
            By.ID, "Password"
        )

        email_field.send_keys(email.strip())
        password_field.send_keys(password)

        self.driver.find_element(
            By.CSS_SELECTOR, "input.login-button"
        ).click()

        logout_link = self.wait.until(
            EC.visibility_of_element_located(
                (By.LINK_TEXT, "Log out")
            )
        )

        assert logout_link.is_displayed(), "Login failed!"

        print("Login successful!")

    def test_unsuccessful_login(self):
        email = input("Enter your email: ")
        wrong_password = "WrongPassword123!"

        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "Email"))
        )

        password_field = self.driver.find_element(
            By.ID, "Password"
        )

        email_field.send_keys(email.strip())
        password_field.send_keys(wrong_password)

        self.driver.find_element(
            By.CSS_SELECTOR, "input.login-button"
        ).click()

        error_message = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".validation-summary-errors")
            )
        )

        assert error_message.is_displayed(), \
            "Expected login error was not displayed!"

        print("Unsuccessful login test passed!")


if __name__ == "__main__":
    test = TestLogin()

    test.setUp()
    try:
        test.test_successful_login()
    finally:
        test.tearDown()

    test = TestLogin()

    test.setUp()
    try:
        test.test_unsuccessful_login()
    finally:
        test.tearDown()
