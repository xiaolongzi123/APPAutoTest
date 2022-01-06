import os
import unittest
import time
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from HTMLTestRunner import HTMLTestRunner
from testCase.test_analyst_overlay import MyTestCaseOverlay
from testCase.test_analyst_buffer import MyTestCaseBuffer
from testCase2.test_testyaml import MyTestCaseBuffer


if __name__ == "__main__":
    suite = unittest.TestSuite()
    # discover = unittest.defaultTestLoader.discover("../testCase/", pattern='test_*.py', top_level_dir=None)
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         suite.addTests(test_case)
    #         print(suite)
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCaseOverlay))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCaseBuffer))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCaseBuffer))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCaseTheme))
    # 生成测试报告
    # 选择指定时间格式
    timestr = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
    # 定义测试报告存放路径和报告名称
    Report = '../report/test_report_' + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + '.html'
    with open(Report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='iTablet自动化测试报告', description='执行人：lq')
        runner.run(suite)
        f.close()
