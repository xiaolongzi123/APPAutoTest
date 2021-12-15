import os
import sys
from testTools import baseOperation
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

def compareResult(self, fileName):
    f = os.popen(r"adb shell ls /sdcard/iTablet/ExternalData/ExportData", "r")
    b = f.read()
    f.close()
    print(b)
    result = b.find(fileName) >= 0
    print(result)
    self.assertTrue(result, "执行失败")

def datasetExport(driver ,datasource ,dataset ,type):
    baseOperation.findElementAndClick(driver, "text", "数据")
    baseOperation.findElementAndClick(driver, "text", datasource)
    if dataset=='CAD' or dataset=='Text':
        baseOperation.swipe_to_up(driver)
    # 获取数据集的中心点坐标并通过相对位置点击菜单
    pt =baseOperation.findElementCenterPt(driver, "text", dataset)
    baseOperation.clickByPt1(driver, 1000, pt[1])
    baseOperation.findElementAndClick(driver, "text", "分享数据集")
    baseOperation.findElementAndClick(driver, "text", "本地")
    baseOperation.findElementAndClick(driver, "text" ,type)
    baseOperation.findElementAndClick(driver ,"text" ,"确定")
    time.sleep(10)


if __name__ == "__main__":
    datasetExport("ChongQing","DEM","*.tif")