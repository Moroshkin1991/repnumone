from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def equal_url(self):
        if self.base_url == self.get_url():
            return True
        else:
            return False
