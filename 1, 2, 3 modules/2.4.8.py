from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
book = browser.find_element_by_id("book").click()

x = browser.find_element_by_id("input_value").text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
submit1 = browser.find_element_by_id("solve")
submit1.click()