import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    btn_start = browser.find_element_by_css_selector("[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)
    x = browser.find_element_by_id("input_value").text

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    submit1 = browser.find_element_by_class_name("btn-primary")
    submit1.click()
finally:
    time.sleep(2)
    browser.quit()
