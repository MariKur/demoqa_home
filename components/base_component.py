class BaseComponent:
    def __init__(self, driver, locator: str):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element("css selector", self.locator)

    def get_text(self) -> str:
        return str(self.find_element().text)
