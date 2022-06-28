from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

elems = browser.find_elements_by_css_selector('input[type="text"]')
for element in elems:
        element.send_keys("loxloxlox")
print(len(elems))