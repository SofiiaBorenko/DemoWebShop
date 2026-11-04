
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


EMAIL = "borenkosofiia@gmail.com"
LOGIN_PAGE = "https://demowebshop.tricentis.com/login"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE)

    yield driver
    driver.quit()


def test_login_with_wrong_password(driver):
    email = driver.find_element(By.ID, "Email")
    password = driver.find_element(By.ID, "Password")

    email.send_keys(EMAIL)
    password.send_keys("WrongPassword123!")

    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".validation-summary-errors")
        )
    )

    assert error.is_displayed()
    assert "Login was unsuccessful" in error.text


def test_login_with_empty_password(driver):
    email = driver.find_element(By.ID, "Email")
    email.send_keys(EMAIL)
    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".validation-summary-errors")
        )
    )

    assert error.is_displayed()
    assert "Login was unsuccessful" in error.text



def test_login_with_wrong_email_format(driver):
    email = driver.find_element(By.ID, "Email")
    password = driver.find_element(By.ID, "Password")

    email.send_keys("student.example.com")
    password.send_keys("WrongPassword123!")

    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".validation-summary-errors, .field-validation-error")
        )
    )

    assert error.is_displayed()
    assert not driver.find_elements(By.LINK_TEXT, "Log out")

