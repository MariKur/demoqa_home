from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_window_tab(browser):
    page = BasePage(browser, "https://demoqa.com/links")
    page.visit()

    home_link = BaseComponent(browser, "#simpleLink")

    assert home_link.get_text() == "Home"
    assert home_link.get_attribute("href") == "https://demoqa.com/"

    old_tabs = browser.window_handles
    home_link.click()
    new_tabs = browser.window_handles

    assert len(new_tabs) == len(old_tabs) + 1
