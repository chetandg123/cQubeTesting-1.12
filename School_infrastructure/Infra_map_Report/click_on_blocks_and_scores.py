import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class block_btn_scores():
    def __init__(self,driver):
        self.driver = driver

    def test_click_blocks(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id('blockbtn').click()
        self.p.page_loading(self.driver)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        for i in range(len(scores.options)):
            time.sleep(1)
            scores.select_by_index(i)
        self.p.page_loading(self.driver)