import os
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class ClusterwiseCsv():

    def __init__(self, driver, year, month):
        self.driver = driver
        self.year = year.strip()
        self.month = month.strip()

    def click_download_icon_of_clusters(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management_name = self.driver.find_element_by_id('name').text
        name = management_name[16:].strip().lower()
        self.year,self.month = cal.get_student_month_and_year_values()
        self.driver.find_element_by_id(Data.SAR_Clusters_btn).click()
        cal.page_loading(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() +'/'+files.teacher_cluster_download()+name+'_allClusters_'+self.month+"_"+self.year+'_'+cal.get_current_date()+".csv"
        print(self.filename)
        if os.path.isfile(self.filename) !=True:
            count = count + 1
        else:
            os.remove(self.filename)
        return count
