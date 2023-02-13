from pages.text_box_page import TextBoxPage


def text_dz_text_box(browser):
    text_box = TextBoxPage(browser)
    full_name = 'Andrey'
    current_address = 'Russia, Novokuznetsk city'

    text_box.visit()
    text_box.full_name.send_keys(full_name)
    text_box.current_address.send_keys(current_address)
    text_box.btn_sumit.click()
    assert text_box.output_border_name.get_text() == full_name
    assert text_box.output_border_permanent_address.get_text() == current_address


