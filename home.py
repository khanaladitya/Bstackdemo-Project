
from confi import *


def logo_visible():

    try:

        driver = browser_call()
        bstack_logo = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "svg[width = '257']")))
        bstack_logo.is_displayed()
        print("TC_001 PASSED: Logo Is Visible")
        driver.quit()
    except Exception as e:
        print("test failed: logo is not visible", {e})


def verify_copyright():
    try:
        driver = browser_call()
        copyright = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//span[normalize-space()="© 2020 BrowserStack. All rights reserved."]')))
        expected_text = "© 2020 BrowserStack. All rights reserved."
        # assert copyright.text == expected_text
        if copyright.text == expected_text:
            print("TC_057 PASSED: Copyright Text is Visible")
        else:
            print("fail")
        driver.quit()
    except Exception as e:
        print("exception fail", {e})


def Orders_is_clickable_on_nav_menu():
    try:
        driver = browser_call()
        orders_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//strong[normalize-space()="Orders"]')))
        orders_button.is_displayed()
        orders_button.click()
        assert "orders" in driver.current_url
        print("TC_037 PASSED: Orders in Nav menu is Clickable")
        driver.quit()
    except Exception as e:
        print("exception fail", {e})


def fill_in_checkout_details():
    try:
        driver = browser_call()
        first_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//input[@id="firstNameInput"]')))
        first_name.send_keys("aditya")
        last_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//input[@id="lastNameInput"]')))
        last_name.send_keys("khanal")
        address = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#addressLine1Input')))
        address.send_keys("kirtipur")
        state_province = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//input[@id="provinceInput"]')))
        state_province.send_keys("kathmandu")
        postal_code = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="postCodeInput"]')))
        postal_code.send_keys("12345")
        submit_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="checkout-shipping-continue"]')))
        submit_button.click()
        driver.quit()
    except Exception as e:
        print("exception fail", {e})


def Orders_details_visible():
    try:
        driver = browser_call()
        signin_with_valid_credentials()
        add_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]')))
        add_to_cart.click()
        checkout = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="buy-btn"]')))
        checkout.click()
        fill_in_checkout_details()
        successful_order_validation = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//legend[@id="confirmation-message"]')))
        successful_order_validation.is_displayed()
        continue_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//button[normalize-space()="Continue Shopping »"]')))
        continue_button.click()

        home_page_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]')))

        home_page_element.is_displayed()
        time.sleep(1)
        Orders_is_clickable_on_nav_menu()
        time.sleep(1)
        order_title = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//strong[normalize-space()="Title:"]')))
        order_title.is_displayed()
        print("pass")
        time.sleep(1)
        driver.quit()
    except Exception as e:
        print("fail", {e})


def signin_with_valid_credentials():
    try:
        driver = browser_call()
        signin_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='signin']")))

        signin_button.click()
        username_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Username")]')))
        username_element.click()
        select_username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='demouser' or @id='react-select-2-option-0-0']")))
        select_username.click()
        passsword_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Password")]')))
        passsword_element.click()
        action = ActionChains(driver)
        # using action chains enteriing tab key
        press_tabkey = action.send_keys(Keys.TAB).perform()

        login_button = driver.find_element(
            By.XPATH, '//button[@id="login-btn"]')

        login_button.click()
        unique_element_after_login = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="username"]')))
        if unique_element_after_login.is_displayed():
            print("TC_024 PASSED: Sucessfull SignIn with Valid Credentials")
        else:
            print("fail")

    except Exception as e:
        print({e})


def verify_fav_functionality():
    try:

        driver = browser_call()
        signin_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='signin']")))

        signin_button.click()
        username_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Username")]')))
        username_element.click()
        select_username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='demouser' or @id='react-select-2-option-0-0']")))
        select_username.click()
        passsword_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Password")]')))
        passsword_element.click()
        action = ActionChains(driver)
        # using action chains enteriing tab key
        press_tabkey = action.send_keys(Keys.TAB).perform()

        login_button = driver.find_element(
            By.XPATH, '//button[@id="login-btn"]')

        login_button.click()
        unique_element_after_login = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="username"]')))

        time.sleep(1)
        add_to_fav = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[id="1"] span[class="MuiIconButton-label"] svg')))
        add_to_fav.click()
        time.sleep(2)
        favourites = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//strong[normalize-space()="Favourites"]')))
        favourites.click()
        time.sleep(2)
        assert 'favourites' in driver.current_url
        item_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//p[@class="shelf-item__title"]')))
        if item_visible.is_displayed:
            print("TC_055 PASSED: Item is Visible")
        else:
            print("item is not visible")
        driver.quit()
    except Exception as e:
        print("fail", {e})


def price_calculation():
    driver = browser_call()

    # Step 1: Add the item to the cart
    add_to_cart = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div[id="1"] div[class="shelf-item__buy-btn"]'))
    )
    add_to_cart.click()

    # Step 2: Extract the price for one item
    extract_price_for_one_item = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//p[@class="sub-price__val"]'))
    )
    initial_item_price = extract_price_for_one_item.text  # Accessing the text content
    item_price = float(initial_item_price.replace(
        '$', '').strip())  # Convert to float

    print(f"The price of one item is: ${item_price}")
    increase_quantity = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="+"]')))

    items = 10

    for i in range(items):
        increase_quantity.click()
     # Step 2: Extract the price for one item
    extract_price_for_five_item = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//p[@class="sub-price__val"]'))
    )
    final_extracted_price = extract_price_for_five_item.text  # Accessing the text content
    item_price_after_update = float(final_extracted_price.replace(
        '$', '').strip())  # Convert to float
    print(f"The price of five item is: ${item_price_after_update}")

    expected_total_price = item_price * (items+1)

    assert expected_total_price == item_price_after_update, (
        f" Total price mismatch! Expected: ${expected_total_price}, Actual: ${item_price_after_update}")

    print(
        f"TC_035 PASSED: Total price match! Expected: ${expected_total_price}, Actual: ${item_price_after_update}.")
    driver.quit()
