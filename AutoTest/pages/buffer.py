import os
import sys

from testTools import baseOperation
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

# type=1为平头缓冲
# ismerge=1为合并缓冲区
def setBufferparaAndAnalyst(driver, datasource, dataset, type, distance, ismerge, resultdatasource, resultdataset):
    baseOperation.findElementAndClick(driver, "xpath",
                                      "// android.view.ViewGroup / android.view.ViewGroup[3] / android.view.ViewGroup[2] / android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", "分析")
    baseOperation.findElementAndClick(driver, "text", "单缓冲区")
    # 数据源
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 数据集
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", dataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 类型
    if type == 1:
        baseOperation.findElementAndClick(driver, "xpath",
                                          "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    # 缓冲半径单缓冲
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup[1]")
    baseOperation.input(driver, "class", "android.widget.EditText", distance)
    baseOperation.findElementAndClick(driver, "text", "确定")

    # 合并缓冲区
    if ismerge == 1:
        baseOperation.findElementAndClick(driver, "text", "关闭")
    # 结果
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[11]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", resultdatasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[12]/android.view.ViewGroup[1]")
    baseOperation.input(driver, "class", "android.widget.EditText", resultdataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "text", "分析")
    time.sleep(15)


# type=1为平头缓冲
# ismerge=1为合并缓冲区
####多重缓冲区
def setMulBufferparaAndAnalyst(driver, datasource, dataset, type, startDistance, endDistance, step, ismerge,
                               resultdatasource,
                               resultdataset):
    baseOperation.findElementAndClick(driver, "xpath",
                                      "// android.view.ViewGroup / android.view.ViewGroup[3] / android.view.ViewGroup[2] / android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", "分析")
    baseOperation.findElementAndClick(driver, "text", "多重缓冲区")
    # 数据源
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 数据集
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", dataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 类型
    if type == 1:
        baseOperation.findElementAndClick(driver, "xpath",
                                          "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    # 缓冲半径
    baseOperation.findElementAndClick(driver, "text", "去设置")
    baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='10']", startDistance)
    baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='30']", endDistance)
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    baseOperation.input(driver, "xpath",
                        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.EditText[1]",
                        step)
    baseOperation.findElementAndClick(driver, "text", "确定")

    # 合并缓冲区
    if ismerge == 1:
        baseOperation.findElementAndClick(driver, "text", "关闭")
    # 结果
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[11]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", resultdatasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[12]/android.view.ViewGroup[1]")
    baseOperation.input(driver, "class", "android.widget.EditText", resultdataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "text", "分析")
    time.sleep(15)


# islocation == 1针对数据记录数>1的结果
def resultCompare(self,driver, count, islocation):
    ###########查看属性比对结果######################################
    baseOperation.findElementAndClick(driver, "text", "图层")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", "属性")
    if islocation == 1:
        baseOperation.findElementAndClick(driver, "text", "定位")
        baseOperation.findElementAndClick(driver, "text", "定位到末行")
    ele = baseOperation.findElement(driver, "text", count)
    self.assertIsNotNone(ele, "执行失败")

if __name__ == "__main__":
    print("执行")
