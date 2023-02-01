from pages.demoqa import Demoqa


def test_icon_exist(browser):
    a = Demoqa(browser)
    a.visit()
    a.icon.click()
    assert a.equal_url()
    assert a.icon.exist()
