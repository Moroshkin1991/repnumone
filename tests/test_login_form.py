from pages.form_page import FormPage
import time


def test_login_form(browser):
    from_page = FormPage(browser)

    from_page.visit()
    assert not from_page.modal_dialog.exist()
    time.sleep(2)
    from_page.first_name.send_keys('tester')
    from_page.last_name.send_keys('testerovich')
    from_page.user_email.send_keys('test@ttt.ru')
    from_page.gender_radio_1.click_force()
    from_page.user_number.send_keys('9992223344')
    time.sleep(2)
    from_page.btn_submit.click_force()
    time.sleep(2)
    assert from_page.modal_dialog.exist()
    from_page.btn_close_modal.click_force()
