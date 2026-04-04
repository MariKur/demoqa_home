from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_text_box(browser):
    page = BasePage(browser, "https://demoqa.com/text-box")
    page.visit()

    full_name_value = "Ivan Ivanov"
    current_address_value = "Moscow, Red Square, 1"

    full_name = BaseComponent(browser, "#userName")
    current_address = BaseComponent(browser, "#currentAddress")
    submit_button = BaseComponent(browser, "#submit")

    output_name = BaseComponent(browser, "#output #name")
    output_address = BaseComponent(browser, "#output #currentAddress")

    full_name.find_element().send_keys(full_name_value)
    current_address.find_element().send_keys(current_address_value)
    submit_button.click()

    assert output_name.get_text() == f"Name:{full_name_value}"
    assert output_address.get_text() == f"Current Address :{current_address_value}"
