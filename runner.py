import os
import unittest
import HTMLTestRunner_cn2
from datetime import datetime
suite=unittest.defaultTestLoader.discover("./",pattern='Test_*')

if __name__=="__main__":
    #run1=unittest.TextTestRunner()
    t=datetime.now().strftime("%Y_%m_%d_%H%M%S")
    file_result_name="result"+t+".html"
    file_result_dir=os.path.dirname(__file__)
    path1=file_result_dir+'/'+file_result_name
    if  not os.path.exists(path1):
        path2 = path1
    run1=HTMLTestRunner_cn2.HTMLTestRunner(open(path2,"wb"),title="zjx测试报告",description="zjx描述")
    run1.run(suite)
