from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FilterCategoryPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    category_page_url = 'https://goldapple.ru/uhod'

    filter_subcategory = '#subcategory .filters-list .filter-parent-item:nth-child(3) div label'
    filter_delivery = '#delivery_type .filters-list .filter-parent-item:nth-child(4)'
    filter_store = '#store_id .btn-show'
    filter_store_list = '#store_id .filters-list.open .filter-parent-item:nth-child(12) div label'
    filter_material_1 = '#material .filters-list .filter-parent-item:nth-child(2) .filter-child-items div:nth-child(1) label'
    filter_material_2 = '#material .filters-list .filter-parent-item:nth-child(5) div label'
    filter_slider_lower = '#slider .noUi-base .noUi-origin .noUi-handle.noUi-handle-lower'
    filter_slider_upper = '#slider .noUi-base .noUi-origin .noUi-handle.noUi-handle-upper'
    filter_gender = '#gender .filters-list .filter-parent-item:nth-child(4) div label'
    view_products = '#filter .product-list-filters  .btn-desktop .apply-btn-desktop.btn.primary.send'

    def button_filter_subcategory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_subcategory)))

    def button_filter_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_delivery)))

    def button_filter_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_store)))

    def button_filter_store_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_store_list)))

    def button_filter_material_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_material_1)))

    def button_filter_material_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_material_2)))

    def button_filter_slider_lower(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_slider_lower)))

    def button_filter_slider_upper(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_slider_upper)))

    def button_filter_gender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_gender)))

    def button_view_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.view_products)))


# действия

    def click_button_filter_subcategory(self):
        self.button_filter_subcategory().click()

    def click_button_filter_delivery(self):
        self.button_filter_delivery().click()
        self.screenshot()

    def click_button_filter_store(self):
        self.button_filter_store().click()
        self.action_on_element().move_to_element(self.button_filter_store()).perform()
        self.screenshot()

    def click_button_filter_store_list(self):
        self.button_filter_store_list().click()
        self.action_on_element().move_to_element(self.button_filter_store_list()).perform()
        self.screenshot()

    def click_button_filter_material_1(self):
        self.button_filter_material_1().click()
        self.screenshot()

    def click_button_filter_material_2(self):
        self.button_filter_material_2().click()
        self.action_on_element().move_to_element(self.button_filter_material_2()).perform()
        self.screenshot()

    def drag_button_filter_slider_lower(self):
        self.action_on_element().drag_and_drop_by_offset(self.button_filter_slider_lower(), 50, 0).perform()

    def drag_button_filter_slider_upper(self):
        self.action_on_element().drag_and_drop_by_offset(self.button_filter_slider_upper(), -50, 0).perform()

    def click_button_filter_gender(self):
        self.button_filter_gender().click()
        self.action_on_element().move_to_element(self.button_filter_gender()).perform()
        self.screenshot()

    def click_button_view_products(self):
        self.button_view_products().click()

# подробно

    def select_store(self):
        self.click_button_filter_store()
        self.click_button_filter_store_list()

    def select_materials(self):
        self.click_button_filter_material_1()
        self.click_button_filter_material_2()

    def select_maximum_and_minimum_prices(self):
        self.drag_button_filter_slider_lower()
        self.drag_button_filter_slider_upper()

    def select_filters(self):
        self.screenshot()
        self.click_button_filter_subcategory()
        self.click_button_filter_delivery()
        self.select_store()
        self.select_materials()
        self.select_maximum_and_minimum_prices()
        self.click_button_filter_gender()
        self.click_button_view_products()