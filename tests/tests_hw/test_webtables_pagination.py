from pages.web_tables_page import WebTablesPage


def test_webtables_pagination(browser):
    page = WebTablesPage(browser)
    page.visit()

    # предусловие: 5 строк на странице
    page.set_rows_per_page("5")

    # i. Next и Previous заблокированы
    assert page.next_is_disabled()
    assert page.prev_is_disabled()

    # ii. добавить еще 3 записи
    data = [
        ("Test1", "User1", "test1@example.com", "21", "1000", "QA"),
        ("Test2", "User2", "test2@example.com", "22", "2000", "Dev"),
        ("Test3", "User3", "test3@example.com", "23", "3000", "AQA"),
    ]

    for row in data:
        page.add_new_record(*row)

    # появляется 2-я страница
    assert "of 2" in page.page_info.get_text()

    # кнопка Next доступна
    assert not page.next_is_disabled()

    # iii. перейти на 2 страницу
    page.next_button.click()
    assert page.page_info.find_element().get_attribute("value") == "2"

    # iv. вернуться на 1 страницу
    page.prev_button.click()
    assert page.page_info.find_element().get_attribute("value") == "1"
