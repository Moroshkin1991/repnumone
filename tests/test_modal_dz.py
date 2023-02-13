from pages.modal_dialogs_page import ModalDialogsPage
from selenium import webdriver
import allure
import pytest
import time


def param():
    browser = webdriver.Chrome()
    modal_page = ModalDialogsPage(browser)
    modal_page.visit()
    time.sleep(2)
    return not modal_page.equal_url()


@allure.feature('Проверка доступа страницы')
@allure.title('Страница доступна')
@pytest.mark.skipif(condition=(param() == True), reason='Условия выполнились')
def test_modal(browser):
    test_modal = ModalDialogsPage(browser)

    test_modal.visit()
    time.sleep(1)
    test_modal.btn_large_modal.click()
    time.sleep(1)
    test_modal.btn_close_large_modal.click()
    time.sleep(1)
    test_modal.btn_small_modal.click()
    time.sleep(1)
    test_modal.btn_close_small_modal.click()
    time.sleep(1)


@allure.feature('Проверка доступа страницы')
@allure.title('Страница недоступна')
@pytest.mark.skipif(condition=(param() == False), reason='Условия не выполнились')
def test_modal2(browser):
    test_modal2 = ModalDialogsPage(browser)

    test_modal2.visit()
    time.sleep(1)
    test_modal2.btn_large_modal.click()
    time.sleep(1)
    test_modal2.btn_close_large_modal.click()
    time.sleep(1)
    test_modal2.btn_small_modal.click()
    time.sleep(1)
    test_modal2.btn_close_small_modal.click()
    time.sleep(1)
