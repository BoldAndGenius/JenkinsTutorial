from PageObjects.registerpage import (RegisterPage)
from selenium.webdriver.chrome.webdriver import WebDriver


driver = WebDriver()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

def test_register_with_valid_info():
    register = RegisterPage(driver)
    register.click_on_register_link()
    register.click_on_male_radio_button()
    register.enter_firstname("hello")
    register.enter_lastname("world")
    register.enter_email("a123@321.com")
    register.enter_password("1234@1234")
    register.enter_confirm_password("1234@1234")
    register.click_on_register_button()
    register.click_on_logout_link()