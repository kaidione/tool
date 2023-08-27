from base.basePage_wx import BasePage
from appium.webdriver.common.mobileby import MobileBy


class SendMessage_Page_wx(BasePage):

    def sendMessage_wx(self, friendName, Message_Text):
        data = self.getAutomationID()
        el_search_button = (MobileBy.ID, data["Wechat"]["wx_page"]["search_button"])
        el_search_friend = (MobileBy.ID, data["Wechat"]["wx_page"]["search_friend"])
        el_click_search_result = (MobileBy.ID, data["Wechat"]["wx_page"]["click_search_result"])
        el_edit_message = (MobileBy.ID, data["Wechat"]["wx_page"]["edit_message"])
        el_send_button = (MobileBy.ID, data["Wechat"]["wx_page"]["send_button"])
        self.click(el_search_button, 5)
        self.click(el_search_friend, 5)
        self.input(el_search_friend, 5, friendName)
        self.click(el_click_search_result, 5)
        self.click(el_edit_message, 5)
        self.input(el_edit_message, 5, Message_Text)
        self.click(el_send_button, 5)


class SetTopMessage_wx(BasePage):

    def setTopMessage_wx(self, friendName):
        data = self.getAutomationID()
        el_search_button = (MobileBy.ID, data["Wechat"]["wx_page"]["search_button"])
        el_search_friend = (MobileBy.ID, data["Wechat"]["wx_page"]["search_friend"])
        el_click_search_result = (MobileBy.ID, data["Wechat"]["wx_page"]["click_search_result"])
        el_more = (MobileBy.ID, data["Wechat"]["wx_page"]["more"])
        el_top_toggle_xpath = (MobileBy.XPATH, data["Wechat"]["wx_page"]["top_toggle_xpath"])
        el_back_wx_button = (MobileBy.ID, data["Wechat"]["wx_page"]["back_wx_button"])
        el_back_more_button = (MobileBy.ID, data["Wechat"]["wx_page"]["back_more_button"])
        el_cancel_button = (MobileBy.ID, data["Wechat"]["wx_page"]["cancel_button"])
        self.click(el_search_button, 5)
        self.click(el_search_friend, 5)
        self.input(el_search_friend, 5, friendName)
        self.click(el_click_search_result, 5)
        self.click(el_more, 5)
        self.click(el_top_toggle_xpath, 5)
        self.click(el_back_more_button, 5)
        self.click(el_back_wx_button, 5)
        self.click(el_cancel_button, 5)


class Send_Circle_of_friend_wx(BasePage):

    def send_Circle_of_friend_wx(self, TextMessage):
        data = self.getAutomationID()
        el_find_xpath = (MobileBy.XPATH, data["Wechat"]["find_page"]["find_xpath"])
        el_circle_of_friend = (MobileBy.ID, data["Wechat"]["find_page"]["circle_of_friend"])
        keep_tap_camera_button = data["Wechat"]["find_page"]["keep_tap_camera_button"]
        el_edit_text_message = (MobileBy.ID, data["Wechat"]["find_page"]["edit_text_message"])
        el_send_editAfter_button = (MobileBy.ID, data["Wechat"]["find_page"]["send_editAfter_button"])
        self.click(el_find_xpath, 5)
        self.click(el_circle_of_friend, 5)
        self.swipe(keep_tap_camera_button["start_x"], keep_tap_camera_button["start_y"], keep_tap_camera_button["end_x"], keep_tap_camera_button["end_y"], keep_tap_camera_button["duration"])
        self.click(el_edit_text_message, 5)
        self.input(el_edit_text_message, 5, TextMessage)
        self.click(el_send_editAfter_button, 5)


class Update_Friend_name_wx(BasePage):

    def update_Friend_name_wx(self, old_friendName, new_friendName):
        data = self.getAutomationID()
        el_search_button = (MobileBy.ID, data["Wechat"]["wx_page"]["search_button"])
        el_search_friend = (MobileBy.ID, data["Wechat"]["wx_page"]["search_friend"])
        el_click_search_result = (MobileBy.ID, data["Wechat"]["wx_page"]["click_search_result"])
        el_more = (MobileBy.ID, data["Wechat"]["wx_page"]["more"])
        el_friend_picture = (MobileBy.ID, data["Wechat"]["connect_page"]["friend_picture"])
        el_update_name = (MobileBy.ID, data["Wechat"]["connect_page"]["update_name"])
        el_update_name_text = (MobileBy.ID, data["Wechat"]["connect_page"]["update_name_text"])
        el_send_editAfter_button = (MobileBy.ID, data["Wechat"]["find_page"]["send_editAfter_button"])
        el_update_name_text_editing = (MobileBy.ID, data["Wechat"]["connect_page"]["update_name_text_editing"])
        self.click(el_search_button, 5)
        self.click(el_search_friend, 5)
        self.input(el_search_friend, 5, old_friendName)
        self.click(el_click_search_result, 5)
        self.click(el_more, 5)
        self.click(el_friend_picture, 5)
        self.click(el_update_name, 5)
        self.click(el_update_name_text, 5)
        self.input(el_update_name_text_editing, 5, new_friendName)
        self.click(el_send_editAfter_button, 5)

        el_nike = (MobileBy.ID, data["Wechat"]["connect_page"]["nike"])
        return self.get_locator_attribute_value(el_nike, 5, "text")
