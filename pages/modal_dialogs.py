from pages.base_page import BasePage
from components.base_component import BaseComponent


class ModalDialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver, base_url='https://demoqa.com/modal-dialogs')

        # кнопки подменю слева
        self.submenu_buttons = BaseComponent(driver, 'li.btn.btn-light')

        # иконка Home
        self.home_icon = BaseComponent(driver, 'header a')

    def refresh_page(self) -> None:
        self.driver.refresh()

    def back(self) -> None:
        self.driver.back()

    def forward(self) -> None:
        self.driver.forward()

    def set_window_size(self, width: int, height: int) -> None:
        self.driver.set_window_size(width, height)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title
