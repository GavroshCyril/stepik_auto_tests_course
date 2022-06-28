import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    btn_start = browser.find_element_by_class_name("trollface").click()
    # current_window = browser.current_window_handle
    # print(current_window)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)
    x = browser.find_element_by_id("input_value").text

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    submit1 = browser.find_element_by_class_name("btn-primary")
    submit1.click()
finally:
    time.sleep(2)
    browser.quit()
