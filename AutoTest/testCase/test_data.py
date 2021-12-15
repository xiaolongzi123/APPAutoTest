import configparser
import unittest
import os
import os.path
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from testTools import baseOperation, baseApp
from pages import data,common
import time
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
cf = configparser.ConfigParser()
cf.read(root_dir+"/config/config.ini")  # 拼接得到config.ini文件的路径，直接使用
deviceName=cf.get('device','deviceName')


class MyTestCaseData(unittest.TestCase):
    global driver
    @classmethod
    def setUpClass(cls):  # 固定写法，只在类执行之前执行一次！
        driver=baseApp.startApp("我的")
        common.delAllDataset(driver,"TestResult")
        mylogger.info("删除历史数据集成功")
        baseOperation.home(driver)
        baseApp.closeApp(driver)

    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("我的")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")



    #新建点数据集
    def test_createDataset1(self):
        ele=data.createDataset(self.driver,"TestResult","点","NewPoint")
        self.assertIsNotNone(ele,"新建失败")
    # 新建线数据集
    def test_createDataset2(self):
        ele = data.createDataset(self.driver,"TestResult", "线", "NewLine")
        self.assertIsNotNone(ele, "新建失败")
    # 新建面数据集
    def test_createDataset3(self):
        ele = data.createDataset(self.driver,"TestResult", "面", "NewRegion")
        self.assertIsNotNone(ele, "新建失败")
    # 新建文本数据集
    def test_createDataset4(self):
        ele = data.createDataset(self.driver,"TestResult", "文本", "NewText")
        self.assertIsNotNone(ele, "新建失败")
    # 新建CAD数据集
    def test_createDataset5(self):
        ele = data.createDataset(self.driver,"TestResult", "CAD", "NewCAD")
        self.assertIsNotNone(ele, "新建失败")
    #删除点数据集
    def test_delDataset1(self):
        ele=data.delDataset(self.driver,"TestResult","NewPoint")
        self.assertIsNotNone(ele, "删除失败")
    # 删除线数据集
    def test_delDataset2(self):
        ele=data.delDataset(self.driver,"TestResult","NewLine")
        self.assertIsNotNone(ele, "删除失败")
    # 删除面数据集
    def test_delDataset3(self):
        ele=data.delDataset(self.driver,"TestResult","NewRegion")
        self.assertIsNotNone(ele, "删除失败")

    # 删除文本数据集
    def test_delDataset4(self):
        ele=data.delDataset(self.driver,"TestResult","NewText")
        self.assertIsNotNone(ele, "删除失败")

    # 删除CAD数据集
    def test_delDataset5(self):
        ele=data.delDataset(self.driver,"TestResult","NewCAD")
        self.assertIsNotNone(ele, "删除失败")



