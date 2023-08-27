import os
import threading

from pywinauto import application, findwindows

from base.basePage_win import BasePage
from appium.webdriver.common.mobileby import MobileBy
from common.PowerShell import PowerShell
import pywinauto
import time

languageTarget = "US"


class Jump_T0_Power_Page_win(BasePage):

    def jump_to_power_page(self, target_element):
        data = self.getAutomationID()
        # time.sleep(5)
        # print(data["windows"]["language"][languageTarget]["device_name"])
        with PowerShell('GBK') as ps:
            ps.run("explorer.exe shell:AppsFolder\\E046963F.LenovoCompanion_k1h2ywk1493x8!App")
        el_device = (MobileBy.NAME, data["windows"]["language"][languageTarget]["device_name"])
        # print(el_device)
        # el_power = (MobileBy.ID, data["windows"]["language"][languageTarget]["power"])
        # print(el_power)
        el_power = (MobileBy.NAME, data["windows"]["language"][languageTarget]["power_name"])
        el_target_element = (MobileBy.NAME, target_element)
        # print(target_element)
        # print(el_target_element)

        try:
            self.click(el_device, 5)
            self.click(el_power, 5)
            self.locator(el_target_element, 5)
            self.quit()
            # print(True)
            return True
        except:
            self.quit()
            # print(False)
            return False


class Jump_T0_Audio_Page_win(BasePage):
    def jump_to_audio_page(self, target_element):
        data = self.getAutomationID()
        with PowerShell('GBK') as ps:
            ps.run("explorer.exe shell:AppsFolder\\E046963F.LenovoCompanion_k1h2ywk1493x8!App")
        # PowerShell.run()
        el_device = (MobileBy.NAME, data["windows"]["language"][languageTarget]["device_name"])
        el_audio = (MobileBy.NAME, data["windows"]["language"][languageTarget]["audio_name"])
        el_target_element = (MobileBy.NAME, target_element)
        # print(target_element)
        # print(el_target_element)

        try:
            self.click(el_device, 5)
            self.click(el_audio, 5)
            self.locator(el_target_element, 5)
            # print(True)
            self.quit()
            return True
        except:
            # print(False)
            self.quit()
            return False


class Jump_T0_Display_Page_win(BasePage):
    def jump_to_display_page(self, target_element):
        data = self.getAutomationID()
        with PowerShell('GBK') as ps:
            ps.run("explorer.exe shell:AppsFolder\\E046963F.LenovoCompanion_k1h2ywk1493x8!App")
        # PowerShell.run()
        el_device = (MobileBy.NAME, data["windows"]["language"][languageTarget]["device_name"])
        el_display = (MobileBy.NAME, data["windows"]["language"][languageTarget]["display_name"])
        el_target_element = (MobileBy.NAME, target_element)
        # print(target_element)
        # print(el_target_element)

        try:
            self.click(el_device, 5)
            self.click(el_display, 5)
            self.locator(el_target_element, 5)
            self.quit()
            # print(True)
            return True
        except:
            # print(False)
            self.quit()
            return False


class Jump_T0_Input_Page_win(BasePage):
    def jump_to_input_page(self, target_element):
        data = self.getAutomationID()
        with PowerShell('GBK') as ps:
            ps.run("explorer.exe shell:AppsFolder\\E046963F.LenovoCompanion_k1h2ywk1493x8!App")
        # PowerShell.run()
        el_device = (MobileBy.NAME, data["windows"]["language"][languageTarget]["device_name"])
        el_input = (MobileBy.NAME, data["windows"]["language"][languageTarget]["input_name"])
        el_target_element = (MobileBy.NAME, target_element)
        # print(target_element)
        # print(el_target_element)

        try:
            self.click(el_device, 5)
            self.click(el_input, 5)
            self.locator(el_target_element, 5)
            # print(True)
            self.quit()
            return True
        except:
            # print(False)
            self.quit()
            return False


class Jump_T0_Advanced_Settings_Page_win(BasePage):
    def jump_to_advanced_settings_page(self, target_element):
        data = self.getAutomationID()
        with PowerShell('GBK') as ps:
            ps.run("explorer.exe shell:AppsFolder\\E046963F.LenovoCompanion_k1h2ywk1493x8!App")
        # PowerShell.run()
        el_device = (MobileBy.NAME, data["windows"]["language"][languageTarget]["device_name"])
        el_advanced = (MobileBy.NAME, data["windows"]["language"][languageTarget]["advanced_name"])
        el_target_element = (MobileBy.NAME, target_element)
        # print(target_element)
        # print(el_target_element)

        try:
            self.click(el_device, 5)
            self.click(el_advanced, 5)
            self.locator(el_target_element, 5)
            # print(True)
            self.quit()
            return True
        except:
            # print(False)
            self.quit()
            return False


class ClearPopupThread(threading.Thread):
    def __init__(self, window_name, button_name, quit_event):
        threading.Thread.__init__(self)
        self.quit_event = quit_event
        self.window_name = window_name
        self.button_name = button_name

    def run(self):
        # from pywinauto import application, findwindows
        while True:

            try:
                handles = findwindows.find_windows(title=self.window_name)
            except findwindows.WindowNotFoundError:
                pass  # Just do nothing if the pop-up dialog was not found
            else:  # The window was found, so click the button
                for hwnd in handles:
                    app = application.Application()
                    app.connect(handle=hwnd)
                    popup = app[self.window_name]
                    # popup.print_control_identifiers()
                    # popup.child_window(title=self.button_name, class_name="Button").click()
                    button = getattr(popup, self.button_name)
                    button.click()
                    break
            if self.quit_event.is_set():
                break
            time.sleep(1)  # should help reduce cpu load a little for this thread


def DealPopup():
    time.sleep(2)
    quit_event = threading.Event()
    myThread = ClearPopupThread('System Language Modification Tool V2.0', '是(&Y)Button', quit_event)
    myThread.start()
    quit_event.set()


def switchLanguage(languageName):
    global languageTarget
    languageTarget = languageName
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app = pywinauto.Application(backend="uia").start(
        os.path.join(rootPath, "common\\SystemLanguageModificationTool.exe"))

    title = app["System Language Modification Tool V2.0"]
    # title.print_control_identifiers()
    languagePanel = title.child_window(auto_id="languagePanel", control_type="Pane")
    # languagePanel = title["Pane2"]
    # print(languagePanel.print_control_identifiers())
    SC = languagePanel.child_window(title="Chinese (Simplified)\r\n简体中文\r\n中文(中华人民共和国)",
                                    auto_id="Chinese (Simplified)", control_type="Button")
    AR = languagePanel.child_window(title="Arabic\r\n阿拉伯语\r\nالعربية (المملكة العربية السعودية)", auto_id="Arabic",
                                    control_type="Button")
    BR = languagePanel.child_window(title="Brazilian Portuguese\r\n巴西葡萄牙语\r\nPortuguês (Brasil)",
                                    auto_id="Brazilian Portuguese", control_type="Button")
    CR = languagePanel.child_window(title="Croatian\r\n克罗地亚语\r\nHrvatski (Hrvatska)", auto_id="Croatian",
                                    control_type="Button")
    CZ = languagePanel.child_window(title="Czech\r\n捷克语\r\nČeština", auto_id="Czech", control_type="Button")
    DK = languagePanel.child_window(title="Danish\r\n丹麦语\r\nDansk", auto_id="Danish", control_type="Button")
    FI = languagePanel.child_window(title="Finnish\r\n芬兰语\r\nSuomi", auto_id="Finnish", control_type="Button")
    FR = languagePanel.child_window(title="French\r\n法语\r\nFrançais (France)", auto_id="French",
                                    control_type="Button")
    GK = languagePanel.child_window(title="Greek\r\n希腊语\r\nΕλληνικά", auto_id="Greek", control_type="Button")
    GR = languagePanel.child_window(title="German\r\n德语\r\nDeutsch (Deutschland)", auto_id="German",
                                    control_type="Button")
    HE = languagePanel.child_window(title="Hebrew\r\n希伯来语\r\nעברית", auto_id="Hebrew", control_type="Button")
    HU = languagePanel.child_window(title="Hungarian\r\n匈牙利语\r\nMagyar", auto_id="Hungarian", control_type="Button")
    IT = languagePanel.child_window(title="Italian\r\n意大利语\r\nItaliano (Italia)", auto_id="Italian",
                                    control_type="Button")
    JP = languagePanel.child_window(title="Japanese\r\n日语\r\n日本語", auto_id="Japanese", control_type="Button")
    KR = languagePanel.child_window(title="Korean\r\n韩语\r\n한국어", auto_id="Korean", control_type="Button")
    NL = languagePanel.child_window(title="Dutch\r\n荷兰语\r\nNederlands (Nederland)", auto_id="Dutch",
                                    control_type="Button")
    Norwegian = languagePanel.child_window(title="Norwegian\r\n挪威语\r\nNorsk (bokmål)", auto_id="Norwegian",
                                    control_type="Button")
    PL = languagePanel.child_window(title="Polish\r\n波兰语\r\nPolski", auto_id="Polish", control_type="Button")
    PO = languagePanel.child_window(title="Portuguese\r\n葡萄牙语\r\nPortuguês (Portugal)", auto_id="Portuguese",
                                    control_type="Button")
    RO = languagePanel.child_window(title="Romanian\r\n罗马尼亚语\r\nRomână (România)", auto_id="Romanian",
                                    control_type="Button")
    RU = languagePanel.child_window(title="Russian\r\n俄语\r\nРусский", auto_id="Russian", control_type="Button")
    SH = languagePanel.child_window(title="Serbian (Latin)\r\n塞尔维亚语(拉丁语)\r\nSrpski (Srbija)",
                                    auto_id="Serbian (Latin)", control_type="Button")
    SK = languagePanel.child_window(title="Slovakian\r\n斯洛伐克语\r\nSlovenčina", auto_id="Slovakian",
                                    control_type="Button")
    SL = languagePanel.child_window(title="Slovenian\r\n斯洛文尼亚语\r\nSlovenski", auto_id="Slovenian",
                                    control_type="Button")
    SP = languagePanel.child_window(title="Spanish\r\n西班牙语\r\nEspañol (España)", auto_id="Spanish",
                                    control_type="Button")
    SV = languagePanel.child_window(title="Swedish\r\n瑞典语\r\nSvenska (Sverige)", auto_id="Swedish",
                                    control_type="Button")
    TC = languagePanel.child_window(title="Chinese (Traditional)\r\n繁体中文\r\n中文(台灣)",
                                    auto_id="Chinese (Traditional)", control_type="Button")
    TU = languagePanel.child_window(title="Turkish\r\n土耳其语\r\nTürkçe", auto_id="Turkish", control_type="Button")
    UA = languagePanel.child_window(title="Ukranian\r\n乌克兰语\r\nУкраїнська", auto_id="Ukranian",
                                    control_type="Button")
    US = languagePanel.child_window(title="Enlish\r\n英语\r\nEnglish (United States)", auto_id="Enlish",
                                    control_type="Button")
    # print(chinese.print_control_identifiers())

    if languageName == "AR":
        AR.click_input()
        DealPopup()
    elif languageName == "BR":
        BR.click_input()
        DealPopup()
    elif languageName == "CR":
        CR.click_input()
        DealPopup()
    elif languageName == "CZ":
        CZ.click_input()
        DealPopup()
    elif languageName == "DK":
        DK.click_input()
        DealPopup()
    elif languageName == "FI":
        FI.click_input()
        DealPopup()
    elif languageName == "FR":
        FR.click_input()
        DealPopup()
    elif languageName == "GK":
        GK.click_input()
        DealPopup()
    elif languageName == "GR":
        GR.click_input()
        DealPopup()
    elif languageName == "HE":
        HE.click_input()
        DealPopup()
    elif languageName == "HU":
        HU.click_input()
        DealPopup()
    elif languageName == "IT":
        IT.click_input()
        DealPopup()
    elif languageName == "JP":
        JP.click_input()
        DealPopup()
    elif languageName == "KR":
        KR.click_input()
        DealPopup()
    elif languageName == "NL":
        NL.click_input()
        DealPopup()
    elif languageName == "Norwegian":
        Norwegian.click_input()
        DealPopup()
    elif languageName == "PL":
        PL.click_input()
        DealPopup()
    elif languageName == "PO":
        PO.click_input()
        DealPopup()
    elif languageName == "RO":
        RO.click_input()
        DealPopup()
    elif languageName == "RU":
        RU.click_input()
        DealPopup()
    elif languageName == "SH":
        SH.click_input()
        DealPopup()
    elif languageName == "SK":
        SK.click_input()
        DealPopup()
    elif languageName == "SL":
        SL.click_input()
        DealPopup()
    elif languageName == "SP":
        SP.click_input()
        DealPopup()
    elif languageName == "SV":
        SV.click_input()
        DealPopup()
    elif languageName == "TC":
        TC.click_input()
        DealPopup()
    elif languageName == "TU":
        TU.click_input()
        DealPopup()
    elif languageName == "UA":
        UA.click_input()
        DealPopup()
    elif languageName == "US":
        US.click_input()
        # dlg = app["System Language Modification Tool V2.0Dialog2"]
        # dlg.wait(wait_for="ready", timeout=20, retry_interval=1)
        # yeah = dlg.child_window(title="是(Y)", auto_id="6", control_type="Button")
        # # dlg.print_control_identifiers()
        # yeah.click_imput()
        # Start the thread
        DealPopup()
        # ...
        # My program does it's thing here
        # ...
        # When my program is done I need to end the thread

    elif languageName == "SC":
        SC.click_input()
        DealPopup()
    title.wait(wait_for="ready", timeout=20, retry_interval=1)
    # send_keys("{VK_RETURN}")
    with PowerShell('GBK') as ps:
        time.sleep(1)
        ps.run("taskkill /im SystemLanguageModificationTool.exe /f")
    # send_keys("{VK_TAB}")


# if __name__ == '__main__':
    # Jump_T0_Power_Page_win().jump_to_power_page("Lenovo Vantage toolbar and premium settings")
    # switchLanguage('US')
    # Jump_T0_Audio_Page_win().jump_to_audio_page(123)
    # Jump_T0_Display_Page_win().jump_to_display_page(123)
