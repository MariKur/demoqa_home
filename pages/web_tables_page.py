from pages.base_page import BasePage
from components.base_component import BaseComponent


class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, base_url="https://demoqa.com/webtables")

        self.add_button = BaseComponent(driver, "#addNewRecordButton")
        self.submit_button = BaseComponent(driver, "#submit")
        self.form = BaseComponent(driver, "#userForm")

        self.first_name = BaseComponent(driver, "#firstName")
        self.last_name = BaseComponent(driver, "#lastName")
        self.user_email = BaseComponent(driver, "#userEmail")
        self.age = BaseComponent(driver, "#age")
        self.salary = BaseComponent(driver, "#salary")
        self.department = BaseComponent(driver, "#department")

        self.rows = BaseComponent(driver, ".rt-tbody .rt-tr-group")
        self.page_info = BaseComponent(driver, ".-pageInfo")
        self.next_button = BaseComponent(driver, ".-next > button")
        self.prev_button = BaseComponent(driver, ".-previous > button")
        self.rows_select = BaseComponent(driver, "select[aria-label='rows per page']")

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: str,
        salary: str,
        department: str,
    ) -> None:
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.user_email.send_keys(email)
        self.age.send_keys(age)
        self.salary.send_keys(salary)
        self.department.send_keys(department)

    def add_new_record(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: str,
        salary: str,
        department: str,
    ) -> None:
        self.add_button.click()
        self.fill_form(first_name, last_name, email, age, salary, department)
        self.submit_button.click()

    def table_text(self) -> str:
        return self.rows.get_text()

    def is_form_open(self) -> bool:
        return self.form.is_visible()

    def edit_button(self, row_index: int) -> BaseComponent:
        return BaseComponent(self.driver, f"#edit-record-{row_index}")

    def delete_button(self, row_index: int) -> BaseComponent:
        return BaseComponent(self.driver, f"#delete-record-{row_index}")

    def search_input(self) -> BaseComponent:
        return BaseComponent(self.driver, "#searchBox")

    def find_row_text_by_search(self, value: str) -> str:
        search = self.search_input()
        search.clear()
        search.send_keys(value)
        return self.table_text()

    def set_rows_per_page(self, value: str) -> None:
        select = self.rows_select.find_element()
        from selenium.webdriver.support.ui import Select
        Select(select).select_by_value(value)

    def next_is_disabled(self) -> bool:
        return self.next_button.get_attribute("disabled") is not None

    def prev_is_disabled(self) -> bool:
        return self.prev_button.get_attribute("disabled") is not None
