import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class last7day_download():
    def __init__(self,driver):
        self.driver = driver

    def test_last_7_records(self):
        self.data = GetData()
        self.p = pwd()
        self.fname = file_extention()
        self.data.page_loading(self.driver)
        period = Select(self.driver.find_element_by_id('period'))
        # period.select_by_visible_text(' Last 7 Days ')
        period.select_by_index(3)
        self.data.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        count = len(markers)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(4)
        self.filename = self.p.get_download_dir() + '/' + self.fname.telemetry_last7days()+self.data.get_current_date()+'.csv'
        print(self.filename)
        file = os.path.isfile(self.filename)
        self.data.page_loading(self.driver)
        os.remove(self.filename)
        return file
