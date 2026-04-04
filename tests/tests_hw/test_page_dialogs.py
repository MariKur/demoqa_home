from pages.modal_dialogs import ModalDialogs


# 1. Проверка количества кнопок
def test_modal_elements(browser):
    page = ModalDialogs(browser)
    page.visit()

    # проверка, что кнопок подменю 5
    assert page.submenu_buttons.count_elements() == 5


# 2. Проверка навигации
def test_navigation_modal(browser):
    page = ModalDialogs(browser)
    page.visit()

    # обновить страницу
    page.refresh_page()

    # перейти на главную через иконку
    page.home_icon.click()

    # шаг назад
    page.back()

    # установить размер окна
    page.set_window_size(900, 400)

    # шаг вперед
    page.forward()

    # проверка URL главной страницы
    assert page.get_current_url() == "https://demoqa.com/"

    # проверка title
    assert page.get_title() == "DEMOQA"

    # вернуть размер окна
    page.set_window_size(1000, 1000)
