import os
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class semester_clusters():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id('clusterbtn').click()
        cal = GetData()
        self.fname = file_extention()
        cal.page_loading(self.driver)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        markers = len(dots)-1
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.exception_cluster()+cal.get_current_date()+'.csv'
        if os.path.isfile(self.filename) != True:
            os.remove(self.filename)
            return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)
        return markers