from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainePage(Base):

    main_page_url = 'https://sokolov.ru/'

    search_city = '.form-input.search-city'
    city = 'Москва'
    city_field = '.suggest-wrapper.open .suggest-item:nth-child(1)'
    choice_city = '.sklv-button.sklv-change-city-button'
    catalog = '.sklv-button.sklv-button_black'
    category = '.sklv-nav__list .sklv-nav__list__point.sklv-nav__list__point_active .sklv-nav__list__item .sklv-nav__list__item__el:nth-child(2) .sklv-nav__list__item__el_sub .sklv-nav__list__item__el_sub_small_tile:nth-child(1)'

    def get_main_page(self):
        self.driver.get(self.main_page_url)
        self.driver.maximize_window()

    def button_choice_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.choice_city)))

    def field_search_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search_city)))

    def field_selection_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.city_field)))

    def button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog)))

    def button_category(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.category)))

    def click_button_choice_city(self):
        self.screenshot()
        self.button_choice_city().click()

    def input_in_field_search_city(self):
        self.field_search_city().send_keys(self.city)
        self.screenshot()

    def click_field_selection_city(self):
        self.action_on_element().move_to_element(self.field_selection_city()).perform()
        self.screenshot()
        self.field_selection_city().click()

    def click_button_catalog(self):
        self.button_catalog().click()
        self.screenshot()

    def click_button_category(self):
        self.action_on_element().move_to_element(self.button_category()).perform()
        self.screenshot()
        self.button_category().click()

    def main_page_choosing_city(self):
        self.get_main_page()
        self.click_button_choice_city()
        self.input_in_field_search_city()
        self.click_field_selection_city()

    def go_catalog_select_category(self):
        self.click_button_catalog()
        self.click_button_category()

