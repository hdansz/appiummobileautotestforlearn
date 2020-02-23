# -*- coding:utf-8 -*-
import os
import allure
import pytest
from Cases.mydriver import mydriver
from Pages import searchpage, fcirclepage
from Tools import logger

class TestDemo:
    def setup(self):
        self.driver=mydriver()

    #搜索联系人
    @allure.MASTER_HELPER.step("搜索联系人")
    @pytest.mark.parametrize("name",["han"])
    def test_search_contact(self,name):
        search=searchpage.search(self.driver)
        search.search_contacts(name)

    #朋友圈发文字
    @allure.MASTER_HELPER.step("朋友圈发表文字")
    @pytest.mark.parametrize("word",["hello friend","a apple a day"])
    def test_publish_word(self,word):
        publish=fcirclepage.fcirclepublish(self.driver)
        publish.publish_word(word)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    #存放xml、html的报告路径
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_result = path + "/result/xml"
    #pytest+allure执行脚本，生成测试报告
    pytest.main(['-s', '-q', '--alluredir', file_result])
   '''
    #查看测试报告的方法
    #cmd生成HTML报告
    #file_report=path+"/report/html"
    # allure generate file_result -o file_report --clean
    # cmd查看HTML报告
    # allure open -h 127.0.0.1 -p 8083 file_report
    #print("cmd下生成HTML报告："+"allure generate "+ file_result+" -o "+file_report+" --clean")
    #print("查看HTML报告："+"allure open -h 127.0.0.1 -p 8083 "+file_report)
    '''