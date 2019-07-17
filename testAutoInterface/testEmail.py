__author__ = '791399137'
import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from common.configEmail import send_email
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom
import common.Log
path = getpathInfo.get_Path()
caseFile = os.path.join(path, "testCase")#真正的测试断言文件路径
test_suite = unittest.TestSuite()
all_case=unittest.defaultTestLoader.discover(caseFile,'test01case.py')
print(all_case)