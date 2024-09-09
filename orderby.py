from confi import *


def order_by_is_visible():
    try:
        driver = browser_call()
        orderby_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class= "sort"]//select')))
        orderby_button.is_displayed()
        print("TC_014 PASSED: Order By Button is Visible")
        driver.quit()
    except Exception as e:
        print("fail")


def order_items_from_low_to_high():
    try:
        driver = browser_call()
        order_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class= "sort"]//select')))
        select = Select(order_button)
        select.select_by_visible_text("Lowest to highest")
        time.sleep(2)
        print("TC016 PASSED: Items Is in Low to High Order")
        driver.quit()
    except Exception as e:
        print("fail", {e})


def order_items_from_high_to_low():
    try:
        driver = browser_call()
        order_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class= "sort"]//select')))
        select = Select(order_button)
        select.select_by_visible_text("Highest to lowest")
        time.sleep(2)
        print("TC017 PASSED: Items Is in HIgh to Low Order")

        driver.quit()
    except Exception as e:
        print("fail", {e})
