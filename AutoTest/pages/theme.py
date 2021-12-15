import os
import sys

from testTools import baseOperation, imgCompare
import time
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

def resultCompare(self, driver,mapName):
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
    time.sleep(5)
    # baseOperation.cutPic(driver, "../images/expect/theme/" + "ex_" + mapName + ".png")
    baseOperation.cutPic(driver, "../images/actual/theme/" + "ac_" + mapName + ".png")
    r = imgCompare.compare("../images/actual/theme/" + "ac_" + mapName + ".png",
                           "../images/expect/theme/" + "ex_" + mapName + ".png", 85)
    self.assertTrue(r, "对比失败")

def createMapAddLayer(driver, mapName, dadaset, ishide):
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
    baseOperation.findElementAndClick(driver, "xpath",
                                      "// android.view.ViewGroup / android.view.ViewGroup[3] / android.view.ViewGroup[2] / android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "// android.view.ViewGroup / android.view.ViewGroup[3] / android.view.ViewGroup[2] / android.widget.ImageView[1]")
    baseOperation.findElementAndClick(driver, "text", "工具")
    baseOperation.findElementAndClick(driver, "text", "全幅")
    if ishide == 1:
        baseOperation.findElementAndClick(driver, "text", "图层")
        baseOperation.findElementAndClick(driver, "xpath",
                                          "//android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]")
        baseOperation.findElementAndClick(driver, "text", "地图")

# is_swip表示需要上滑才能找到数据集
# is_swip1表示需要上滑才能找到字段
def makeTheme(driver, dadaset, themeType, is_swip, filed, colorTable):
    baseOperation.findElementAndClick(driver, "text", "专题图")
    baseOperation.findElementAndClick(driver, "text", themeType)
    baseOperation.findElementAndClick(driver, "text", dadaset)
    time.sleep(1)
    if is_swip == 1:
        baseOperation.swipe_up_custom(driver, 6 / 7, 4 / 7)
    baseOperation.findElementAndClick(driver, "text", filed)
    baseOperation.findElementAndClick(driver, "text", "风格")
    baseOperation.findElementAndClick(driver, "text", "颜色方案")
    baseOperation.findElementAndClick(driver, "text", colorTable)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)


def makeLableTheme(driver, dadaset, themeType, is_swip, filed, shape):
    baseOperation.findElementAndClick(driver, "text", "专题图")
    baseOperation.findElementAndClick(driver, "text", themeType)
    baseOperation.findElementAndClick(driver, "text", dadaset)
    time.sleep(1)
    if is_swip == 1:
        baseOperation.swipe_up_custom(driver, 6 / 7, 4 / 7)
    baseOperation.findElementAndClick(driver, "text", filed)
    time.sleep(2)
    baseOperation.findElementAndClick(driver, "text", "风格")
    time.sleep(2)
    baseOperation.findElementAndClick(driver, "text", "背景形状")
    baseOperation.findElementAndClick(driver, "text", shape)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)


def makeRangeLableTheme(driver, dadaset, themeType, is_swip, filed1, filed2):
    baseOperation.findElementAndClick(driver, "text", "专题图")
    baseOperation.findElementAndClick(driver, "text", themeType)
    baseOperation.findElementAndClick(driver, "text", dadaset)
    time.sleep(1)
    if is_swip == 1:
        baseOperation.swipe_up_custom(driver, 6 / 7, 4 / 7)
    baseOperation.findElementAndClick(driver, "text", filed1)
    baseOperation.findElementAndClick(driver, "text", "风格")
    time.sleep(2)
    baseOperation.findElementAndClick(driver, "text", "表达式")
    baseOperation.findElementAndClick(driver, "text", filed2)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)


def makeStatisticsTheme(driver, themeType, dataset, filed1, filed2, filed3, colorTable):
    baseOperation.findElementAndClick(driver, "text", "专题图")
    baseOperation.findElementAndClick(driver, "text", themeType)
    baseOperation.findElementAndClick(driver, "text", dataset)
    time.sleep(1)
    baseOperation.findElementAndClick(driver, "text", filed1)
    baseOperation.findElementAndClick(driver, "text", filed2)
    baseOperation.findElementAndClick(driver, "text", filed3)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)
    baseOperation.findElementAndClick(driver, "text", "是")
    baseOperation.findElementAndClick(driver, "text", "风格")
    baseOperation.findElementAndClick(driver, "text", "颜色方案")
    baseOperation.findElementAndClick(driver, "text", colorTable)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)


def makeHeatOrGridTheme(driver, dadaset, themeType, colorTable):
    baseOperation.findElementAndClick(driver, "text", "专题图")
    baseOperation.findElementAndClick(driver, "text", themeType)
    baseOperation.findElementAndClick(driver, "text", dadaset)
    time.sleep(1)
    baseOperation.findElementAndClick(driver, "text", "风格")
    baseOperation.findElementAndClick(driver, "text", "颜色方案")
    baseOperation.findElementAndClick(driver, "text", colorTable)
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)
    if themeType == "栅格单值专题图" or themeType == "栅格分段专题图":
        baseOperation.findElementAndClick(driver, "text", "图层")
        baseOperation.findElementAndClick(driver, "xpath",
                                          "//android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.ImageView[1]")
        baseOperation.findElementAndClick(driver, "text", "全幅显示本图层")
        time.sleep(8)


def makeDotOrSymbolTheme(driver, dadaset, themeType, filed):
    baseOperation.findElementAndClick(driver, "text", "专题图")
    baseOperation.findElementAndClick(driver, "text", themeType)
    baseOperation.findElementAndClick(driver, "text", dadaset)
    baseOperation.findElementAndClick(driver, "text", filed)
    time.sleep(1)
    baseOperation.findElementAndClick(driver, "text", "风格")
    baseOperation.findElementAndClick(driver, "text", "颜色")
    baseOperation.findElementAndClick(driver, "xpath",
                                      "//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[4]")
    baseOperation.clickByPt(driver, 970, 2280, 1033, 2400)

if __name__ == "__main__":
    print("执行")