import time
from pages.main_page import MainePage
from selenium import webdriver


def test_new():
    driver = webdriver.Chrome()

    main_page = MainePage(driver)
    main_page.get_main_page()
    main_page.catalog_click()


    time.sleep(10)
    driver.quit()
