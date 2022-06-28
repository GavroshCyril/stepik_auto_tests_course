from selenium import webdriver
# import unittest


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
    browser.find_element_by_css_selector(".second:required").send_keys("Petrov")
    browser.find_element_by_css_selector(".third:required").send_keys("url@gmail")
    browser.find_element_by_css_selector("button.btn").click()

    return browser.find_element_by_tag_name("h1").text


class TestReg:
    def test_reg1(self):
        assert (fill_form("http://suninjuly.github.io/registration1.html"),
                         "Congratulations!", "registration is failed")

    def test_reg2(self):
        assert (fill_form("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

