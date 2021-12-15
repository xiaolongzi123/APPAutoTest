import cv2
import os
import sys

from testTools.testLog import Logger

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

import shutil
# import numpy as np

import cv2 as cv
print(cv.__file__)
mylogger=Logger(logger='TestMyLog').getlog()
#均值哈希算法
def aHash(img):
    #缩放为8*8
    img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    #转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s=0
    hash_str=''
    #遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s=s+gray[i,j]
    #求平均灰度
    avg=s/64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if  gray[i,j]>avg:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str

#差值感知算法
def dHash(img):
    #缩放8*8
    img=cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    #转换灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
    #每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if   gray[i,j]>gray[i,j+1]:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str

#Hash值对比
def cmpHash(hash1,hash2):
    n=100
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    #遍历判断
    for i in range(len(hash1)):
        #不相等则n计数+1，n最终为相似度
        if hash1[i]!=hash2[i]:
            n=n-1
    return n

def compare(img1Path,img2Path,pecent):
    img1 = cv2.imread(img1Path)
    img2 = cv2.imread(img2Path)
    hash1 = aHash(img1)
    hash2 = aHash(img2)
    print(hash1)
    print(hash2)
    n = cmpHash(hash1, hash2)
    print('均值哈希算法相似度：', n)
    mylogger.info('均值哈希算法相似度：'+str(n))
    if n<pecent:
        shutil.move(img1Path, "../images/differ")
        return False
    else:
        return True
        print("图片对比成功")


# img1=cv2.imread('../images/walk_m.jpg')
# img2=cv2.imread('../images/walks1.jpg')
#
# # img1=cv2.imread('../images/login2.png')
# # img2=cv2.imread('../images/login1.png')
# hash1= aHash(img1)
# hash2= aHash(img2)
# print(hash1)
# print(hash2)
# n=cmpHash(hash1,hash2)
# print('均值哈希算法相似度：',n)
#
#
# hash1= dHash(img1)
# hash2= dHash(img2)
# print(hash1)
# print(hash2)
# n=cmpHash(hash1,hash2)
# print('差值哈希算法相似度：',n)