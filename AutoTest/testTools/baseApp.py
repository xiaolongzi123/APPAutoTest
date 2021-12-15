# -*- coding: UTF-8 -*-
from appium import webdriver

from testTools import baseOperation
import time
import configparser
import os

root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
cf = configparser.ConfigParser()
cf.read(root_dir+"/config/config.ini")  # 拼接得到config.ini文件的路径，直接使用
deviceName=cf.get('device','deviceName')
print(deviceName)

def startApp1():
    desired_caps = {}
    desired_caps['noReset'] = 'true' # 是否重新安装
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['platformName'] = 'Android'  # 平台 名称
    desired_caps['platformVersion'] = '11'  # Android 版本号
    # desired_caps['deviceName'] = '7xnv7pa6kfbycqbm'  # 设备名称（cmd -- adb devices 确保手机连接电脑正常）
    desired_caps['deviceName'] = deviceName
    desired_caps['appPackage'] = 'com.supermap.itablet'
    desired_caps['appActivity'] = 'com.supermap.itablet.MainActivity'  # 要打开的app入口Activity
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver
# 打开app并进入指定模块
def startApp(module):
    desired_caps = {}
    desired_caps['noReset'] = 'true' # 是否重新安装
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['platformName'] = 'Android'  # 平台 名称
    desired_caps['platformVersion'] = '11'  # Android 版本号
    desired_caps['deviceName'] = '7xnv7pa6kfbycqbm'  # 设备名称（cmd -- adb devices 确保手机连接电脑正常 28D6R17314002930/7xnv7pa6kfbycqbm）
    desired_caps['appPackage'] = 'com.supermap.itablet'
    desired_caps['appActivity'] = 'com.supermap.itablet.MainActivity'  # 要打开的app入口Activity
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    time.sleep(5)
    baseOperation.swipe_to_up(driver)
    driver.implicitly_wait(5)
    baseOperation.findElementAndClick(driver, "text", module)
    time.sleep(5)
    return driver

def closeApp(driver):
    """关闭应用"""
    driver.close_app()
    driver.quit()


if __name__ == '__main__':
    startApp("数据处理")