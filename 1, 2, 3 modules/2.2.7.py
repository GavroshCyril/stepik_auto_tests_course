import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

with open('test1.txt', 'w') as file:
   file.write('test1 for mls 228')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, 'test1.txt')
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
element_firstname = browser.find_element_by_css_selector("[name='firstname']")
element_firstname.send_keys("slave")
element_lastname = browser.find_element_by_css_selector("[name='lastname']")
element_lastname.send_keys("yurch")
element_email = browser.find_element_by_css_selector("[name='email']")
element_email.send_keys("ya@ya.ru")
element_btn = browser.find_element_by_css_selector("[type='submit']").click()



