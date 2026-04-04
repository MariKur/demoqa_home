from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_login_form_validate(browser):
    page = BasePage(browser, "https://demoqa.com/automation-practice-form")
    page.visit()

    first_name = BaseComponent(browser, "#firstName")
    last_name = BaseComponent(browser, "#lastName")
    user_email = BaseComponent(browser, "#userEmail")
    form = BaseComponent(browser, "form")
    submit_button = BaseComponent(browser, "#submit")

    assert first_name.find_element().get_attribute("placeholder") == "First Name"
    assert last_name.find_element().get_attribute("placeholder") == "Last Name"
    assert user_email.find_element().get_attribute("placeholder") == "name@example.com"
    assert user_email.find_element().get_attribute("pattern") == r"^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$"

    submit_button.click()

    assert "was-validated" in form.find_element().get_attribute("class")
from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_fill_state_and_city(browser):
    page = BasePage(browser, "https://demoqa.com/automation-practice-form")
    page.visit()

    state = BaseComponent(browser, "#state")
    city = BaseComponent(browser, "#city")

    state.click()
    browser.find_element("css selector", "#react-select-3-option-0").click()

    city.click()
    browser.find_element("css selector", "#react-select-4-option-0").click()

    assert "NCR" in state.get_text()
    assert "Delhi" in city.get_text()
