# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.by import By
from Pages.basepage import base

class fcirclepublish(base):
    '''_xxx：加下划线_，用来定义类的私有变量
       By.XX：selenium.webdriver通用方法By，查找元素的方式，如By.XPATH、By.ID、
       By.CLASS_NAME、By.CSS_SELECTOR等
       此写法可分离页面变量和操作 '''
    #控件列表,数据类型为元组
    _found = (By.XPATH,"//*[@text='发现']")
    _cir = (By.XPATH,"//*[@text='朋友圈']")
    _ent = (By.XPATH,"//*[@class='android.support.v7.widget.LinearLayoutCompat']")
    _edis =(By.ID,"com.tencent.mm:id/d41")
    _pub = (By.ID,"com.tencent.mm:id/ln")
    _pubed = (By.XPATH,"//*[contains(@text,WORDS)]")
    #当前时间
    #now_time=time.asctime(time.localtime(time.time()))

    #朋友圈发表文字功能
    def publish_word(self,word):
        self.log.debug("点击APP的发现tab")
        self.find_and_click(self._found)
        self.log.debug("点击朋友圈")
        self.find_and_click(self._cir)
        ele=self.find_element(self._ent)
        self.log.debug("长按相机入口进入文本编辑器")
        self.long_press(ele)
        self.log.debug("输入内容："+word)
        self.find_and_sendkeys(self._edis,word)
        self.log.debug("点击发表文字")
        self.find_and_click(self._pub)
        self.log.debug("验证发布结果")
        assert len(self.find_elements(self._pubed))>=1