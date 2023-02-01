from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage
import time


def test_go_to_page_elements(browser):
    b = Demoqa(browser)
    c = ElementsPage(browser)

    b.visit()
    assert b.equal_url()
    b.btn_elements.click()
    assert c.equal_url()
