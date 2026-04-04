from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    page = ModalDialogs(browser)
    page.visit()

    assert page.submenu_buttons.count_elements() == 5


def test_navigation_modal(browser):
    page = ModalDialogs(browser)
    page.visit()

    # обновить страницу
    page.refresh_page()

    # перейти на главную через иконку
    page.home_icon.click()

    # шаг назад
    page.back()

    # установить размеры окна
    page.set_window_size(900, 400)

    # шаг вперед
    page.forward()

    # проверка url главной страницы
    assert page.get_current_url() == 'https://demoqa.com/'

    # проверка title главной страницы
    assert page.get_title() == 'DEMOQA'

    # вернуть размеры по умолчанию
    page.set_window_size(1000, 1000)
