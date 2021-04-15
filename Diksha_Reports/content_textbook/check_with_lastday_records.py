import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Districtwise_lastday_records():
    def __init__(self,driver):
        self.driver = driver

    def test_districts(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        times = Select(self.driver.find_element_by_name('timePeriod'))
        # times.select_by_visible_text(' Last Day ')
        times.select_by_index(3)
        print(times.first_selected_option)
        self.data.page_loading(self.driver)
        if self.msg.no_data_found() in self.driver.page_source:
            print("Last days records")
        else:
            districts  =Select(self.driver.find_element_by_id('choose_dist'))
            for x in range(len(districts.options)-3,len(districts.options)):
                time.sleep(1)
                districts.select_by_index(x)
                self.data.page_loading(self.driver)
                if  self.msg.no_data_found() in self.driver.page_source:
                    print(districts.options[x].text ," does not last day records")
                    count = count + 1
        return count