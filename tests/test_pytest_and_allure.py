import pytest
import allure


@allure.title('Пропущенный тест')
@pytest.mark.skip(reason='Причина пропуска')
def test_skip():
    assert True


@allure.title('Тест с ошибкой')
@pytest.mark.xfail(condition=True, reason='Причина, по которой тестовая функция помечена как Xfail')
def test_xfail_1():
    assert False


@allure.title('Тест с ошибкой №2')
@pytest.mark.xfail(condition=True, reason='Причина, по которой тестовая функция помечена как Xfail')
def test_xfail_2():
    assert True


@allure.title('Пропущенный тест с условием')
@pytest.mark.skipif(condition='2+2 !=5')
def test_skipif_by_triggered_condition():
    pass


@allure.title('Тест с указанными параметрами')
@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) ==0
