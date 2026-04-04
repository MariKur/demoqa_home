from pages.base_page import BasePage
from components.base_component import BaseComponent


# 2. Проверка текста в подвале
def test_footer_text(driver):
    page = BasePage(driver, base_url="https://demoqa.com/")
    page.visit()

    footer = BaseComponent(driver, "footer")
    text = footer.get_text()

    assert text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


# 3. Проверка текста на странице Elements
def test_elements_page_text(driver):
    page = BasePage(driver, base_url="https://demoqa.com/")
    page.visit()

    # клик по кнопке "Elements"
    elements_button = BaseComponent(driver, "div.card.mt-4.top-card:nth-child(1)")
    elements_button.find_element().click()

    # текст по центру
    center_text = BaseComponent(driver, "div.col-12.mt-4.col-md-6")
    text = center_text.get_text()

    assert text == "Please select an item from left to start practice."
