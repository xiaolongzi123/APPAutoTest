import os
import sys
import time
import unittest
import ddt
# 必须加上以下几个路径，否则部署CI会报错找不到路径
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from pages import buffer
from testTools import baseApp, baseOperation
from testTools.testLog import Logger

mylogger=Logger(logger='TestMyLog').getlog()

@ddt.ddt
class MyTestCaseBuffer(unittest.TestCase):
    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("数据处理")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")


    @ddt.file_data('../dataYaml/buffer.yaml')
    def test_a1(self, **para):
        buffer.setBufferparaAndAnalyst(self.driver,para.get('datasource'),para.get('dataset'),
                                       para.get('type'),para.get('distance'),para.get('ismerge'),
                                       para.get('resultdatasource'),para.get('resultdataset'))

if __name__ == '__main__':
    unittest.main()
