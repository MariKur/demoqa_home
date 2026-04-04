import time
from pages.accordion import Accordion


def test_visible_accordion(browser):
    page = Accordion(browser)
    page.visit()

    # элемент виден
    assert page.section_1_content.is_visible()

    # клик по заголовку
    page.section_1_heading.click()
    time.sleep(2)

    # элемент не виден
    assert not page.section_1_content.is_visible()


def test_visible_accordion_default(browser):
    page = Accordion(browser)
    page.visit()

    # по умолчанию скрыты
    assert not page.section_2_content_p1.is_visible()
    assert not page.section_2_content_p2.is_visible()
    assert not page.section_3_content.is_visible()
