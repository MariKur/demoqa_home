import time
from pages.web_tables_page import WebTablesPage


def test_webtables_crud(browser):
    page = WebTablesPage(browser)
    page.visit()

    # a-b. открыть форму
    page.add_button.click()
    assert page.is_form_open()

    # c. пустую форму нельзя сохранить
    page.submit_button.click()
    assert page.is_form_open()
    assert "was-validated" in page.form.get_attribute("class")

    # d. заполнить все поля и сохранить
    first_name = "Ivan"
    last_name = "Petrov"
    email = "ivan.petrov@example.com"
    age = "30"
    salary = "5000"
    department = "QA"

    page.fill_form(first_name, last_name, email, age, salary, department)
    page.submit_button.click()

    # d.i диалог закрылся
    assert not page.is_form_open()

    # d.ii в таблице есть новая запись
    row_text = page.find_row_text_by_search(email)
    assert first_name in row_text
    assert last_name in row_text
    assert email in row_text
    assert age in row_text
    assert salary in row_text
    assert department in row_text

    # e. клик по карандашу
    page.edit_button(4).click()
    assert page.is_form_open()

    # e.i диалог открылся с введенными данными
    assert page.first_name.get_attribute("value") == first_name
    assert page.last_name.get_attribute("value") == last_name
    assert page.user_email.get_attribute("value") == email
    assert page.age.get_attribute("value") == age
    assert page.salary.get_attribute("value") == salary
    assert page.department.get_attribute("value") == department

    # f. изменить имя и сохранить
    new_first_name = "Petr"
    page.first_name.clear()
    page.first_name.send_keys(new_first_name)
    page.submit_button.click()

    row_text = page.find_row_text_by_search(email)
    assert new_first_name in row_text
    assert first_name not in row_text

    # g. удалить запись
    page.delete_button(4).click()
    row_text = page.find_row_text_by_search(email)
    assert email not in row_text
