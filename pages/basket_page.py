from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasketPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    basket_page_url = 'https://sokolov.ru/basket/'

    basket_product = '.checkout-products .checkout-product:nth-child(1)'
    basket_product_price = '.checkout-products .checkout-product:nth-child(1) div .checkout-product__info .checkout-product__info-row div .checkout-product__cost'
    basket_product_name = '.checkout-products .checkout-product:nth-child(1) div .checkout-product__info .checkout-product__info-row a'
    basket_product_size = '.checkout-products .checkout-product:nth-child(1) div .checkout-product__info .checkout-product__controls button span'

    def field_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.basket_product_price)))

    def field_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.basket_product_name)))

    def field_product_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.basket_product_size)))

    def get_value_field_product_price(self):
        self.screenshot()
        product_price = self.field_product_price().text
        product_price = product_price.replace(' ₽', '')
        product_price = product_price.replace(' ', '')
        return int(product_price)

    def get_value_product_field_name(self):
        return self.field_product_name().text

    def get_value_product_field_size(self):
        product_size = self.field_product_size().text
        product_size = product_size.replace('1 шт, ', '')
        product_size = product_size.replace('размер', '')
        return float(product_size)

    def get_value_product_fields(self):
        name = self.get_value_product_field_name()
        price = self.get_value_field_product_price()
        size = self.get_value_product_field_size()
        return name, price, size


