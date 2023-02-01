import time
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    b = Demoqa(browser)
    c = ElementsPage(browser)
    b.visit()
    b.btn_elements.click()
    #time.sleep(3)
    #c.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert c.equal_url()

