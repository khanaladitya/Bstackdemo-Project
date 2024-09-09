from confi import *


def filter_samsung_products_and_validate():

    driver = uc.Chrome()
    driver.get("https://bstackdemo.com/")
    driver.maximize_window()
    try:
        click_samsung_on_filter = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Samsung']"))).click()

        time.sleep(2)

        products_after_filter = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='shelf-container']//p[@class='shelf-item__title']")))
        print(f"Total Samsung Products: {len(products_after_filter)}")

        # Iterate over all products and print the individual product title
        for product in products_after_filter:
            expected_product_name = "Galaxy"
            product_names = product.text
            if expected_product_name not in product_names:
                assert False
            if expected_product_name in product_names:
                assert True
    except Exception as e:
        print(f"An error occurred: {e}")
    driver.quit()
