# # !/user/bin/python
# # -*- coding:utf-8 -*-
#
# import os
# from multiprocessing import Pool
# from time import sleep
# import winsound
#
#
# # 重连动作
# def reconnectAction(deviceid):
#     devlist = getdevlist()
#     print(f'设备{deviceid}正在尝试重连.')
#     id = 1
#     while deviceid not in devlist:
#         print(f'第{id}次 ', end=' ')
#         devlist = getdevlist()
#         id = id + 1
#     print(f'\n设备{deviceid}重新建立连接成功.')
#     sleep(1)
#
#
# # 执行普通的cmd命令
# def exeCmd(cmdInfo, deviceid):
#     cmd = 'adb -s ' + deviceid + ' shell ' + cmdInfo[0]
#     print(f'设备{deviceid}:exeCmd():{cmdInfo[1]}.')
#     if os.system(cmd) != 0:
#         return False
#     else:
#         return True
#
#
# # 按键动作
# def pressKeyevent(keycodeInfo, deviceid=''):
#     cmd = 'adb -s ' + deviceid + ' shell input keyevent ' + keycodeInfo[0]
#     print(f'设备{deviceid}:pressKeyevent():{keycodeInfo[1]}.')
#     if os.system(cmd) != 0:
#         return False
#     else:
#         return True
#
#
# # 点击屏幕的动作
# def clickScreen(positionInfo, deviceid=''):
#     cmd = 'adb -s ' + deviceid + ' shell input tap ' + positionInfo[0]
#     print(f'设备{deviceid}:clickScreen():{positionInfo[1]}.')
#     if os.system(cmd) != 0:
#         return False
#     else:
#         return True
#
#
# # 滑动屏幕的动作
# def swipeScreen(positionInfo, deviceid=''):
#     cmd = 'adb -s ' + deviceid + ' shell input swipe ' + positionInfo[0]
#     print(f'设备{deviceid}:swipeScreen():{positionInfo[1]}.')
#     if os.system(cmd) != 0:
#         return False
#     else:
#         return True
#
#
# # 运行app
# def launchApp(appactivityInfo, deviceid=''):
#     cmd = 'adb -s ' + deviceid + ' shell am start ' + appactivityInfo[0]
#     print(f'设备{deviceid}:launchApp():{appactivityInfo[1]}.')
#     if os.system(cmd) != 0:
#         return False
#     else:
#         return True
#
#
# # 获取username,  如chinaren
# def getusername():
#     namelist = os.popen('echo %username%').readlines()
#     username = namelist[0].replace("\n", "")
#     # 获取当前的username
#     return username
#
#
# # 获取设备id列表
# def getdevlist():
#     devlist = []
#     connectfile = os.popen('adb devices')
#     list = connectfile.readlines()
#     # print(list)
#     for i in range(len(list)):
#         if list[i].find('\tdevice') != -1:
#             temp = list[i].split('\t')
#             devlist.append(temp[0])
#     return devlist
#
#
# # 返回指定txt文件的第一行内容，主要是为了获取待Copy的文件名
# def getspecifytxtfilefirstline(txtfilename):
#     '''
#     返回指定txt文件的第一行内容
#     txt档要求与py档在同一目录
#     '''
#     currunningpyfilepath = os.path.split(os.path.realpath(__file__))[0]
#     copyfile2phoneTXT = currunningpyfilepath + '\\' + txtfilename
#     while True:
#         if os.path.exists(copyfile2phoneTXT) == True:
#             with open(copyfile2phoneTXT, 'r') as f:
#                 filename = f.readline()
#                 if filename == '':
#                     print('txt档为空,输入重新写入待copy文件名.')
#                     with open(copyfile2phoneTXT, 'w') as f:
#                         fileStr = input('请输入你要copy文件的完整文件名\n(建议直接拖入文件至这里，会自动获取写入txt档)：')
#                         filenamelist = fileStr.split('\\')
#                         filename = filenamelist[len(filenamelist) - 1]
#                         f.write(filename)
#                         print('输入的文件名已写入.')
#                         return filename
#                 else:
#                     return filename
#         else:
#             print('copyfile2phone.txt文件不存在，将在当前目录新建一个此txt文件！')
#             with open(copyfile2phoneTXT, 'w') as f:
#                 print('copyfile2phone.txt文件新建成功!')
#                 fileStr = input('请输入你要copy文件的完整文件名\n(建议直接拖入文件至这里，会自动获取写入txt档)：')
#                 filenamelist = fileStr.split('\\')
#                 filename = filenamelist[len(filenamelist) - 1]
#                 f.write(filename)
#                 print('输入的文件名已写入.')
#                 return filename
#
#
# # 测试Adb连接性
# def checkAdbConnectability(flag=0):
#     '''
#     flag =0时，当连接正常时返回True(default)
#     flag!=0时，直接打印出结果
#     '''
#     connectstring = '''ADB连接失败, 请check以下项:
#     1. 是否有连接上手机？请连接上手机选并重新check连接性!
#     2. 是否有开启"开发者选项\\USB调试模式"?\n'''
#     connectinfolist = getdevlist()
#
#     if len(connectinfolist) == 0:
#         return False
#     if len(connectinfolist) == 1:
#         if flag != 0:
#             print('连接正常')
#             print(f'设备SN: {connectinfolist[0]}')
#         else:
#             return True
#     if len(connectinfolist) >= 2:
#         print('连接正常，当前有连接多台设备. ')
#         for i in range(len(connectinfolist)):
#             print(f'设备{i + 1} SN: {connectinfolist[i]}')
#         return True
#
#
# def isAwaked(deviceid=''):
#     '''
#     判断的依据是'    mAwake=false\n'
#     '''
#     if deviceid == '':
#         cmd = 'adb shell dumpsys window policy'
#     else:
#         cmd = 'adb -s ' + deviceid + ' shell dumpsys window policy'
#     screenAwakevalue = '    mAwake=true\n'
#     allList = os.popen(cmd).readlines()
#     if screenAwakevalue in allList:
#         return True
#     else:
#         return False
#
#
# # Copy文件操作
# def copyfile_task(deviceid, filename):
#     # 删除BxxTest文件夹和*.zip文件
#     delBxxTestcmd = ('rm -r /sdcard/iTablet', '删除iTablet文件夹')
#     delzipcmd = ('rm -r /sdcard/*.*', '删除根目录下的旧版本文件')
#
#     print(f'设备:{deviceid}正在执行删除BSTTest、XXXreports文件夹动作... ...')
#     exeCmd(delBxxTestcmd, deviceid)
#     exeCmd(delzipcmd, deviceid)
#
#     copyfilepath = '../data/'
#     print(f'设备：{deviceid}准备执行copy操作!')
#     cmd = 'adb -s ' + deviceid + ' push ' + copyfilepath + ' /sdcard/'
#     if os.system(cmd) == 0:
#         print(f'设备：{deviceid} 文件copy成功！\n')
#     else:
#         winsound.Beep(800, 10000)
#
#     # 打开filemanager application
#     print('正在开启filemanager应用... ...')
#     isexistCmd = ('ps | findstr filemanager', '查看filemanager app是否已开启')
#     closeappCmd = ('am force-stop com.android.filemanager', '关闭filemanager app')
#     runappCmd = ('am start com.android.filemanager/.FileManagerListActivity', '开启filemanager app')
#
#     if exeCmd(isexistCmd, deviceid) == True:
#         print(f'设备{deviceid}的filemanager app之前已开启.将关闭再开启')
#         exeCmd(closeappCmd, deviceid)
#         # exeCmd(runappCmd, deviceid)
#         if exeCmd(runappCmd, deviceid) == False:
#             reconnectAction(deviceid)
#             exeCmd(runappCmd, deviceid)
#     else:
#         print('filemanager app已开启.')
#         if exeCmd(runappCmd, deviceid) == False:
#             reconnectAction(deviceid)
#             exeCmd(runappCmd, deviceid)
#
#     # 点亮手机屏幕开始升级
#     lightCmd = ('26', '点亮屏幕')
#     unlockscreenCmd = ('380 1300 380 300', '屏幕解锁')
#     swipescreen = ('380 1300 380 300', '上滑屏幕')
#     clickload = ('400 1300', '在文件列表中点击load')
#     clickupdata = ('509 1330', '点击升级按键')
#     if isAwaked(deviceid) == False:
#         pressKeyevent(lightCmd, deviceid)
#     swipeScreen(unlockscreenCmd, deviceid)
#     sleep(0.5)
#     # 因为在解锁后设备会大概率的断开一下，故如果断线则需要等待重连
#     if swipeScreen(swipescreen, deviceid) == False:
#         reconnectAction(deviceid)
#         swipeScreen(swipescreen, deviceid)
#     swipeScreen(swipescreen, deviceid)
#     sleep(0.5)
#     if clickScreen(clickload, deviceid) == False:
#         reconnectAction(deviceid)
#         clickScreen(clickload, deviceid)
#     sleep(0.5)
#     if clickScreen(clickupdata, deviceid) == False:
#         reconnectAction(deviceid)
#         clickScreen(clickupdata, deviceid)
#     # 当所有操作完成时，手机会不断的闪屏+PC会不断的'嘟嘟'提醒,直到设备断开
#     print(f'\n当前设备{deviceid} copy动作已完成... 请拨线... ')
#     temp = getdevlist()
#     while deviceid in temp:
#         # os.popen('adb -s ' + deviceid + ' shell input keyevent 26')
#         winsound.Beep(500, 500)
#         temp = getdevlist()
#
#
# def main():
#     print('---------重要提示---------')
#     print('请将待Copy文件放置在桌面再进行操作\n\n')
#
#     connectdevice = input('请输入每次要同时下载的设备数（注意：如果要改变设备同时下载的设备数，则需要关闭脚本重新run）:')
#     number = int(connectdevice.strip())
#
#     while True:
#         lists = getdevlist()
#         devnum = len(lists)
#         id = 1
#         tempdevlist = getdevlist()
#         if devnum < number:
#             print(f'\n设备未全部识别，应识别{number}台设备!\n当前已识别{devnum}台设备,请连接设备并等待识别:\n\n')
#             for i in range(devnum):
#                 print(f'设备{id}: {lists[i]}')
#                 id = id + 1
#         while devnum < number:
#             lists = getdevlist()
#             curnum = len(lists)
#             if curnum > devnum:
#                 for i in range(len(lists)):
#                     if lists[i] not in tempdevlist:
#                         print(f'设备{id}: {lists[i]}')
#                         id = id + 1
#                         tempdevlist = getdevlist()
#                 devnum = curnum
#
#         print(f'\n所有设备已全部识别!当前有连接{len(getdevlist())}台设备.\n\n')
#
#         while True:
#             copyfilename = getspecifytxtfilefirstline('copyfile2phone.txt')
#             if checkAdbConnectability() == True:
#                 copyfilepath = 'C:\\Users\\' + getusername() + '\\Desktop\\' + copyfilename
#                 if os.path.isfile(copyfilepath) == True:
#                     devicelist = getdevlist()
#                     print(f'要copy的文件名:{copyfilename}')
#                     print('COPY文件准备中，请稍候... ...\n')
#                     p = Pool(4)
#                     for i in range(len(devicelist)):
#                         p.apply_async(copyfile_task, args=(devicelist[i], copyfilename))
#                     p.close()
#                     p.join()
#                     # 等待的设备断开
#                     devnum = len(getdevlist())
#                     while devnum != 0:
#                         devnum = len(getdevlist())
#                     print('\n所有设备已断开!\n\n\n请连接其它手机进行下一轮Copy... ...')
#                 else:
#                     print('TXT档中指定的文件名不存在TXT档将被删除并新建，需要重新输入文件名:')
#                     # 删除文件
#                     curfilepath = os.path.split(os.path.realpath(__file__))[0]
#                     TXTfilepath = curfilepath + '\\' + 'copyfile2phone.txt'
#                     os.remove(TXTfilepath)
#                     print('TXT档被删除成功')
#             else:
#                 break
#
#             # 主程序
#
#
# if __name__ == '__main__':
#     main()