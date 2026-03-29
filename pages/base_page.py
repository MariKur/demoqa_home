from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, base_url='https://www.saucedemo.com/'):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator: str):
        return self.driver.find_element(By.CSS_SELECTOR, locator)
