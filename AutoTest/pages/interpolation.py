import os
import sys
from testTools import baseOperation, imgCompare
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

def createMapAddLayer(driver, mapName, dadaset):
    baseOperation.findElementAndClick(driver, "text", "开始")
    baseOperation.findElementAndClick(driver, "text", "新建地图")
    baseOperation.findElementAndClick(driver, "text", "不保存")
    baseOperation.input(driver, "class", "android.widget.EditText", mapName)
    baseOperation.findElementAndClick(driver, "text", "确定")
    time.sleep(5)
    baseOperation.findElementAndClick(driver, "text", "图层")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", "地图")
    baseOperation.findElementAndClick(driver, "text", "添加")
    baseOperation.findElementAndClick(driver, "text", "ChongQing")

    baseOperation.findElementAndClick(driver, "text", dadaset)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)
    baseOperation.findElementAndClick(driver, "text", "是")
    for i in range(3):
        baseOperation.findElementAndClick(driver, "xpath",
                                      "// android.view.ViewGroup / android.view.ViewGroup[3] / android.view.ViewGroup[2] / android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", "工具")
    baseOperation.findElementAndClick(driver, "text", "全幅")

def interpolationAnalyst(driver ,type,srcDatasource ,srcDataset ,filed,desDatasource ,desDataset,radius,sum):
    baseOperation.findElementAndClick(driver, "text", "分析")
    baseOperation.findElementAndClick(driver, "text", "插值分析")
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
    if "吕金" in type:
        baseOperation.swipe_up_custom(driver, 6 / 7, 5 / 7)
    baseOperation.findElementAndClick(driver, "text", type)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "xpath","//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", srcDatasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "xpath", "//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver, "text", srcDataset)
    baseOperation.findElementAndClick(driver, "text" ,"确定")
    baseOperation.findElementAndClick(driver, "xpath","//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]")
    baseOperation.swipe_up_custom(driver, 6 / 7, 5 / 7)
    baseOperation.swipe_up_custom(driver, 6 / 7, 5 / 7)
    baseOperation.findElementAndClick(driver, "text", filed)
    baseOperation.findElementAndClick(driver, "text", "确定")
    # 结果数据源数据集
    baseOperation.findElementAndClick(driver,"xpath","//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[6]/android.view.ViewGroup[1]")
    baseOperation.findElementAndClick(driver,"text",desDatasource)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "xpath","//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.view.ViewGroup[1]")
    baseOperation.input(driver, "xpath","//android.widget.EditText[@content-desc='输入框']", desDataset)
    baseOperation.findElementAndClick(driver, "text", "确定")
    baseOperation.findElementAndClick(driver, "text", "下一步")
    if type=="距离反比权重":
        print("默认参数")
        # baseOperation.input(driver,"xpath","//android.widget.EditText[@text='2']","4")
    elif type=="样条":
        baseOperation.input(driver,"xpath","//android.widget.EditText[@text='0']",radius)
        baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='12']", sum)
        baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='40']", "50")
        baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='0.1']", "0.2")
    else:
        baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='0']", radius)
        baseOperation.input(driver, "xpath", "//android.widget.EditText[@text='12']", sum)
    baseOperation.findElementAndClick(driver,"text","分析")
    time.sleep(5)

def resultCompare(self, driver, mapName):
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
    time.sleep(5)
    baseOperation.cutPic(driver, "../images/expect/interpolation/" + "ex_" + mapName + ".png")
    # baseOperation.cutPic(driver, "../images/actual/interpolation/" + "ac_" + mapName + ".png")
    # r = imgCompare.compare("../images/actual/interpolation/" + "ac_" + mapName + ".png",
    #                        "../images/expect/interpolation/" + "ex_" + mapName + ".png", 85)
    # self.assertTrue(r, "对比失败")
    # self.assertTrue(r, "对比失败")

if __name__ == "__main__":
    print("111")