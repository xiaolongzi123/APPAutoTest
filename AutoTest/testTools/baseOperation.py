# -*- coding: UTF-8 -*-
import configparser
import os
import time

import winsound
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from testTools import baseOperation
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
cf = configparser.ConfigParser()
cf.read(root_dir+"/config/config.ini")  # 拼接得到config.ini文件的路径，直接使用
deviceName=cf.get('device','deviceName')


# 打开app后允许所以的的权限
def always_allow(driver, number=6):
    for i in range(number):
        loc = ("xpath", "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            pass
#唤醒屏幕
def wake_up():
    cmd = 'adb shell input keyevent 26'
    isWakeup =os.system(cmd)
    if isWakeup == False:
        mylogger.info("唤醒屏幕失败")
    else:
        mylogger.info("唤醒屏幕成功")
#解锁
def un_lock():
    cmd = 'adb shell input keyevent 82'
    isWakeup = os.system(cmd)
    if isWakeup == False:
        mylogger.info("解锁失败")
    else:
        mylogger.info("解锁成功")


# 截屏
def cutPic(driver, picPath):
    # driver.save_screenshot("ex_theme1.png")
    driver.get_screenshot_as_file(picPath)

# 定位元素
def findElement(driver, type, value, timeout=15):
    try:
        if type == "id":
            # element = driver.find_element_by_id(value)
            element = WebDriverWait(driver, timeout, 1).until(EC.presence_of_element_located((By.ID, value)))
            return element
        elif type == "text":
            # element = driver.find_element_by_xpath("//*[@text='" + value + "']").implicitly_wait(5)
            element = WebDriverWait(driver, timeout, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@text='" + value + "']")))
            return element
        elif type == "xpath":
            element = WebDriverWait(driver, timeout, 5).until(EC.presence_of_element_located((By.XPATH, value)))
            return element
        elif type == "class":
            element = WebDriverWait(driver, timeout, 5).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            return element
    except BaseException:
        baseOperation.cutPic(driver, "../images/actual/" + time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  + ".png")
        print("页面未找到元素:"+value)
        mylogger.info("页面未找到元素:"+value)

# 点击元素
def findElementAndClick(driver, type, value):
    element = findElement(driver, type, value)
    element.click()
    time.sleep(1.5)

# 获取元素中心店坐标
def findElementCenterPt(driver, type, value):
    element = findElement(driver, type, value)
    ele_size=element.size
    # 元素的宽
    width = ele_size['width']
    # 元素的高
    height = ele_size['height']
    ele_coordinate = element.location
    # 元素左上角横坐标
    x = ele_coordinate['x']
    # 元素左上角纵坐标
    y = ele_coordinate['y']
    centerPt=[x + width / 2, y + height / 2]
    return centerPt

# 通过坐标点击元素
def clickByPt(driver,x1,y1,x2,y2):
    driver.tap([(x1, y1), (x2, y2)], 500)
    time.sleep(1.5)
# 通过坐标点击元素
def clickByPt1(driver,x1,y1):
    driver.tap([(x1, y1)], 500)
    time.sleep(1.5)

# 输入
def input(driver, type, value, text):
    element = findElement(driver, type, value)
    element.clear()
    element.send_keys(text)

# 获取屏幕尺寸
def get_size(driver):
    size = driver.get_window_size()
    return size

# 上滑
def swipe_to_up(driver):
    window_size = get_size(driver)
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

# 上滑
def swipe_up_custom(driver,heightRatio1,heightRatio2):
    window_size = get_size(driver)
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width / 2, height *heightRatio1, width / 2, height*heightRatio2, 500)
# 下滑
def swipe_down_custom(driver,heightRatio1,heightRatio2):
    window_size = get_size(driver)
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width / 2, height *heightRatio1, width / 2, height*heightRatio2, 500)
    time.sleep(2)

# 下滑
def swipe_to_down(driver):
    window_size = get_size(driver)
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

# 左滑
def swipe_to_left(driver):
    window_size = get_size(driver)
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

# 右滑
def swipe_to_right(driver):
    window_size = get_size(driver)
    width = window_size.get("width")
    height = window_size.get("height")
    driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

# 按下返回键
def back(driver):
    driver.keyevent(4)

# 按下home键
def home(driver):
    driver.keyevent(3)

# Copy文件操作
def copyfile_task(deviceid):
    # 删除BxxTest文件夹和*.zip文件
    delBxxTestcmd = ('rm -r /sdcard/iTablet', '删除iTablet文件夹')
    delzipcmd = ('rm -r /sdcard/*.*', '删除根目录下的旧版本文件')

    print(f'设备:{deviceid}正在执行删除BSTTest、XXXreports文件夹动作... ...')
    exeCmd(delBxxTestcmd, deviceid)
    exeCmd(delzipcmd, deviceid)

    copyfilepath = '../data/iTablet'
    print(f'设备：{deviceid}准备执行copy操作!')
    cmd = 'adb -s ' + deviceid + ' push ' + copyfilepath + ' /sdcard/iTablet/ExternalData'
    if os.system(cmd) == 0:
        print(f'设备：{deviceid} 文件copy成功！\n')
    else:
        winsound.Beep(800, 10000)
# 执行普通的cmd命令
def exeCmd(cmdInfo, deviceid):
    cmd = 'adb -s ' + deviceid + ' shell ' + cmdInfo[0]
    print(f'设备{deviceid}:exeCmd():{cmdInfo[1]}.')
    if os.system(cmd) != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    copyfile_task("28D6R17314002930")
