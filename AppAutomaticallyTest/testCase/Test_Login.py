import os


import allure
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy

from pageObjects.login_Page import LoginPage
import pytest
from common.data_util import readYaml


@allure.feature("qq")
@allure.story("测试用例")
@pytest.mark.flaky(reruns=2, reruns_delay=1)
class TestLogin:

    # def setup_method(self):
    #     rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #     path = os.path.join(rootPath, "config\\config.yaml")
    #     data = readYaml(path)
    #     server = r"http://localhost:4723/wd/hub"
    #     self.driver = webdriver.Remote(server, data["desired_capabilities"])
    #@pytest.mark.smoke
    @pytest.mark.parametrize('username,pw',
                             [('123456', '123456'), ('12345678', '12345678'), ('2796176358', 'liwenhu1')])
    def test_login(self, username, pw):
        login_page = LoginPage()
        login_page.login(username, pw)
        el_icon = (MobileBy.ID, 'com.tencent.mobileqq:id/e3u')
        if username == '2796176358':
            assert login_page.locator(el_icon, 5)
        else:
            pass

# if __name__ == "__main__":
#     pytest.main()
