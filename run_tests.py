import time
import sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
import unittest
from HTMLTestRunner import HTMLTestRunner
from db_fixture import test_data

#指定测试用例为当前文件夹下的interface目录
test_dir='./interface'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__=="__main__":
    test_data.init_data()#初始化接口测试数据
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    filename='./report/'+now+'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title="Test Report",description='Implementation Example with:')
    #runner.run(discover)
    runner.run(discover, rerun=0, save_last_run=False)

fp.close()
