import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"
#
browser = webdriver.Chrome()
browser.get(link)

try:
    check_img = browser.find_element_by_id("input_value")
    x = check_img.get_attribute("valuex")

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    print(y)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element_by_id("robotsRule").click()
    submit = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:

    time.sleep(10)
    browser.quit()