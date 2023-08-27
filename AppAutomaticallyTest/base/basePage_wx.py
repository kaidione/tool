#  定义一个类来定义描述每个页面的属性和行为
import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

from common.data_util import readYaml


class BasePage:

    # 属性

    def teardown_method(self):
        self.driver.quit()

    def __init__(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = os.path.join(rootPath, "config\\config_wx.yaml")
        data = readYaml(path)
        server = r"http://localhost:4723/wd/hub"
        self.driver = webdriver.Remote(server, data["desired_capabilities"])

    # 行为? 输入 点击

    def getAutomationID(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = os.path.join(rootPath, "config\\AutomationID.yaml")
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
