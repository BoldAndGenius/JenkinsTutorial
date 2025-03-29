from selenium.webdriver.support.select import Select

class Base:
    def __init__(self, driver):
        self.driver = driver

    def enter_text_to(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def click_on(self, locator):
        self.driver.find_element(*locator).click()

    def clear_text_from(self, locator):
        self.driver.find_element(*locator).clear()

    def get_text_from(self, locator):
        return self.driver.find_element(*locator).text

    def select_option_with_text(self, locator, text):
        select_element = self.driver.find_element(*locator)
        select_obj = Select(select_element)
        select_obj.select_by_visible_text(text)

    def check_displayed(self, locator):
        self.driver.find_element(*locator).is_displayed()
