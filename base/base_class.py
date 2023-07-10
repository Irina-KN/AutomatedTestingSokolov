from selenium.webdriver import ActionChains
import datetime

import screen2


class Base:

    def __init__(self, driver):
        self.driver = driver

    def action_on_element(self):
        return ActionChains(self.driver)

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
        name_screenshot = 'test_screenshot_' + now_date + '.png'
        path_for_screenshot = './screen/' + name_screenshot
        self.driver.save_screenshot(path_for_screenshot)
