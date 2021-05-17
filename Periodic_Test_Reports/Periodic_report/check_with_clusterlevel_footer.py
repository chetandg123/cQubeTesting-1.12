

import csv
import os
import re
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Clusterwise_footers():

    def __init__(self, driver):
        self.driver = driver

    def check_with_footervalues(self):
        cal = GetData()
        files = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        management = self.driver.find_element_by_id('nm').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_id(Data.cluster_btn).click()
        cal.page_loading(self.driver)
        markers = self.driver.find_elements_by_class_name(Data.dots)
        dots = len(markers)-1
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        p = pwd()
        count = 0
        self.filename = p.get_download_dir() + "/"+ files.pat_cluster()+management+'_all_allGrades__allClusters_'+cal.get_current_date()+'.csv'
        print(self.filename)
        if os.path.isfile(self.filename) != True:
            return "File Not Downloaded"
        else:
            with open(self.filename) as fin:
                csv_reader = csv.reader(fin, delimiter=',')
                header = next(csv_reader)
                data = list(csv_reader)
                row_count = len(data)
                if int(dots) != row_count:
                    print("Markers and csv file records count mismatched", dots, row_count)
                    count = count + 1
            os.remove(self.filename)
        return dots, count


