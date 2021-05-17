import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class completion_time_periods():
    def __init__(self,driver):
        self.driver = driver

    def test_completion_overall(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Overall ')
        timeseries.select_by_index(1)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for Over All')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(5)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            self.filename = self.p.get_download_dir() + '/'+'enrollment_completion_completion_all_district_overall_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options)-1
            for i in range(1,len(collnames.options)-1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion Over all csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            return counter,count

    def test_completion_last_day(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last Day ')
        timeseries.select_by_index(1)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last day')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/'+'tpd_'+ctype+'_all_district_last_day'+'_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options)-1
            for i in range(1,len(collnames.options)-1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion last day csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            # return counter,count

    def test_completion_last7_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 7 Days ')
        timeseries.select_by_index(2)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 7 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(4)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            ctype = (self.driver.find_element_by_id(Data.coursetype).text).strip()
            self.filename = self.p.get_download_dir() + '/'+'tpd_'+ctype+'_all_district_last_7_days'+'_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion last 7 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
            # return counter, count

    def test_completion_last30_days(self):
        self.data = GetData()
        self.p = pwd()
        self.msg = file_extention()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        course_type = Select(self.driver.find_element_by_id(Data.coursetype))
        # course_type.select_by_visible_text(' Completion ')
        course_type.select_by_index(2)
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 30 Days ')
        timeseries.select_by_index(3)
        self.data.page_loading(self.driver)
        if self.msg.no_data_available() in self.driver.page_source:
            print('No Data Available for last 30 days')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            times = (self.driver.find_element_by_name(Data.timeperiods).text).strip()
            ctype = course_type.first_selected_option
            self.filename = self.p.get_download_dir() + '/'+'enrollment_completion_completion_all_district_last_30_days_'+self.data.get_current_date()+'.csv'
            print(self.filename)
            self.data.page_loading(self.driver)
            collnames = Select(self.driver.find_element_by_id(Data.coll_names))
            counter = len(collnames.options) - 1
            for i in range(1, len(collnames.options) - 1):
                collnames.select_by_index(i)
                self.data.page_loading(self.driver)
            if os.path.isfile(self.filename) != True:
                print('Completion last 30 days csv file is not downloaded ')
                count = count + 1
            self.data.page_loading(self.driver)
            os.remove(self.filename)
        return  count
