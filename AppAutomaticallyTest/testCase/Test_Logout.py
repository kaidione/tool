import allure
from appium.webdriver.common.mobileby import MobileBy

from pageObjects.logout_Page import Logout_Page

import pytest



@allure.feature("qq")
@allure.story("测试用例")
@pytest.mark.flaky(reruns=2, reruns_delay=1)
class Test_Logout:

    # def setUp_method(self):
    #     rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #     path = os.path.join(rootPath, "config\\config.yaml")
    #     data = readYaml(path)
    #     server = r"http://localhost:4723/wd/hub"
    #     self.driver = webdriver.Remote(server, data["desired_capabilities"])

    #@pytest.mark.smoke
    def test_logout(self):
        el_login = (MobileBy.ID, "com.tencent.mobileqq:id/login")
        logout_page = Logout_Page()
        logout_page.logout()
        assert logout_page.locator(el_login, 5)



if __name__ == "__main__":
    pytest.main()