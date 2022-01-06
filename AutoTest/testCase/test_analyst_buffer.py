import unittest
import os
import sys
# 必须加上以下几个路径，否则部署CI会报错找不到路径
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from testTools import baseOperation, baseApp
from pages import buffer
import time
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()


class MyTestCaseBuffer(unittest.TestCase):
    global driver

    # @classmethod
    # def setUpClass(cls):  # 固定写法，只在类执行之前执行一次！
    #     mylogger.info("开始执行测试类")
    #     print("开始执行测试")

    # @classmethod
    # def tearDownClass(cls, driver=driver):
    #     mylogger.info("结束执行测试类")
    #     baseOperation.home(driver);
    #     baseApp.closeApp(driver)
    #     print("结束测试")
    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("数据处理")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")

    #点数据单缓冲区分析
    def test_buffer1(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing","风景名胜",0,1000,0,"TestResult","BufferByPoint")
        buffer.resultCompare(self,self.driver,"641",1)

    # 点数据单缓冲区分析（合并缓冲区）
    def test_buffer2(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing","风景名胜",0,1000,1,"TestResult","BufferByPointMerge")
        buffer.resultCompare(self,self.driver,"1",0)

    # 线数据单缓冲区分析（平头缓冲）
    def test_buffer3(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 1, 1000, 0, "TestResult", "BufferFlatByLine")
        buffer.resultCompare(self,self.driver,"7", 1)

    # 线数据单缓冲区分析（平头缓冲&合并缓冲区）
    def test_buffer4(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 1, 1000, 1, "TestResult", "BufferFlatByLineMerge")
        buffer.resultCompare(self,self.driver,"1", 0)

    # 线数据单缓冲区分析（圆头缓冲）
    def test_buffer5(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 0, 1000, 0, "TestResult", "BufferRoundByLine")
        buffer.resultCompare(self,self.driver,"7", 1)

    # 线数据单缓冲区分析（平圆头缓冲&合并缓冲区）
    def test_buffer6(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 0, 1000, 1, "TestResult", "BufferRoundByLineMerge")
        buffer.resultCompare(self,self.driver,"1", 0)

    # 面数据单缓冲区分析
    def test_buffer7(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing", "区县级行政区划", 0, 1000, 0, "TestResult", "BufferByRegion")
        buffer.resultCompare(self,self.driver,"41", 1)

    # 面数据单缓冲区分析（合并缓冲区）
    def test_buffer8(self):
        buffer.setBufferparaAndAnalyst(self.driver,"ChongQing", "区县级行政区划", 0, 1000, 1, "TestResult", "BufferByRegionMerge")
        buffer.resultCompare(self,self.driver,"1", 0)

    # 点数据多重缓冲区分析
    def test_buffer9(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "风景名胜", 0,"1000","3000","3",0, "TestResult", "MultipleBufferByPoint")
        buffer.resultCompare(self,self.driver,"1923", 1)

    # 点数据多重缓冲区分析（合并缓冲区）
    def test_buffer10(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "风景名胜", 0,"1000","3000","3",1, "TestResult", "MultipleBufferByPointMerge")
        buffer.resultCompare(self,self.driver,"3", 1)

    # 线数据多重缓冲区分析（圆头缓冲）
    def test_buffer11(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 0, "100", "500", "5", 0, "TestResult",
                                        "MultipleBufferRoundByLine")
        buffer.resultCompare(self,self.driver,"35", 1)

     # 线数据多重缓冲区分析（圆头缓冲&合并缓冲区）
    def test_buffer12(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 0, "100", "500", "5", 1, "TestResult",
                                        "MultipleBufferRoundByLineMerge")
        buffer.resultCompare(self,self.driver,"5", 1)

    # 线数据多重缓冲区分析（平头缓冲）
    def test_buffer13(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 1, "100", "500", "5", 0, "TestResult",
                                        "MultipleBufferFlatByLine")
        buffer.resultCompare(self,self.driver,"35", 1)

    # 线数据多重缓冲区分析（平头缓冲&合并缓冲区）
    def test_buffer14(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "城市轨道交通", 1, "100", "500", "5", 1, "TestResult",
                                        "MultipleBufferFlatByLineMerge")
        buffer.resultCompare(self,self.driver,"5", 1)

    # 面数据多重缓冲区分析
    def test_buffer15(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "区县级行政区划", 0, "1000", "2000", "2", 0, "TestResult",
                                        "MultipleBufferByRegion")
        buffer.resultCompare(self,self.driver,"82", 1)

    # 面数据多重缓冲区分析（合并缓冲区）
    def test_buffer16(self):
        buffer.setMulBufferparaAndAnalyst(self.driver,"ChongQing", "区县级行政区划", 0, "1000", "2000", "2", 1, "TestResult",
                                        "MultipleBufferByRegionMerge")
        buffer.resultCompare(self,self.driver,"2", 1)

if __name__ == '__main__':
    unittest.main()