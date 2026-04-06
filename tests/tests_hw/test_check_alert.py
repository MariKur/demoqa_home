from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_check_alert(browser):
    page = BasePage(browser, "https://demoqa.com/alerts")
    page.visit()

    timer_alert_button = BaseComponent(browser, "#timerAlertButton")
    timer_alert_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert is not None
    alert.accept()
