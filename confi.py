from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import undetected_chromedriver as uc
import os


def browser_call():
    chrome_option = uc.ChromeOptions()
    chrome_option.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_option.add_argument("--headless")

    driver = uc.Chrome(options=chrome_option)
    driver.get("https://bstackdemo.com/")
    assert "bstack" in driver.current_url
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "svg[width = '257']")))
    driver.maximize_window()
    time.sleep(1)
    return driver
