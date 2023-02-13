import time
from pages.text_box_page import TextBoxPage
from components.components import WebElement
import allure


@allure.feature('check attr')
@allure.story('Проверка значения атрибута элемента')
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    '''Проверка значения атрибута элемента'''

    test_box_page = TextBoxPage(browser)

    test_box_page.visit()
    assert test_box_page.full_name.exist()
    assert test_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'

@allure.feature('check attr')
@allure.story('Проверка наличия атрибута')
@allure.severity(allure.severity_level.CRITICAL)
def test_attr_exist(browser):
    '''Проверка наличия атрибута'''

    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    text_box_page.btn_first.click()
    assert text_box_page.box_first_menu.get_dom_attribute('style')

@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.NORMAL)
def test_attr_not_exist(browser):
    '''Проверка отсутствия атрибута'''

    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert not text_box_page.btn_first.get_dom_attribute('style')
