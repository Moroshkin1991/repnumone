from pages.text_box_page import TextBoxPage
import time


def test_clear(browser):
    test_box_clear = TextBoxPage(browser)

    test_box_clear.visit()
    test_box_clear.full_name.send_keys('Andrey')
    time.sleep(2)
    test_box_clear.full_name.clear()
    time.sleep(2)
    assert test_box_clear.full_name.get_text() == ''

