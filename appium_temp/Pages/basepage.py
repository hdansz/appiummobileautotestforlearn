# -*- coding:utf-8 -*-
import os
from appium.webdriver.common.touch_action import TouchAction
from Tools import logger

LOG = logger.Logger("base").getlog()
class base:
    _path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    def __init__ ( self, driver ):
        self.driver = driver
        self.log=LOG
    
    def find_element(self,loc):
        return self.driver.find_element(*(loc))#元组取值*(loc)

    def find_and_click(self,loc):
        return self.find_element(loc).click()

    def find_and_sendkeys(self,loc,words):
        return self.find_element(loc).send_keys(words)

    def find_elements(self,loc):
        return self.driver.find_elements(*(loc))

    def long_press(self,ele):
        return TouchAction(self.driver).long_press(ele).perform()

    def save_img(self,f_name):
        return self.driver.save_screenshot(self._path+"/result/img/"+f_name+".png")



