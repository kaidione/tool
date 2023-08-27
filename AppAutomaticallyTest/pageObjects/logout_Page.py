from base.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class Logout_Page(BasePage):
    el_icon = (MobileBy.ID, 'com.tencent.mobileqq:id/e3u')
    el_setting = (MobileBy.ID, 'com.tencent.mobileqq:id/nuf')
    el_switch = (MobileBy.XPATH, '//*[@text="帐号管理"]')
    el_exit = (MobileBy.XPATH, '//*[@text="退出"]')
    el_sureExit = (MobileBy.XPATH, '//*[@text="退出登录"]')
    el_sure = (MobileBy.ID, 'com.tencent.mobileqq:id/dialogRightBtn')

    # com.tencent.mobileqq:id/action_sheet_button
    # 退出登录   //*[@resource-id="com.tencent.mobileqq:id/e3u"]/android.widget.FrameLayout[1]
    # //*[@text="退出登录"]

    def logout(self):
        # self.swipe(0.1, 0.5, 0.8, 0.5, 1000)
        self.click(self.el_icon, 5)
        self.click(self.el_setting, 5)
        self.click(self.el_switch, 5)
        self.click(self.el_exit, 5)
        self.click(self.el_sureExit, 5)
        self.click(self.el_sure, 5)
