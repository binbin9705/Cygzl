
import unittest
# import HTMLTestRunner
import HTMLTestRunner_cn
from case import test_case1
if __name__ == '__main__':
    #创建一个测试套件
    dir='case'
    dircase='test*.py'
    # dircase = 'test_case3.py'
    suite=unittest.defaultTestLoader.discover(dir,dircase)
    #创建生成测试报告方法
    # now=time.strftime('%Y-%m-%d %H_%M_%S')
    path='plugins/测试报告.html'
    pathopen=open(path,'wb')
    runner=HTMLTestRunner_cn.HTMLTestRunner(stream=pathopen,description=u'用例执行情况',title='产业高质量发展平台测试报告',verbosity=2)
    runner.run(suite)





