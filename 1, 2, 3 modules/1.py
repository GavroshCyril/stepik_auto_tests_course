import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium import webdriver
from selenium.webdriver import Chrome
@pytest.fixture
def browser():
# Инициализация ChromeDriver
driver = Chrome()
# Неявное ожидание готовности элементов перед попыткой взаимодействия
driver.implicitly_wait(10)
# Возвращение объекта драйвера в конце настройки
yield driver
# Для очистки покиньте драйвер
driver.quit()
def test_basic_duckduckgo_search(browser):
# Настройте данные для тест-кейса
PHRASE = 'panda'
# Поиск фразы
search_page = DuckDuckGoSearchPage(browser)
search_page.load()
search_page.search(PHRASE)
# Проверка, что результаты появились
result_page = DuckDuckGoResultPage(browser)
assert result_page.link_div_count() > 0
assert result_page.phrase_result_count(PHRASE) > 0
assert result_page.search_input_value() == PHRASE