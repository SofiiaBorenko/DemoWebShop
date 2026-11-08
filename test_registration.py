

import time

import pytest
from selenium import webdriver
from demo_registration_page import DemoRegistrationPage


PASSWORD = "test123456"


def unique_email():
    return f"sofiia_{int(time.time())}@example.com"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")

    yield driver
    driver.quit()


def test_successful_registration(driver):
    page = DemoRegistrationPage(driver)

    page.open_registration_page()
    page.fill_first_name("Sofiia")
    page.fill_last_name("Borenko")
    page.fill_email(unique_email())
    page.fill_password(PASSWORD)
    page.fill_confirm_password(PASSWORD)

    page.click_register_button()

    result = page.get_result_text()

    print(repr(result))

    assert "registration completed" in result.lower()
