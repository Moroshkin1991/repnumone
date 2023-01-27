from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_check_text_please(browser):
    demo_qa_page = Demoqa(browser)
    element_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert element_page.text_please.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    demo_text_elements = ElementsPage(browser)
    demo_text_elements.visit()
    assert demo_text_elements.text_elements.get_text() == 'Elements'
