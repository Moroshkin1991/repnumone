from pages.elements_page import ElementsPage
from pages.demoqa import Demoqa
from pages.accordion_page import AccordionPage
import time


def test_visible_btn_sidebar(browser):
    visible_btn = ElementsPage(browser)
    visible_btn.visit()
    visible_btn.btn_sidebar_first.click()
    time.sleep(3)
    assert visible_btn.btn_sidebar_first.visible()


def test_not_visible_btn_sidebar(browser):
    not_visible_btn = ElementsPage(browser)
    not_visible_btn.visit()
    assert not_visible_btn.btn_sidebar_first_checkbox.visible()
    not_visible_btn.btn_sidebar_first.click()
    time.sleep(2)
    assert not_visible_btn.btn_sidebar_first_checkbox.not_visible()


def test_visible_accordian(browser):
    visible_acc = AccordionPage(browser)
    visible_acc.visit()
    assert visible_acc.big_text.visible()
    visible_acc.btn_first_question.click()
    time.sleep(2)
    assert visible_acc.big_text.not_visible()


def test_visible_default_accordion(browser):
    a = AccordionPage(browser)
    a.visit()
    assert a.big_text.visible()
    a.btn_first_question.click()
    browser.set_window_size(1000,300)
    time.sleep(3)
    assert a.big_text.not_visible()
    browser.refresh()
    browser.set_window_size(1000,1000)
    assert a.big_text.visible()
