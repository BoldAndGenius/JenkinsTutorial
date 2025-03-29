from selenium.webdriver.chrome.webdriver import WebDriver
from PageObjects.loginpage import LoginPage


driver = WebDriver()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

def test_login_with_valid_creds():
    login = LoginPage(driver)
    login.click_on_login_link()
    login.enter_email("reddyvinuth27@gmail.com")
    login.enter_password("selenium")
    login.click_on_login_button()
    login.click_on_logout_link()

