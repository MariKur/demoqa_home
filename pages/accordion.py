from pages.base_page import BasePage
from components.base_component import BaseComponent


class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver, base_url='https://demoqa.com/accordian')

        self.section_1_content = BaseComponent(driver, '#section1Content > p')
        self.section_1_heading = BaseComponent(driver, '#section1Heading')

        self.section_2_content_p1 = BaseComponent(driver, '#section2Content > p:nth-child(1)')
        self.section_2_content_p2 = BaseComponent(driver, '#section2Content > p:nth-child(2)')
        self.section_3_content = BaseComponent(driver, '#section3Content > p')
