import pytest
import requests
from selenium.common.exceptions import TimeoutException
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
    reason="Страница https://demoqa.com/modal-dialogs недоступна"
)
def test_check_modal(browser):
    page = BasePage(browser, "https://demoqa.com/modal-dialogs")
    page.visit()

    small_modal_button = BaseComponent(browser, "#showSmallModal")
    large_modal_button = BaseComponent(browser, "#showLargeModal")

    small_modal = BaseComponent(browser, ".modal-content")
    close_small_button = BaseComponent(browser, "#closeSmallModal")

    close_large_button = BaseComponent(browser, "#closeLargeModal")

    # Small modal
    assert small_modal_button.get_text() == "Small modal"
    small_modal_button.click()
    assert small_modal.is_visible()
    close_small_button.click()

    try:
        WebDriverWait(browser, 5).until(lambda d: not small_modal.is_visible())
    except TimeoutException:
        assert False, "Small modal не закрылось"

    # Large modal
    assert large_modal_button.get_text() == "Large modal"
    large_modal_button.click()
    assert small_modal.is_visible()
    close_large_button.click()

    try:
        WebDriverWait(browser, 5).until(lambda d: not small_modal.is_visible())
    except TimeoutException:
        assert False, "Large modal не закрылось"
