from pages.base_page import BasePage
from components.components import WebElement


class AccordionPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.big_text = WebElement(driver, '#section1Content > p')
        self.btn_first_question = WebElement(driver, '#section1Heading')
        self.not_elem = WebElement(driver, 'p>p')

