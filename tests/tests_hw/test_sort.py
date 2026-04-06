from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_sort(browser):
    page = BasePage(browser, "https://demoqa.com/webtables")
    page.visit()

    headers = [
        BaseComponent(browser, ".rt-th.-cursor-pointer:nth-child(1)"),  # First Name
        BaseComponent(browser, ".rt-th.-cursor-pointer:nth-child(2)"),  # Last Name
        BaseComponent(browser, ".rt-th.-cursor-pointer:nth-child(3)"),  # Age
        BaseComponent(browser, ".rt-th.-cursor-pointer:nth-child(4)"),  # Email
        BaseComponent(browser, ".rt-th.-cursor-pointer:nth-child(5)"),  # Salary
        BaseComponent(browser, ".rt-th.-cursor-pointer:nth-child(6)"),  # Department
    ]

    for header in headers:
        header.click()
        assert "-sort-asc" in header.get_attribute("class") or "-sort-desc" in header.get_attribute("class")
