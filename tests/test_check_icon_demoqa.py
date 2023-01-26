from pages.demoqa import Demoqa


def test_icon_exist(browser):
    a = Demoqa(browser)
    a.visit()
    a.icon.click()
    assert a.exist_icon()
    assert a.equal_url()

#     browser.get('https://demoqa.com/')
#     icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
#
#     if icon is None:
#         print("Элемент не найден")
#     else:
#         print("Элемент найден")
