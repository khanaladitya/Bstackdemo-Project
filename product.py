from confi import *


def count_total_number_of_products_on_home_page():
    driver = uc.Chrome()
    driver.get("https://bstackdemo.com/")
    driver.maximize_window()

    # Original item title that was added to the cart
    expected_number_of_products = 25

    # Locating all the products inside container
    items_inside_container = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='shelf-container']//div[@class='shelf-item']")))

    total_number_of_products = len(items_inside_container)

    if expected_number_of_products == total_number_of_products:
        assert True
        print(
            f"TC_006 PASSED: Expected number of Product matches actual number of products")
    else:
        assert False, f"FAILED: Expected number of Product doesn't matches actual number of products"

    driver.quit()
