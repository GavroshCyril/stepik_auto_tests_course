from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math
import pytest


@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1"
    browser.get(link)
    price = WebDriverWait(browser, 5)
    price.until(
        ec.text_to_be_present_in_element((By.CLASS_NAME, "submit-submission"), "Отправить"))

    def calc():
        return math.log(int(time.time()))
    y = calc()
    print(y)
    find_area = browser.find_element_by_css_selector("textarea[placeholder='Напишите ваш ответ здесь...']")
    find_area.send_keys(str(math.log(int(time.time()))))
    press_button = browser.find_element_by_css_selector("button[class='submit-submission']")
    press_button.click()
    find_cor = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    print(find_cor)
    if find_cor != 'Correct!':
        with open('string.txt', 'a') as outfile:
            outfile.write(find_cor)
