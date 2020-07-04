import time

from Data.parameters import Data
from reuse_func import GetData


class click_on_blocks():
   def __init__(self,driver ):
       self.driver = driver
   def test_blocks_button(self):
       self.p = GetData()
       self.driver.find_element_by_xpath(Data.hyper_link).click()
       self.p.page_loading(self.driver)
       self.driver.find_element_by_id(Data.scm_block).click()
       self.p.page_loading(self.driver)
       dots = self.driver.find_elements_by_class_name(Data.dots)
       count = len(dots) - 1
       self.p.page_loading(self.driver)
       return count

