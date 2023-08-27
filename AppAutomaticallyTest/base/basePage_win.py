#  定义一个类来定义描述每个页面的属性和行为
import os

from appium import webdriver
import subprocess
import time
from common.PowerShell import PowerShell
from common.data_util import readYaml


class BasePage:

    # 属性
    def appium_start(self, host, port, log_Path):
        """
        启动appium server
        :param log_Path:
        :param host:
        :param port:
        :return:
        """
        # 指定bp端口号
        bootstrap_port = str(port + 1)
        # 把在cmd弹窗输入的命令，直接写到这里
        # cmd = 'start /b appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
        # 去掉 “/b”，即可以打开cmd弹窗运行
        cmd = 'start  appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
        # 打印输入的cmd命令，及时间
        # print("%s at %s " % (cmd, time.ctime()))
        # print("./")
        subprocess.Popen(cmd, shell=True, stdout=open(log_Path + str(port) + '.log', 'a'),
                         stderr=subprocess.STDOUT)

    def stop_appium(self, pc="WIN", post_num=4723):
        '''关闭appium服务'''
        if pc.upper() == 'WIN':
            p = os.popen(f'netstat  -aon|findstr {post_num}')
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
                os.popen(f'taskkill /F /PID {p1}')  # 结束进程
                print('appium server已结束')
                # time.sleep(2)
                # os.popen(f'taskkill /im node.exe /f')  # 结束打开的cmd进程
                # print('node已结束')
        elif pc.upper() == 'MAC':
            p = os.popen(f'lsof -i tcp:{post_num}')
            p0 = p.read()
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
                os.popen(f'kill {p1}')  # 结束进程
                print('appium server已结束')
    def quit(self):
        self.driver.quit()
        with PowerShell('GBK') as ps:
            time.sleep(1)
            ps.run("taskkill /F /IM node.exe /t")
        with PowerShell('GBK') as ps:
            time.sleep(1)
            ps.run("taskkill /F /IM cmd.exe /t")



    def __init__(self):

        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # print(rootPath)
        path = os.path.join(rootPath, "config\\config_win.yaml")
        # print(path)
        log_Path = os.path.join(rootPath, "config\\appium_log")
        # print(log_Path)
        self.appium_start('127.0.0.1', 4723, log_Path)
        data = readYaml(path)
        server = r"http://localhost:4723/wd/hub"
        # server = r"http://127.0.0.1:4723"
        # os.system(r'start "" /d "C:\Program Files (x86)\Windows Application Driver\"  "WinAppDriver.exe"')
        # print("开始连接")
        try:
            self.driver = webdriver.Remote(server, data["desired_capabilities"])
            # print("连接完成")
        except Exception as e:
            raise AssertionError(e)

    # 行为? 输入 点击

    def getAutomationID(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = os.path.join(rootPath, "config\\AutomationID_win.yaml")
        data = readYaml(path)
        return data

    # 定位元素
    def locator(self, loc, times=5):
        # self.driver.implicitly_wait(20)
        for i in range(times):
            self.driver.implicitly_wait(3000)
            return self.driver.find_element(*loc)

    def get_locator_attribute_value(self, loc, times, attribute):
        self.locator(loc, times)
        return self.driver.find_element(*loc).get_attribute(attribute)

    def input(self, loc, times, value):
        self.locator(loc, times).clear()
        self.locator(loc, times).send_keys(value)
        # time.sleep(1)

    def click(self, loc, times):
        self.locator(loc, times).click()
        # time.sleep(1)

    def swipe(self, start_x, start_y, end_x, end_y, duration=0):
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']

        self.driver.swipe(start_x=x * start_x, start_y=y * start_y, end_x=x * end_x, end_y=y * end_y, duration=1000)


# if __name__ == '__main__':
#     BasePage().__init__()