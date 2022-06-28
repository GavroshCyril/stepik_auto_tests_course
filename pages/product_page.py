from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_in_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message_name_book(self):
        assert self.browser.find_element(*ProductPageLocators.ALARM_BOOK_NAME).text == \
            self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, "В корзину попала не та книга"

    def should_be_message_price_book(self):
        assert self.browser.find_element(*ProductPageLocators.ALARM_PRICE).text == \
            self.browser.find_element(*ProductPageLocators.PRICE).text, "Цена товара не совпадает с суммой корзины"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
