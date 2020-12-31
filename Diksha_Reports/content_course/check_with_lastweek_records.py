
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Districtwise_lastweek_records():
    def __init__(self,driver):
        self.driver = driver

    def test_districts(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(' Last 7 Days ')
        times.select_by_index(1)
        time.sleep(2)
        if "No data found" in self.driver.page_source:
            print("Last 7 Day are not having records")
        else:
            districts  =Select(self.driver.find_element_by_id('choose_dist'))
            for x in range(len(districts.options)-1,len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                self.data.page_loading(self.driver)
                if  "No data found" in self.driver.page_source:
                    print(districts.options[x].text ," does not last week records")
                    count = count + 1
        return count