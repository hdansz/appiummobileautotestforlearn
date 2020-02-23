# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Pages.basepage import base

class search(base):
    _serch = (By.ID, "com.tencent.mm:id/r_")
    _conte = (By.ID, "com.tencent.mm:id/m7")
    _resus = (By.ID, "com.tencent.mm:id/s5")

    def search_contacts( self, name ) :
        self.log.debug("点击搜索框")
        self.find_and_click(self._serch)
        self.log.debug("输入搜索内容")
        self.find_and_sendkeys(self._conte,name)
        self.log.debug("验证搜索结果")
        assert len(self.find_elements(self._resus))>=1