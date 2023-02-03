from pages.modal_dialogs_page import ModalDialogsPage
from pages.alerts_page import AlertsPage


def test_elements_dz(browser):
    modal_dialogs = ModalDialogsPage(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btns_third_menu.check_count_elements(5)


def test_navigation_dz(browser):
    modal_dialogs = ModalDialogsPage(browser)
    alerts_page = AlertsPage(browser)

    modal_dialogs.visit()
    modal_dialogs.btns_alerts_third_menu.click()
    browser.back()
    browser.set_window_size(900, 900)
    browser.forward()
    assert alerts_page.equal_url()
    browser.set_window_size(1000, 1000)
