from pages.swag_labs import SwagLabs


def test_check_icon(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_icon() is True


def test_check_username(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_username() is True


def test_check_password(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_password() is True
