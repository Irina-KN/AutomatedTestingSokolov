from pages.main_page import MainePage
from pages.filter_category_page import FilterCategoryPage
from pages.jewelry_catalog_page import JeweryCatalogPage
from pages.basket_page import BasketPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_buy_product(set_up, set_group):

    option = Options()
    option.add_argument("--disable-notifications")

    driver = webdriver.Chrome(option)

    main_page = MainePage(driver)
    main_page.main_page_choosing_city()

    main_page.go_catalog_select_category()

    filter_category_page = FilterCategoryPage(driver)
    filter_category_page.select_filters()

    jewelry_catalog = JeweryCatalogPage(driver)
    catalog_product_name, catalog_product_price, catalog_product_size = jewelry_catalog.test_product()
    jewelry_catalog.go_to_basket()

    basket_page = BasketPage(driver)
    basket_product_name, basket_product_price, basket_product_size = basket_page.get_value_product_fields()

    try:
        assert catalog_product_name == basket_product_name
        print('The product name corresponds to')
    except AssertionError:
        print('The product name does not match')

    try:
        assert catalog_product_price == basket_product_price
        print('The product price corresponds to')
    except AssertionError:
        print('The product price does not match')

    try:
        assert catalog_product_size == basket_product_size
        print('The product size corresponds to')
    except AssertionError:
        print('The product price does not match')

    driver.quit()
