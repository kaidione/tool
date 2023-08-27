



from base.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class SendMessage_Page(BasePage):
    # // *[ @ text = "联系人"]
    # //*[@text="好友"]
    # //*[@resource-id="com.tencent.mobileqq:id/rm"]/android.widget.LinearLayout[3]
    # //*[@resource-id="com.tencent.mobileqq:id/al_"]/android.widget.LinearLayout[3]
    # //*[@resource-id="com.tencent.mobileqq:id/rm"]/android.widget.LinearLayout[7]
    el_connector = (MobileBy.XPATH, '//*[@resource-id="com.tencent.mobileqq:id/recent_chat_list"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.view.View[1]')
    #el_friendlist = (MobileBy.XPATH, '//*[@text="好友"]')
    #el_targetfriend = (MobileBy.XPATH, '//*[@resource-id="com.tencent.mobileqq:id/rm"]/android.widget.LinearLayout[3]')
    #el_sendmessage = (MobileBy.XPATH, '//*[@resource-id="com.tencent.mobileqq:id/al_"]/android.widget.LinearLayout[3]')
    #
    # 	android.widget.EditText
    # //*[@resource-id="com.tencent.mobileqq:id/input"]

    el_inputmessage = (MobileBy.ID, 'com.tencent.mobileqq:id/input')
    # android.widget.Button
    # //*[@resource-id="com.tencent.mobileqq:id/fun_btn"]
    el_sendbutton = (MobileBy.ID, 'com.tencent.mobileqq:id/fun_btn')

    def sendMessage(self, message):
        self.click(self.el_connector, 5)
        #self.click(self.el_friendlist, 5)
        #self.click(self.el_targetfriend, 5)
        #self.click(self.el_sendmessage, 5)

        self.click(self.el_inputmessage, 5)
        self.input(self.el_inputmessage, 5, message)
        self.click(self.el_sendbutton, 5)

