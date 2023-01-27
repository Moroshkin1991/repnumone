from pages.elements_page import ElementsPage
from pages.demoqa import Demoqa
import time


def test_visible_btn_sidebar(browser):
    visible_btn = ElementsPage(browser)
    visible_btn.visit()
    visible_btn.btn_sidebar_first.click()
    time.sleep(3)
    assert visible_btn.btn_sidebar_first.visible()
