from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class JewelryCatalogPage(Base):

    catalog_product = '.product-list.catalog.sklv .sklv-product-link:nth-child(8)'
    catalog_product_basket = '.product-list.catalog.sklv .sklv-product-link:nth-child(8) .sklv-product-action'
    catalog_product_price = '.product-list.catalog.sklv .sklv-product-link:nth-child(8) div.sklv-prices__bottom'
    catalog_product_name = '.product-list.catalog.sklv .sklv-product-link:nth-child(8) .sklv-product-title'
    catalog_product_size = '.product-list.catalog.sklv .sklv-product-link:nth-child(8) .sklv-modal .sklv-modal__body button:nth-child(3)'
    basket_header_catalog = '.sklv-header-top__rigth .sklv-bar .sklv-bar_inner .sklv-bar-button.sklv-bar-button_basket'

    def field_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_product)))

    def button_product_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_product_basket)))

    def button_product_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_product_size)))

    def button_basket_header_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.basket_header_catalog)))

    def field_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_product_price)))

    def field_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_product_name)))

    def field_product_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_product_size)))

    def move_field_product(self):
        self.screenshot()
        self.action_on_element().move_to_element(self.field_product()).perform()

    def click_button_product_basket(self):
        self.button_product_basket().click()
        self.screenshot()

    def click_button_basket_header_catalog(self):
        self.action_on_element().move_to_element(self.button_basket_header_catalog()).perform()
        self.screenshot()
        self.button_basket_header_catalog().click()

    def click_button_product_size(self):
        self.button_product_size().click()
        self.screenshot()

    def select_product(self):
        self.screenshot()
        self.move_field_product()

    def get_value_field_product_name(self):
        product_name = self.field_product_name().text
        return product_name

    def get_value_field_product_price(self):
        self.screenshot()
        price = self.field_product_price().text
        price = price.replace('-55%', '')
        price = price.replace(' ', '')
        return price

    def get_value_field_product_size(self):
        value_size = self.field_product_size().text
        return float(value_size)

    def add_product_basket(self):
        self.click_button_product_basket()

    def select_product_size(self):
        self.click_button_product_size()

    def test_product(self):
        self.select_product()
        name = self.get_value_field_product_name()
        price = self.get_value_field_product_price()
        self.add_product_basket()
        size = self.get_value_field_product_size()
        self.select_product_size()
        return name, price, size

    def go_to_basket(self):
        self.click_button_basket_header_catalog()