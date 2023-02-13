from selenium.webdriver.common.keys import Keys
import time
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.ru')
    form_page.gender_radio_1.send_keys(Keys.SPACE)
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies_sports.click_force()
    form_page.hobbies_music.click_force()
    form_page.current_addres.send_keys('Russia, Novokuznetsk city')
    time.sleep(2)
    form_page.user_email.send_keys(Keys.CONTROL + 'a')
    form_page.user_email.send_keys(Keys.DELETE)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
