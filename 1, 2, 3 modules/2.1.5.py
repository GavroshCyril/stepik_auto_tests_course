import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text


    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    checkbox = browser.find_element_by_class_name("form-check-input")
    checkbox.click()
    radiobox = browser.find_element_by_css_selector("[for=robotsRule]").click()
    submit = browser.find_element_by_css_selector("[type=submit]").click()

finally:

    time.sleep(10)
    browser.quit()
