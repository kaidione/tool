from base.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BasePage):
    el_cancel = (MobileBy.XPATH, '//android.widget.ImageView[@content-desc="清除帐号"]')
    el_inputText = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="请输入QQ号码或手机号或QID或邮箱"]')
    el_pw = (MobileBy.ID, "com.tencent.mobileqq:id/password")
    el_agree = (MobileBy.ID, "com.tencent.mobileqq:id/r15")
    el_login = (MobileBy.ID, "com.tencent.mobileqq:id/login")

    # 特有行为

    def login(self, username, pw):
        self.click(self.el_inputText, 5)
        self.click(self.el_cancel, 5)
        self.input(self.el_inputText, 5, username)
        self.click(self.el_pw, 5)
        self.input(self.el_pw, 5, pw)
        self.click(self.el_agree, 5)
        self.click(self.el_login, 5)
        # self.swipe(0.5, 0.1, 0.5, 0.8, 1000)
