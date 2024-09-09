from confi import *


def signin_with_invalid_credentials():
    try:
        driver = browser_call()
        signin_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='signin']")))

        signin_button.click()
        username_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Username")]')))
        username_element.click()

        action = ActionChains(driver)
        action.send_keys("tigger")
        # using action chains enteriing tab key
        press_tabkey = action.send_keys(Keys.TAB).perform()
        passsword_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Password")]')))
        passsword_element.click()

        action = ActionChains(driver)
        action.send_keys("cat12345")
        press_tabkey = action.send_keys(Keys.TAB).perform()
        login_button = driver.find_element(
            By.XPATH, '//button[@id="login-btn"]')

        login_button.click()

        time.sleep(2)

        expected_message_text = "Invalid Username or Password"
        actual_message_text = driver.find_element(
            By.XPATH, "//h3[normalize-space()='Invalid Username']").text

        assert expected_message_text == actual_message_text, f"FAILED: {expected_message_text} doesn't match {actual_message_text}"
        print("TC_020 PASSED: Sucessfull SignIn with Invalid Username and Invalid Password")

    except Exception as e:
        print({e})
    driver.quit()


def signin_with_valid_username_invalid_password():
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
        enter_pass = action.send_keys("test123")
        # using action chains enteriing tab key
        press_tabkey = action.send_keys(Keys.TAB).perform()
        login_button = driver.find_element(
            By.XPATH, '//button[@id="login-btn"]')

        login_button.click()

        time.sleep(2)

        expected_message_text = "Invalid Password"
        actual_message_text = driver.find_element(
            By.XPATH, "//h3[normalize-space()='Invalid Password']").text

        assert expected_message_text == actual_message_text, f"FAILED: {expected_message_text} doesn't match {actual_message_text}"
        print("TC_022 PASSED: Sucessfull SignIn with Valid Username and Invalid Password")

        driver.quit()
    except Exception as e:
        print({e})


def signin_with_invalid_username_valid_password():
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
        action = ActionChains(driver)
        enter_user = action.send_keys("test124")
        press_tabkey = action.send_keys(Keys.TAB).perform()

        passsword_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Select Password")]')))
        passsword_element.click()

        action = ActionChains(driver)
        # using action chains enteriing tab key
        press_tabkey = action.send_keys(Keys.TAB).perform()

        login_button = driver.find_element(
            By.XPATH, '//button[@id="login-btn"]')

        login_button.click()

        time.sleep(2)

        expected_message_text = "Invalid Username"
        actual_message_text = driver.find_element(
            By.XPATH, "//h3[normalize-space()='Invalid Username']").text

        assert expected_message_text == actual_message_text, f"FAILED: {expected_message_text} doesn't match {actual_message_text}"
        print("TC_021 PASSED: Sucessfull SignIn with InValid Username and valid Password")

        driver.quit()
    except Exception as e:
        print({e})


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

        driver.quit()
    except Exception as e:
        print({e})
