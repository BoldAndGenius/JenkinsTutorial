from selenium.webdriver.chrome.webdriver import WebDriver

from PageObjects.homepage import HomePage
from PageObjects.loginpage import LoginPage
from PageObjects.searchpage import SearchPage


driver = WebDriver()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

def test_search_for_product():
    home = HomePage(driver)
    login = LoginPage(driver)
    search = SearchPage(driver)
    home.enter_email_to_newsletter("reddyvinuth27@gmail.com")
    home.click_on_subscribe_button()
    home.click_on_login_link()
    login.enter_email("reddyvinuth27@gmail.com")
    login.enter_password("selenium")
    home.search_for("computer")
    search.check_search_for("computer")
    search.click_on_logout_link()
