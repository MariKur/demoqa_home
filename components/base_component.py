from selenium.webdriver.common.by import By


class BaseComponent:
    def __init__(self, driver, locator: str):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def click(self) -> None:
        self.find_element().click()

    def get_text(self) -> str:
        return str(self.find_element().text)

    def is_visible(self) -> bool:
        try:
            return self.find_element().is_displayed()
        except:
            return False
