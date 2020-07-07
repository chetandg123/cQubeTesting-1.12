import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class crc_schoolevel_records():

    def __init__(self,driver):
        self.driver = driver

    def test_schoolwise(self):
        p = pwd()
        self.cal = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.cal.page_loading(self.driver)
        select_district = Select(self.driver.find_element_by_name('myDistrict'))
        select_block = Select(self.driver.find_element_by_name('myBlock'))
        select_cluster = Select(self.driver.find_element_by_name('myCluster'))

        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            self.cal.page_loading(self.driver)
            for y in range(len(select_block.options)-1, len(select_block.options)):
                select_block.select_by_index(y)
                self.cal.page_loading(self.driver)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    self.cal.page_loading(self.driver)
                    nodata = self.driver.find_element_by_id("errMsg").text
                    if nodata == "No data found":
                        print(select_cluster.options[z].text,"no data found!")
                    else:
                        self.driver.find_element_by_id(Data.Download).click()
                        time.sleep(3)
                        self.filename = p.get_download_dir() + "/School_level_CRC_Report.csv"
                        if not os.path.isfile(self.filename):
                            print(select_cluster.options[z].text ," csv file not downloaded")
                        else:
                            with open(self.filename) as fin:
                                csv_reader = csv.reader(fin, delimiter=',')
                                header = next(csv_reader)
                                schools = 0
                                vsts = 0
                                totscs = 0
                                for row in csv.reader(fin):
                                    schools += int(row[0])
                                    vsts += int(row[15])
                                    totscs += int(row[1])
                                totalschools = self.driver.find_element_by_id("schools").text
                                schoolvisited = self.driver.find_element_by_id("visited").text
                                visits = self.driver.find_element_by_id("visits").text
                                sc = re.sub('\D', "", schoolvisited)
                                vs = re.sub('\D', "", visits)
                                tsc = re.sub('\D', "", totalschools)
                                self.cal.page_loading(self.driver)
                                if int(sc) != schools:
                                    print("mismatch found at", select_cluster.options[z].text, ":",
                                          "total no of schools visited :", schools, int(sc))
                                if int(tsc) != totscs:
                                    print("mismatch found at", select_cluster.options[z].text, ":",
                                          "total no of schools visited :", totscs, int(tsc))
                                if int(vs) != vsts:
                                    print("mismatch found at", select_cluster.options[z].text, ":",
                                          "total no of schools visited :", vsts, int(vs))

                            os.remove(self.filename)

