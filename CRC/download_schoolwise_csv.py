import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class school_wise_download():
    def __init__(self,driver):
        self.driver = driver

    def test_schoolwise(self):
        self.cal = GetData()
        self.fname=file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('nm').text
        name = management_name[16:].strip().lower()
        p =pwd()
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        District_wise.select_by_visible_text(" School Wise Infra_Table_Report ")
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.cal.page_loading(self.driver)
        self.filename = p.get_download_dir() + '/' + self.fname.crc_school()+name+'_overall_allSchools_'+self.cal.get_current_date()+'.csv'
        self.cal.page_loading(self.driver)
        return os.path.isfile(self.filename)

    def remove_file(self):
        os.remove(self.filename)


