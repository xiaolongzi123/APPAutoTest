import unittest
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from testTools import baseOperation, baseApp
from pages import overlay
import time
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()


class MyTestCaseOverlay(unittest.TestCase):
    global driver
    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("数据处理")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")
    # 点面裁剪
    def test_overlay1(self):
        overlay.setOverlayType(self.driver,"裁剪")
        overlay.setSrcData(self.driver,"China","居民点",1)
        overlay.setDesData(self.driver,"China","区域3")
        overlay.resultData(self.driver,"TestResult","ClipResult1")
        overlay.resultCompare(self,self.driver,"ClipResult1@TestResult","250",1)
    # 线面裁剪
    def test_overlay2(self):
        overlay.setOverlayType(self.driver,"裁剪")
        overlay.setSrcData(self.driver,"China", "国道",0)
        overlay.setDesData(self.driver,"China", "区域3")
        overlay.resultData(self.driver,"TestResult", "ClipResult2")
        overlay.resultCompare(self,self.driver,"ClipResult2@TestResult", "2913",1)
    # 面面裁剪
    def test_overlay3(self):
        overlay.setOverlayType(self.driver,"裁剪")
        overlay.setSrcData(self.driver,"China", "区域2", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "ClipResult3")
        overlay.resultCompare(self,self.driver,"ClipResult3@TestResult", "1",0)
    # 点面求交
    def test_overlay4(self):
        overlay.setOverlayType(self.driver,"求交")
        overlay.setSrcData(self.driver,"China", "居民点", 1)
        overlay.setDesData(self.driver,"China", "区域3")
        overlay.resultData(self.driver,"TestResult", "IntersectResult1")
        overlay.resultCompare(self,self.driver,"IntersectResult1@TestResult", "250", 1)
    # 线面求交
    def test_overlay5(self):
        overlay.setOverlayType(self.driver,"求交")
        overlay.setSrcData(self.driver,"China", "国道", 0)
        overlay.setDesData(self.driver,"China", "区域3")
        overlay.resultData(self.driver,"TestResult", "IntersectResult2")
        overlay.resultCompare(self,self.driver,"IntersectResult2@TestResult", "2913", 1)
    # 面面求交
    def test_overlay6(self):
        overlay.setOverlayType(self.driver,"求交")
        overlay.setSrcData(self.driver,"China", "区域2", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "IntersectResult3")
        overlay.resultCompare(self,self.driver,"IntersectResult3@TestResult", "1",0)
    # 点面擦除
    def test_overlay7(self):
        overlay.setOverlayType(self.driver,"擦除")
        overlay.setSrcData(self.driver,"China", "居民点", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "EraseResult1")
        time.sleep(20)
        overlay.resultCompare(self,self.driver,"EraseResult1@TestResult", "6110", 1)
    # 线面擦除
    def test_overlay8(self):
        overlay.setOverlayType(self.driver,"擦除")
        overlay.setSrcData(self.driver,"China", "国道", 0)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "EraseResult2")
        time.sleep(5)
        overlay.resultCompare(self,self.driver,"EraseResult2@TestResult", "21052", 1)
    # 面面擦除
    def test_overlay9(self):
        overlay.setOverlayType(self.driver,"擦除")
        overlay.setSrcData(self.driver,"China", "土地覆盖", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "EraseResult3")
        time.sleep(30)
        overlay.resultCompare(self,self.driver,"EraseResult3@TestResult", "19741", 1)
    # 点面同一
    def test_overlay10(self):
        overlay.setOverlayType(self.driver,"同一")
        overlay.setSrcData(self.driver,"China", "居民点", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "IdentityResult1")
        time.sleep(30)  # 分析时间较长
        overlay.resultCompare(self,self.driver,"IdentityResult1@TestResult", "12384", 1)
    # 线面同一
    def test_overlay11(self):
        overlay.setOverlayType(self.driver,"同一")
        overlay.setSrcData(self.driver,"China", "国道", 0)
        overlay.setDesData(self.driver,"China", "区域3")
        overlay.resultData(self.driver,"TestResult", "IdentityResult2")
        time.sleep(10)
        overlay.resultCompare(self,self.driver,"IdentityResult2@TestResult", "51477", 1)
    # 面面同一
    def test_overlay12(self):
        overlay.setOverlayType(self.driver,"擦除")
        overlay.setSrcData(self.driver,"China", "区域3", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "IdentityResult3")
        overlay.resultCompare(self,self.driver,"IdentityResult3@TestResult", "1", 0)
    # 面面合并
    def test_overlay13(self):
        overlay.setOverlayType(self.driver,"对称差")
        overlay.setSrcData(self.driver,"China", "区域3", 0)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "UnionResult")
        overlay.resultCompare(self,self.driver,"UnionResult@TestResult", "3", 1)
    # 面面对称差
    def test_overlay14(self):
        overlay.setOverlayType(self.driver,"对称差")
        overlay.setSrcData(self.driver,"China", "区域3", 0)
        overlay.setDesData(self.driver,"China", "区域2")
        overlay.resultData(self.driver,"TestResult", "XORResult")
        overlay.resultCompare(self,self.driver,"XORResult@TestResult", "2", 1)
    # 面面更新
    def test_overlay15(self):
        overlay.setOverlayType(self.driver,"对称差")
        overlay.setSrcData(self.driver,"China", "土地覆盖", 1)
        overlay.setDesData(self.driver,"China", "区域0")
        overlay.resultData(self.driver,"TestResult", "UpdateResult")
        time.sleep(20)
        overlay.resultCompare(self,self.driver,"UpdateResult@TestResult", "19743", 1)
if __name__ == '__main__':
    unittest.main()