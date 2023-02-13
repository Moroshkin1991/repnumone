from pages.base_page import BasePage
from components.components import WebElement


class TextBoxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '//*[@id="userName"]', 'xpath')
        self.current_address = WebElement(driver, '#currentAddress')
        self.box_first_menu = WebElement(driver, "div.row > div:nth-child(1) > div > div > div:nth-child(1) > div")
        self.btn_first = WebElement(driver, "div > div > div:nth-child(1) > span")
        self.btn_sumit = WebElement(driver, '#submit')
        self.output_border_name = WebElement(driver, '#name')
        self.output_border_permanent_address = WebElement(driver, '.border #permanentAddress')
