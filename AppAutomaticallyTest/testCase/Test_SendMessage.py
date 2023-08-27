import os
import time

from pageObjects.sendmessage_Page import SendMessage_Page
import pytest


class TestSendMessage:

    #@pytest.mark.smoke
    @pytest.mark.parametrize('user,message', [('2796176358', '第一条测试内容'), ('2958882954', '第二条测试内容'),
                                              ('2796176358', '第三条测试内容'), ('2958882954', '第四条测试内容')])
    def test_sendMessage(self, user, message):
        sendMessage = SendMessage_Page()
        sendMessage.sendMessage(message)


if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./report --clean")
