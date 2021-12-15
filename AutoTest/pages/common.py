import os
import sys
from testTools import baseOperation, imgCompare
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

def delAllDataset(driver, datasource):
    baseOperation.findElementAndClick(driver, "text", "数据")
    baseOperation.findElementAndClick(driver, "text", datasource)
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]")
    baseOperation.findElementAndClick(driver, "text", "批量操作")
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", "批量删除")
    baseOperation.findElementAndClick(driver, "text", "确定")
    time.sleep(2)


if __name__ == "__main__":
    print("111")