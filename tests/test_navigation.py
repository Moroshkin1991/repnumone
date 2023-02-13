import time
from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    testNavigation = Demoqa(browser)
    testNavigation2 = ElementsPage(browser)

    testNavigation.visit()
    testNavigation.btn_elements.click()
    # time.sleep(3)
    testNavigation2.refresh()
    #time.sleep(2)
    browser.refresh()
    browser.back()
    browser.forward()
    assert testNavigation2.equal_url()
