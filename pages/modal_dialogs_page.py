from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.btns_alerts_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > #item-1')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')
