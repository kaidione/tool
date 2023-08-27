import os
import time

import allure

from pageObjects.sendMessage_Page_wx import SendMessage_Page_wx
from pageObjects.sendMessage_Page_wx import SetTopMessage_wx
from pageObjects.sendMessage_Page_wx import Send_Circle_of_friend_wx
from pageObjects.sendMessage_Page_wx import Update_Friend_name_wx
import pytest


@allure.feature("wechat")
@allure.story("测试用例")
@pytest.mark.flaky(reruns=2, reruns_delay=1)
class TestSendMessage:

    # @pytest.mark.smoke
    @pytest.mark.parametrize('user,message', [('宇轩', '第一条测试内容'), ('宇轩', '第二条测试内容'),
                                              ('宇轩', '第三条测试内容'), ('宇轩', '第四条测试内容')])
    def test_sendMessage_wx(self, user, message):
        sendMessage = SendMessage_Page_wx()
        sendMessage.sendMessage_wx(user, message)


class TestSetTopMessage:

    # @pytest.mark.smoke
    @pytest.mark.parametrize('user', ['宇轩'])
    def test_setTopMessage_wx(self, user):
        SetTopMessage = SetTopMessage_wx()
        SetTopMessage.setTopMessage_wx(user)


class TestSend_Circle_of_friend:

    #@pytest.mark.smoke
    @pytest.mark.parametrize('TextMessage', ['宇轩'])
    def test_send_Circle_of_friend(self, TextMessage):
        Send_Circle_of_friend = Send_Circle_of_friend_wx()
        Send_Circle_of_friend.send_Circle_of_friend_wx(TextMessage)


class TestUpdate_Friend_name:

    #@pytest.mark.smoke
    @pytest.mark.abc
    @pytest.mark.parametrize('old_friendName, new_friendName', [('宇轩', '宇轩1')])
    def test_update_Friend_name(self, old_friendName, new_friendName):
        Update_Friend_name = Update_Friend_name_wx()
        real_result = Update_Friend_name.update_Friend_name_wx(old_friendName, new_friendName)
        assert real_result == new_friendName


if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./report --clean")
