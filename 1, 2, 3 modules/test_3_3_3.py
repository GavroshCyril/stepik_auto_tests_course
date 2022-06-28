from selenium import webdriver
import time


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_tag_name('div.first_block>div.form-group.first_class>input')
    first.send_keys('name')
    second = browser.find_element_by_tag_name('div.first_block>div.form-group.second_class>input')
    second.send_keys('family')
    third = browser.find_element_by_tag_name('div.first_block>div.form-group.third_class>input')
    third.send_keys('mail@mail.ru')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


class TestReg:
    def test_reg1(self):
        assert(link_t("http://suninjuly.github.io/registration1.html"),
                         "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

    def test_reg2(self):
        assert(link_t("http://suninjuly.github.io/registration2.html"),
                         "Поздравляем! Вы успешно зарегистировались!", "registration is failed")
