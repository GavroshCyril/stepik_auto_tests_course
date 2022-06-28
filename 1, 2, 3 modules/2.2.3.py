import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
#
browser = webdriver.Chrome()
browser.get(link)

try:
    first_find = browser.find_element_by_id('num1').text
    second_find = browser.find_element_by_id('num2').text

    s = str(sum([int(first_find), int(second_find)]))

    print(s)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)  # ищем элемент с текстом "Python"

    # input = browser.find_element_by_id("answer")
    # input.send_keys(y)
    # checkbox = browser.find_element_by_id("robotCheckbox")
    # checkbox.click()
    # radiobox = browser.find_element_by_id("robotsRule").click()
    submit = browser.find_element_by_class_name("btn-default").click()

finally:

    time.sleep(5)
    browser.quit()