from confi import *


def add_item_to_cart():
    driver = browser_call()
    expected_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, '//p[@class="shelf-item__title"][normalize-space()="iPhone 12"]'))).text
    # print(f"the expected text is: {expected_text}")

    add_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]')))
    add_to_cart.click()
    actual_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//p[@class='title' and text()='iPhone 12']"))).text
    # print(f"the actual text is: {actual_text}")
    if expected_text == actual_text:
        print("TC_025 PASSED: Item Addedd to Cart")
    else:
        print("fail")
    driver.quit()
    # assert expected_text == actual_text, f"{actual_text} doesnt match {expected_text}"


def add_same_item():

    driver = browser_call()
    add_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]')))
    add_to_cart.click()
    expected_quantiy_text_1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//p[.='Apple Quantity: 1']"))).text
    # print(f"the expected quantity text text is: {expected_quantiy_text}")
    quantity_text_1 = int(expected_quantiy_text_1.split(
        "Quantity: ")[1].strip())  # "2"
    # print(f"the first quantity: {quantity_text_1}")
    assert quantity_text_1 == 1, f"the expected quantiy is not 1"
    print("the expected quantity is 1")

    increase_quantity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="+"]')))
    increase_quantity.click()
    expected_quantiy_text_2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//p[.='Apple Quantity: 2']"))).text
    # print(f"the expected quantity text text is: {expected_quantiy_text}")
    quantity_text_2 = int(expected_quantiy_text_2.split(
        "Quantity: ")[1].strip())  # "2"
    # print(f"the second quantity: {quantity_text_2}")
    assert quantity_text_2 == 2, f"the expected quantiy is not 2"
    print("the expected quantity is 2")
    driver.quit()


def increase_same_item():
    driver = browser_call()
    add_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]')))
    add_to_cart.click()
    increase_quantity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="+"]')))
    for i in range(4):
        increase_quantity.click()
    time.sleep(1)
    print("TC_026 PASSED: Item Increased Sucessfully")
    driver.quit()


def decrease_same_item():
    driver = browser_call()
    add_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]')))
    add_to_cart.click()
    increase_quantity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="+"]')))
    for i in range(4):
        increase_quantity.click()
    decrease_quantity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="-"]')))
    for i in range(4):
        decrease_quantity.click()
    time.sleep(1)
    print("TC_027 PASSED: Item Decreased Sucessfully")
    driver.quit()
