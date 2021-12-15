import os
import sys
import time
from testTools import baseOperation
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

# 叠加分析方式
def setOverlayType(driver, type):
    baseOperation.findElementAndClick(driver, "xpath",
                                      "// android.view.ViewGroup / android.view.ViewGroup[3] / android.view.ViewGroup[2] / android.widget.ImageView[1]")
    time.sleep(2)
    baseOperation.findElementAndClick(driver, "text", "分析")
    baseOperation.findElementAndClick(driver, "text", "叠加分析")
    baseOperation.findElementAndClick(driver, "text", type)


# 源数据
def setSrcData(driver, datasource, dataset, isswip):
    ############源数据##########################################
    # 数据源 isswip=1为需要滑动时设置
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 数据集
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    if isswip == 1:
        baseOperation.swipe_up_custom(driver, 6 / 7, 5 / 7)
    baseOperation.findElementAndClick(driver, "text", dataset)
    baseOperation.findElementAndClick(driver, "text", "确定")


# 叠加数据
def setDesData(driver, datasource, dataset):
    ############叠加数据##########################################
    # 数据源
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 数据集
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", dataset)
    baseOperation.findElementAndClick(driver, "text", "确定")


# 设置结果数据并执行分析
def resultData(driver, datasource, dataset):
    ############结果数据##########################################
    # 数据源
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    # 下滑
    baseOperation.swipe_down_custom(driver, 5 / 7, 6 / 7)
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 数据集
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[6]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    baseOperation.input(driver, "class", "android.widget.EditText", dataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "text", "分析")
    time.sleep(15)


# 结果判断 islocation=1为记录集大于1个时执行
def resultCompare(self,driver, layer, count, islocation):
    ###########查看属性比对结果######################################
    baseOperation.findElementAndClick(driver, "text", "图层")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup[1]")
    # baseOperation.findElementAndClick(driver, "text",layer)
    baseOperation.findElementAndClick(driver, "text", "属性")
    if islocation == 1:
        baseOperation.findElementAndClick(driver, "text", "定位")
        baseOperation.findElementAndClick(driver, "text", "定位到末行")
    ele = baseOperation.findElement(driver, "text", count)
    self.assertIsNotNone(ele, "执行失败")

if __name__ == "__main__":
    print("执行")