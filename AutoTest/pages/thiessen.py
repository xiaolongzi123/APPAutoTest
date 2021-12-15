import os
import sys
from testTools import baseOperation
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

def thiessenAnalyst(driver ,srcDatasource ,srcDataset ,desDatasource ,desDataset):
    baseOperation.findElementAndClick(driver, "text", "分析")
    baseOperation.findElementAndClick(driver, "text", "泰森多边形")
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
    baseOperation.findElementCenterPt(driver, "text", srcDatasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")
    baseOperation.findElementCenterPt(driver, "text", srcDataset)
    baseOperation.findElementAndClick(driver, "text" ,"确定")
    baseOperation.findElementAndClick(driver ,"xpath" ,"//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]")
    baseOperation.findElementCenterPt(driver, "text", desDatasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver,"xpath","//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver,"class","android.widget.EditText")
    baseOperation.input(driver,"class","android.widget.EditText",desDataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "text", "分析")
    time.sleep(5)
def compareResult(self,driver,count):
    baseOperation.findElementAndClick(driver,"text","图层")
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver,"text","属性")
    baseOperation.findElementAndClick(driver,"text","定位")
    baseOperation.findElementAndClick(driver, "text", "定位到末行")
    ele=baseOperation.findElement(driver,"text",count)
    self.assertIsNotNone(ele, "执行失败")

if __name__ == "__main__":
    print("111")