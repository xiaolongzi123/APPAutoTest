import unittest
import os
import sys
from pages import theme
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from testTools import baseOperation, baseApp,imgCompare
import time
from testTools.testLog import Logger
mylogger=Logger(logger='TestMyLog').getlog()


class MyTestCaseTheme(unittest.TestCase):
    global driver

    def setUp(self):  # 固定写法，在每次方法之前执行，注意，是每次！
        self.driver = baseApp.startApp("专题制图")
        mylogger.info("开始执行用例")
        time.sleep(3)

    def tearDown(self):  # 固定写法，在每次方法之后执行，注意，是每次！
        baseOperation.home(self.driver)
        baseApp.closeApp(self.driver)
        mylogger.info("用例执行结束")

    #点数据单值专题图
    def test_theme1(self):
        mapName="ThemeUniqueMap1"
        dataset="风景名胜"
        theme.createMapAddLayer(self.driver,mapName,dataset,0)
        theme.makeTheme(self.driver,dataset,"单值风格",1,"ColorID","BC_Orange")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据单值专题图
    def test_theme2(self):
        mapName = "ThemeUniqueMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 1)
        theme.makeTheme(self.driver,dataset, "单值风格", 0, "ColorID", "BA_Blue")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据单值专题图
    def test_theme3(self):
        mapName = "ThemeUniqueMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeTheme(self.driver,dataset, "单值风格", 0, "ColorID", "BD_Pink")
        theme.resultCompare(self,self.driver,mapName)

    #点数据分段专题图
    def test_theme4(self):
        mapName = "ThemeRangeMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeTheme(self.driver,dataset, "分段风格", 1, "ColorID", "CA_Oranges")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据分段专题图
    def test_theme5(self):
        mapName = "ThemeRangeMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 1)
        theme.makeTheme(self.driver,dataset, "分段风格", 0, "ColorID", "CA_Oranges")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据分段专题图
    def test_theme6(self):
        mapName = "ThemeRangeMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeTheme(self.driver,dataset, "分段风格", 0, "ColorID", "CA_Oranges")
        theme.resultCompare(self,self.driver,mapName)

    #点数据统一标签专题图
    def test_theme7(self):
        mapName = "ThemeLableMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeLableTheme(self.driver,dataset, "统一标签", 0, "NAME", "圆角矩形")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据统一标签专题图
    def test_theme8(self):
        mapName = "ThemeLableMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeLableTheme(self.driver,dataset, "统一标签", 0, "AD_CODE", "矩形")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据统一标签专题图
    def test_theme9(self):
        mapName = "ThemeLableMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeLableTheme(self.driver,dataset, "统一标签", 0, "NAME", "椭圆")
        theme.resultCompare(self,self.driver,mapName)

    #点数据单值标签专题图
    def test_theme10(self):
        mapName = "ThemeLableUniqueMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeTheme(self.driver,dataset, "单值标签", 0, "NAME", "BD_Pink")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据单值标签专题图
    def test_theme11(self):
        mapName = "ThemeLableUniqueMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeTheme(self.driver,dataset, "单值标签", 0, "AD_CODE", "BD_Pink")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据单值标签专题图
    def test_theme12(self):
        mapName = "ThemeLableUniqueMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeTheme(self.driver,dataset, "单值标签", 0, "NAME", "BD_Pink")
        theme.resultCompare(self,self.driver,mapName)

    #点数据分段标签专题图
    def test_theme13(self):
        mapName = "ThemeRangeLableMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeRangeLableTheme(self.driver,dataset, "分段标签", 1, "ColorID", "NAME")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据分段标签专题图
    def test_theme14(self):
        mapName = "ThemeRangeLableMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeRangeLableTheme(self.driver,dataset, "分段标签", 0, "ColorID", "AD_CODE")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据分段标签专题图
    def test_theme15(self):
        mapName = "ThemeRangeLableMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeRangeLableTheme(self.driver,dataset, "分段标签", 0, "ColorID", "NAME")
        theme.resultCompare(self,self.driver,mapName)
    #点数据制作面积图
    def test_theme16(self):
        mapName = "ThemeGraphAreaMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "面积图",dataset, "pop2019", "pop2020", "pop2021","CD_Concise")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作面积图
    def test_theme17(self):
        mapName = "ThemeGraphAreaMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "面积图",dataset, "pop2019", "pop2020", "pop2021","CD_Concise")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作面积图
    def test_theme18(self):
        mapName = "ThemeGraphAreaMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "面积图",dataset, "pop2019", "pop2020", "pop2021","CD_Concise")
        theme.resultCompare(self,self.driver,mapName)
    #点数据制作阶梯图
    def test_theme19(self):
        mapName = "ThemeGraphStepMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "阶梯图",dataset, "pop2019", "pop2020", "pop2021","CD_Concise")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作阶梯图
    def test_theme20(self):
        mapName = "ThemeGraphStepMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "阶梯图",dataset, "pop2019", "pop2020", "pop2021","CD_Concise")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作阶梯图
    def test_theme21(self):
        mapName = "ThemeGraphStepMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "阶梯图",dataset, "pop2019", "pop2020", "pop2021","CD_Concise")
        theme.resultCompare(self,self.driver,mapName)
    #点数据制作折线图
    def test_theme22(self):
        mapName = "ThemeGraphLineMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "折线图",dataset, "pop2019", "pop2020", "pop2021","CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作折线图
    def test_theme23(self):
        mapName = "ThemeGraphLineMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "折线图",dataset, "pop2019", "pop2020", "pop2021","CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作折线图
    def test_theme24(self):
        mapName = "ThemeGraphLineMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver, "折线图",dataset, "pop2019", "pop2020", "pop2021","CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 点数据制作散点图
    def test_theme25(self):
        mapName = "ThemeGraphPointMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"散点图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作散点图
    def test_theme26(self):
        mapName = "ThemeGraphPointMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"散点图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作散点图
    def test_theme27(self):
        mapName = "ThemeGraphPointMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"散点图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
   # 点数据制作柱状图
    def test_theme28(self):
        mapName = "ThemeGraphBarMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"柱状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作柱状图
    def test_theme29(self):
        mapName = "ThemeGraphBarMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"柱状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作柱状图
    def test_theme30(self):
        mapName = "ThemeGraphBarMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"柱状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 点数据制作三维柱状图
    def test_theme31(self):
        mapName = "ThemeGraphBar3DMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维柱状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据三维制作柱状图
    def test_theme32(self):
        mapName = "ThemeGraphBar3DMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维柱状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作三维柱状图
    def test_theme33(self):
        mapName = "ThemeGraphBar3DMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维柱状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
   # 点数据制作饼状图
    def test_theme34(self):
        mapName = "ThemeGraphPieMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"饼状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作饼状图
    def test_theme35(self):
        mapName = "ThemeGraphPieMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"饼状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作饼状图
    def test_theme36(self):
        mapName = "ThemeGraphPieMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"饼状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 点数据制作三维饼状图
    def test_theme37(self):
        mapName = "ThemeGraphPie3DMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维饼状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作三维饼状图
    def test_theme38(self):
        mapName = "ThemeGraphPie3DMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维饼状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作饼三维状图
    def test_theme39(self):
        mapName = "ThemeGraphPie3DMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维饼状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
   # 点数据制作玫瑰图
    def test_theme40(self):
        mapName = "ThemeGraphRoseMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"玫瑰图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作玫瑰图
    def test_theme41(self):
        mapName = "ThemeGraphRoseMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"玫瑰图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作玫瑰图
    def test_theme42(self):
        mapName = "ThemeGraphRoseMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"玫瑰图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
   # 点数据制作三维玫瑰图
    def test_theme43(self):
        mapName = "ThemeGraphRose3DMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维玫瑰图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作三维玫瑰图
    def test_theme44(self):
        mapName = "ThemeGraphRose3DMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维玫瑰图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作三维玫瑰图
    def test_theme45(self):
        mapName = "ThemeGraphRose3DMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维玫瑰图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 点数据制作堆叠图
    def test_theme46(self):
        mapName = "ThemeGraphStackBarMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"堆叠图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作堆叠图
    def test_theme47(self):
        mapName = "ThemeGraphStackBarMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"堆叠图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作堆叠图
    def test_theme48(self):
        mapName = "ThemeGraphStackBarMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"堆叠图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 点数据制作三维堆叠图
    def test_theme49(self):
        mapName = "ThemeGraphStackBar3DMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维堆叠图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作三维堆叠图
    def test_theme50(self):
        mapName = "ThemeGraphStackBar3DMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维堆叠图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作三维堆叠图
    def test_theme51(self):
        mapName = "ThemeGraphStackBar3DMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"三维堆叠图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
   # 点数据制作环状统计专题图
    def test_theme52(self):
        mapName = "ThemeGraphRingMap1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"环状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作环状统计专题图
    def test_theme53(self):
        mapName = "ThemeGraphRingMap2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"环状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作环状统计专题图
    def test_theme54(self):
        mapName = "ThemeGraphRingMap3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeStatisticsTheme(self.driver,"环状图", dataset, "pop2019", "pop2020", "pop2021", "CB_Childish")
        theme.resultCompare(self,self.driver,mapName)
    #点数据制作热力图
    def test_theme55(self):
        mapName="HeatMap"
        dataset="风景名胜"
        theme.createMapAddLayer(self.driver,mapName,dataset,0)
        theme.makeHeatOrGridTheme(self.driver,dataset,"热力图","ZA_Insights")
        theme.resultCompare(self,self.driver,mapName)
   #栅格单值专题图
    def test_theme56(self):
        mapName="ThemeGridUniqueMap"
        dataset="DEM"
        theme.createMapAddLayer(self.driver,mapName,dataset,0)
        theme.makeHeatOrGridTheme(self.driver,dataset,"栅格单值专题图","BA_Blue")
        theme.resultCompare(self,self.driver,mapName)
   # 栅格分段专题图
    def test_theme57(self):
        mapName = "ThemeGridRangeMap"
        dataset = "DEM"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeHeatOrGridTheme(self.driver,dataset, "栅格分段专题图", "CB_Reds")
        theme.resultCompare(self,self.driver,mapName)
    # 点密度专题图
    def test_theme58(self):
        mapName = "ThemeDotDensityMap"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeDotOrSymbolTheme(self.driver,dataset, "点密度图","NUM")
        theme.resultCompare(self,self.driver,mapName)
    # 点数据制作等级符号专题图
    def test_theme59(self):
        mapName = "ThemeGraduatedSymbol1"
        dataset = "风景名胜"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeDotOrSymbolTheme(self.driver,dataset, "等级符号图", "pop2019")
        theme.resultCompare(self,self.driver,mapName)
    # 线数据制作等级符号专题图
    def test_theme60(self):
        mapName = "ThemeGraduatedSymbol2"
        dataset = "城市轨道交通"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeDotOrSymbolTheme(self.driver,dataset, "等级符号图","pop2019")
        theme.resultCompare(self,self.driver,mapName)
    # 面数据制作等级符号专题图
    def test_theme61(self):
        mapName = "ThemeGraduatedSymbol3"
        dataset = "区县级行政区划"
        theme.createMapAddLayer(self.driver,mapName, dataset, 0)
        theme.makeDotOrSymbolTheme(self.driver,dataset, "等级符号图","NUM")
        theme.resultCompare(self,self.driver,mapName)

if __name__ == '__main__':
    unittest.main()