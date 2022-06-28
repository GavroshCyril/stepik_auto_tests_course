import math
from selenium import webdriver
import time

link = "https://suninjuly.github.io/execute_script.html"
#
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.execute_script("window.scrollBy(0, 200);")
    x = browser.find_element_by_id("input_value").text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio1box = browser.find_element_by_id("robotsRule").click()
    submit1 = browser.find_element_by_class_name("btn-primary")
    submit1.click()

finally:
    time.sleep(6)
    browser.quit()
