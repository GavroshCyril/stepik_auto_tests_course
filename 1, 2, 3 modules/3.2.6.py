# assert abs(-42) == 42, "sos"
# assert self.is_element_present('create_class_button', timeout=30), "No create class button"
# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# print(f"{2+3}")

catalog_text = self.catalog_link.text  # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    print(f"Wrong language, got {catalog_text} instead of 'Каталог'")

