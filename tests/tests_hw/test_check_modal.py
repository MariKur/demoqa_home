import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from components.base_component import BaseComponent


def is_page_available(url: str) -> bool:
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False


@pytest.mark.skipif(
    not is_page_available("https://demoqa.com/modal-dialogs"),
    reason="Страница modal-dialogs недоступна",
)
def test_check_modal(browser):
    page = BasePage(browser, "https://demoqa.com/modal-dialogs")
    page.visit()

    small_modal_button = BaseComponent(browser, "#showSmallModal")
    large_modal_button = BaseComponent(browser, "#showLargeModal")
    modal_window = BaseComponent(browser, ".modal-content")
    close_small_button = BaseComponent(browser, "#closeSmallModal")
    close_large_button = BaseComponent(browser, "#closeLargeModal")

    assert small_modal_button.get_text() == "Small modal"
    assert large_modal_button.get_text() == "Large modal"

    # Small modal
    small_modal_button.click()
    assert modal_window.is_visible()
    close_small_button.click()
    WebDriverWait(browser, 5).until(lambda d: not modal_window.is_visible())

    # Large modal
    large_modal_button.click()
    assert modal_window.is_visible()
    close_large_button.click()
    WebDriverWait(browser, 5).until(lambda d: not modal_window.is_visible())
