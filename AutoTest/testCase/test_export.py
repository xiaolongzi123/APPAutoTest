import configparser
import unittest
import os
import os.path
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from testTools import baseOperation, baseApp
from pages import export
import time
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
cf = configparser.ConfigParser()
cf.read(root_dir+"/config/config.ini")  # 拼接得到config.ini文件的路径，直接使用
deviceName=cf.get('device','deviceName')


class MyTestCaseExport(unittest.TestCase):
    global driver
    @classmethod
    def setUpClass(cls):  # 固定写法，只在类执行之前执行一次！
        delcmd = ('rm -r /sdcard/iTablet/ExternalData/ExportData', '删除iTablet生成的数据文件夹')
        b=baseOperation.exeCmd(delcmd,deviceName)
        if b==False:
            mylogger.info("删除历史数据文件夹失败")
        else:
            mylogger.info("删除历史数据文件夹成功")

    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("我的")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")

    #导出影像数据集为tif文件
    def test_imgExportToTif(self):
        dataset="yufengIMG"
        export.datasetExport(self.driver,"China",dataset,"*.tif")
        time.sleep(120)
        export.compareResult(self,dataset+".tif")
    #导出影像数据集为img文件
    def test_imgExportToImg(self):
        dataset = "yufengIMG"
        export.datasetExport(self.driver,"China", dataset, "*.img")
        export.compareResult(self,dataset+".img")
    #导出栅格数据集为tif文件
    def test_gridExportToTif(self):
        dataset = "DEM"
        export.datasetExport(self.driver,"ChongQing",dataset,"*.tif")
        export.compareResult(self,dataset+".tif")
    #导出栅格数据集为img文件
    def test_gridExportToImg(self):
        dataset = "DEM"
        export.datasetExport(self.driver,"ChongQing", dataset, "*.img")
        export.compareResult(self,dataset+".img")
    # 导出CAD数据集为mif文件
    def test_cadExportToMif(self):
        dataset = "CAD"
        export.datasetExport(self.driver,"China", dataset, "*.mif")
        export.compareResult(self,dataset + ".mif")
    # 导出面数据集为shp文件
    def test_RegionExportToShp(self):
        dataset = "Region"
        export.datasetExport(self.driver,"China", dataset, "*.shp")
        export.compareResult(self,dataset + ".shp")
    # 导出面数据集为mif文件
    def test_RegionExportToMif(self):
        dataset = "Region"
        export.datasetExport(self.driver,"China", dataset, "*.mif")
        export.compareResult(self,dataset + ".mif")
    # 导出面数据集为kml文件
    def test_RegionExportToKml(self):
        dataset = "Region"
        export.datasetExport(self.driver,"China", dataset, "*.kml")
        export.compareResult(self,dataset + ".kml")
    # 导出面数据集为kmz文件
    def test_RegionExportToKmz(self):
        dataset = "Region"
        export.datasetExport(self.driver,"China", dataset, "*.kmz")
        export.compareResult(self,dataset + ".kmz")

    # 导出线数据集为shp文件
    def test_LineExportToShp(self):
        dataset = "Line"
        export.datasetExport(self.driver,"China", dataset, "*.shp")
        export.compareResult(self,dataset + ".shp")
    # 导出线数据集为mif文件
    def test_LineExportToMif(self):
        dataset = "Line"
        export.datasetExport(self.driver,"China", dataset, "*.mif")
        export.compareResult(self,dataset + ".mif")
    # 导出线数据集为kml文件
    def test_LineExportToKml(self):
        dataset = "Line"
        export.datasetExport(self.driver,"China", dataset, "*.kml")
        time.sleep(40)
        export.compareResult(self,dataset + ".kml")
    # 导出线数据集为kmz文件
    def test_LineExportToKmz(self):
        dataset = "Line"
        export.datasetExport(self.driver,"China", dataset, "*.kmz")
        time.sleep(40)
        export.compareResult(self,dataset + ".kmz")
    # 导出点数据集为shp文件
    def test_PointExportToShp(self):
        dataset = "Point"
        export.datasetExport(self.driver,"China", dataset, "*.shp")
        export.compareResult(self,dataset + ".shp")
    # 导出点数据集为mif文件
    def test_PointExportToMif(self):
        dataset = "Point"
        export.datasetExport(self.driver,"China", dataset, "*.mif")
        export.compareResult(self,dataset + ".mif")
    # 导出点数据集为kml文件
    def test_PointExportToKml(self):
        dataset = "Point"
        export.datasetExport(self.driver,"China", dataset, "*.kml")
        export.compareResult(self,dataset + ".kml")
    # 导出点数据集为kmz文件
    def test_PointExportToKmz(self):
        dataset = "Point"
        export.datasetExport(self.driver,"China", dataset, "*.kmz")
        export.compareResult(self,dataset + ".kmz")
    # 导出点数据集为gpx文件
    def test_PointExportToGpx(self):
        dataset = "Point"
        export.datasetExport(self.driver,"China", dataset, "*.gpx")
        export.compareResult(self,dataset + ".gpx")


if __name__ == '__main__':
    unittest.main()