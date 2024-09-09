from confi import *


def successfully_order_single_product_and_verify_on_order_page():
    driver = uc.Chrome()
    driver.maximize_window()
    driver.get("https://bstackdemo.com/")

    # ActionChains Instance
    action = ActionChains(driver)

    # Variables
    expected_product = "One Plus 7"
    first_name = "Aditya"
    last_name = "Khanal"
    address = "Kirtipur"
    province = "Bagmati"
    postal_code = "44400"

    original_product_title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='"+expected_product+"']"))).text

    #  Select item and Click 'Add to Cart' button
    add_item_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Add to cart'][preceding-sibling::p[text()='"+expected_product+"']]"))).click()
    print("Successfully Clicked on Add to Cart")

    # Validation of 'original product title' with 'item showed in the cart'
    item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "body div[id='__next'] div div div div div div:nth-child(3) p:nth-child(1)"))).text

    assert item_in_cart == original_product_title, "Validation Failed: The product title do not match the item that is in cart"
    print("Validation Successful: The original product title match the item that is in cart")

    # Click 'Checkout' Button After Adding item to Cart
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Checkout']"))).click()
    print(f"Successfully Added item {item_in_cart} to Cart")

    # Signin via. Valid Username and Valid Password
    username_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Username")]'))).click()
    action.send_keys(Keys.TAB).perform()

    passsword_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Password")]'))).click()
    action.send_keys(Keys.TAB).perform()

    # Click Login Button
    login_button = driver.find_element(
        By.XPATH, '//button[@id="login-btn"]').click()

    time.sleep(2)

    # Validate Successful Login
    unique_locator = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//legend[@data-test='shipping-address-heading']")))
    if unique_locator.is_displayed():
        print("Successful Login")
    else:
        print("Login Failed")

    # Validation of 'original item title' with item showed in 'Order Summary' in Checkout
    checkout_product_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//h5[normalize-space()='"+expected_product+"']"))).text

    assert checkout_product_title == original_product_title, "Validation failed: The product titles doesn't matches the title that is in checkout section"
    print("Validation Successful: The product titles matches the title that is in checkout section")

    # Checkout Process Form Fillup
    enter_first_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='firstNameInput']")))
    enter_first_name.send_keys(first_name)
    print(f"Entered First name is: {first_name}")

    enter_last_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='lastNameInput']")))
    enter_last_name.send_keys(last_name)
    print(f"Entered last name is: {last_name}")

    enter_address_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='addressLine1Input']")))
    enter_address_name.send_keys(address)
    print(f"Entered Address is: {address}")

    enter_state_or_province = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='provinceInput']")))
    enter_state_or_province.send_keys(province)
    print(f"Entered Province is: {province}")

    enter_postal_code = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='postCodeInput']")))
    enter_postal_code.send_keys(postal_code)
    print(f"Entered Postal Code is: {postal_code}")

    click_sumbit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='checkout-shipping-continue']"))).click()
    print("Clicked Sumbit Button")

    # Validation of Successful Order
    successful_order_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//legend[@id='confirmation-message']"))).text

    expected_order_confirmation_message = "Your Order has been successfully placed."

    assert expected_order_confirmation_message == successful_order_message, "Order confirmation messages do not match."

    # Download Order Receipt
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id = 'downloadpdf']"))).click()
    time.sleep(3)

    # Verify File Download
    try:
        # Get the username from environment variables
        username = os.getenv('USERNAME')
        print(username)

        # Set the download directory using the retrieved username
        download_directory = fr"C:\Users\{username}\Downloads"

        file_name = "confirmation.pdf"

        file_path = os.path.join(download_directory, file_name)

        # Assert if the file exists

        assert os.path.exists(
            file_path), f"the file path {file_name} does not exist"

        print(f"{file_name} has been successfully downloaded.")

    except FileNotFoundError:
        pass

    click_continiue_shopping = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Continue Shopping »']"))).click()

    click_order_from_nav = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Orders']"))).click()

    product_title_element_in_order = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='a-row' and contains(.,'"+expected_product+"')])[2]")))
    full_text = product_title_element_in_order.text
    order_product_title = full_text.replace("Title: ", "").strip()

    assert order_product_title == original_product_title, "Validation Failed: The original product title doesn't matches the item that is in order section"

    print(
        f"Validation Successful: The original product title is {order_product_title} in order page")

    driver.quit()
