import os
import sys
from testTools import baseOperation, imgCompare
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

def createDataset(driver, datasource,dadasetType,datasetName):
    baseOperation.findElementAndClick(driver, "text", "数据")
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]")
    baseOperation.findElementAndClick(driver, "text", "新建数据集")
    baseOperation.findElementAndClick(driver, "text", dadasetType)
    baseOperation.input(driver, "class", "android.widget.EditText",datasetName)
    baseOperation.findElementAndClick(driver, "text", "创建")
    time.sleep(2)
    ele=baseOperation.findElement(driver,"text",datasetName)
    return ele
def delDataset(driver,datasource,datasetName):
    baseOperation.findElementAndClick(driver, "text", "数据")
    baseOperation.findElementAndClick(driver, "text", datasource)
    # 获取数据集的中心点坐标并通过相对位置点击菜单
    pt = baseOperation.findElementCenterPt(driver, "text", datasetName)
    baseOperation.clickByPt1(driver, 1000, pt[1])
    baseOperation.findElementAndClick(driver, "text", "删除数据集")
    baseOperation.findElementAndClick(driver, "text", "确定")
    ele=baseOperation.findElement(driver,"text","删除成功")
    return ele





if __name__ == "__main__":
    print("111")