from pages.base_page import BasePage
from components.components import WebElements
class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.accordian = WebElements(driver,'#section1Content > p')
        self.f_accordian = WebElements(driver, '#section1Heading')
