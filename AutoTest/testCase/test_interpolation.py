import configparser
import unittest
import os
import os.path
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from testTools import baseOperation, baseApp
from pages import interpolation
import time
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
cf = configparser.ConfigParser()
cf.read(root_dir+"/config/config.ini")  # 拼接得到config.ini文件的路径，直接使用
deviceName=cf.get('device','deviceName')


class MyTestCaseExport(unittest.TestCase):
    global driver

    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("数据处理")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")

    #插值分析-距离反比权重
    # @unittest.skip("bug")
    def test_interpolation1(self):
        srcDatasource="ChongQing"
        srcDataset="风景名胜"
        desDatasource = "TestResult"
        desDataset = "interpolation1"
        mapName="interpolationMap1"
        interpolation.createMapAddLayer(self.driver, mapName, srcDataset)
        interpolation.interpolationAnalyst(self.driver,"距离反比权重",srcDatasource,srcDataset,"pop2019",desDatasource,desDataset,"0","0")
        interpolation.resultCompare(self,self.driver,mapName)
    #插值分析-样条
    # @unittest.skip("bug")
    def test_interpolation2(self):
        srcDatasource = "ChongQing"
        srcDataset = "风景名胜"
        desDatasource = "TestResult"
        desDataset = "interpolation2"
        mapName = "interpolationMap2"
        interpolation.createMapAddLayer(self.driver,mapName,srcDataset)
        interpolation.interpolationAnalyst(self.driver, "样条", srcDatasource, srcDataset, "pop2019", desDatasource,desDataset,"10000", "3")
        interpolation.resultCompare(self, self.driver, mapName)
