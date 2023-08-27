import os
import time

import allure

from pageObjects.jump_to_page_win import Jump_T0_Power_Page_win
from pageObjects.jump_to_page_win import Jump_T0_Audio_Page_win
from pageObjects.jump_to_page_win import Jump_T0_Display_Page_win
from pageObjects.jump_to_page_win import Jump_T0_Input_Page_win
from pageObjects.jump_to_page_win import Jump_T0_Advanced_Settings_Page_win
from pageObjects.jump_to_page_win import switchLanguage
import pytest
from common.data_util import Json_to_Python
from common.PowerShell import PowerShell


# def teardown_Class():
#     switchLanguage("US")
#
#
# def setup_Class():
#     switchLanguage("US")


@allure.feature("Multi-language")
@allure.story("测试用例")
# @pytest.mark.flaky(reruns=1, reruns_delay=1)
class TestMultiLanguage:
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # print(rootPath1)
    # rootPath = os.path.join(rootPath1, "Multi_Language\\")
    # https://blog.csdn.net/qq_36502272/article/details/100671845

    def teardown_method(self):
        # rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        with PowerShell('GBK') as ps:
            ps.run("taskkill /im LenovoVantage.exe /f")
            # ps.run("taskkill /im SystemLanguageModificationTool.exe /f")
            time.sleep(2)

        with PowerShell('GBK') as ps:
            time.sleep(1)
            ps.run("taskkill /im SystemLanguageModificationTool.exe /f")
            # ps.run(os.path.join(rootPath, "common\\SystemLanguageModificationTool.exe"))

    # def setup_method(self):
    #     with PowerShell('GBK') as ps:
    #         ps.run("explorer.exe shell:AppsFolder\\E046963F.LenovoCompanion_k1h2ywk1493x8!App")
    # https://docs.pytest.org/en/stable/deprecations.html#support-for-tests-written-for-nose

    # path = os.path.join(rootPath, "data")
    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\AR\\") + os.listdir(os.path.join(rootPath, "data\\power\\AR"))[0]))
    def test_AR_Power(self, target_element):
        switchLanguage("AR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\BR\\") + os.listdir(os.path.join(rootPath, "data\\power\\BR"))[0]))
    def test_BR_Power(self, target_element):
        switchLanguage("BR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\CR\\") + os.listdir(os.path.join(rootPath, "data\\power\\CR"))[0]))
    def test_CR_Power(self, target_element):
        switchLanguage("CR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\CZ\\") + os.listdir(os.path.join(rootPath, "data\\power\\CZ"))[0]))
    def test_CZ_Power(self, target_element):
        switchLanguage("CZ")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\DK\\") + os.listdir(os.path.join(rootPath, "data\\power\\DK"))[0]))
    def test_DK_Power(self, target_element):
        switchLanguage("DK")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\FI\\") + os.listdir(os.path.join(rootPath, "data\\power\\FI"))[0]))
    def test_FI_Power(self, target_element):
        switchLanguage("FI")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\FR\\") + os.listdir(os.path.join(rootPath, "data\\power\\FR"))[0]))
    def test_FR_Power(self, target_element):
        switchLanguage("FR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\GK\\") + os.listdir(os.path.join(rootPath, "data\\power\\GK"))[0]))
    def test_GK_Power(self, target_element):
        switchLanguage("GK")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\GR\\") + os.listdir(os.path.join(rootPath, "data\\power\\GR"))[0]))
    def test_GR_Power(self, target_element):
        switchLanguage("GR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\HE\\") + os.listdir(os.path.join(rootPath, "data\\power\\HE"))[0]))
    def test_HE_Power(self, target_element):
        switchLanguage("HE")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\HU\\") + os.listdir(os.path.join(rootPath, "data\\power\\HU"))[0]))
    def test_HU_Power(self, target_element):
        switchLanguage("HU")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\IT\\") + os.listdir(os.path.join(rootPath, "data\\power\\IT"))[0]))
    def test_IT_Power(self, target_element):
        switchLanguage("IT")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\JP\\") + os.listdir(os.path.join(rootPath, "data\\power\\JP"))[0]))
    def test_JP_Power(self, target_element):
        switchLanguage("JP")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\KR\\") + os.listdir(os.path.join(rootPath, "data\\power\\KR"))[0]))
    def test_KR_Power(self, target_element):
        switchLanguage("KR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\NL\\") + os.listdir(os.path.join(rootPath, "data\\power\\NL"))[0]))
    def test_NL_Power(self, target_element):
        switchLanguage("NL")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\NO\\") + os.listdir(os.path.join(rootPath, "data\\power\\NO"))[0]))
    def test_NO_Power(self, target_element):
        switchLanguage("Norwegian")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\PL\\") + os.listdir(os.path.join(rootPath, "data\\power\\PL"))[0]))
    def test_PL_Power(self, target_element):
        switchLanguage("PL")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\PO\\") + os.listdir(os.path.join(rootPath, "data\\power\\PO"))[0]))
    def test_PO_Power(self, target_element):
        switchLanguage("PO")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\RO\\") + os.listdir(os.path.join(rootPath, "data\\power\\RO"))[0]))
    def test_RO_Power(self, target_element):
        switchLanguage("AR")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\RU\\") + os.listdir(os.path.join(rootPath, "data\\power\\RU"))[0]))
    def test_RU_Power(self, target_element):
        switchLanguage("RU")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\SC\\") + os.listdir(os.path.join(rootPath, "data\\power\\SC"))[0]))
    def test_SC_Power(self, target_element):
        switchLanguage("SC")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\SH\\") + os.listdir(os.path.join(rootPath, "data\\power\\SH"))[0]))
    def test_SH_Power(self, target_element):
        switchLanguage("SH")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\SK\\") + os.listdir(os.path.join(rootPath, "data\\power\\SK"))[0]))
    def test_SK_Power(self, target_element):
        switchLanguage("SK")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\SL\\") + os.listdir(os.path.join(rootPath, "data\\power\\SL"))[0]))
    def test_SL_Power(self, target_element):
        switchLanguage("SL")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\SP\\") + os.listdir(os.path.join(rootPath, "data\\power\\SP"))[0]))
    def test_SP_Power(self, target_element):
        switchLanguage("SP")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\SV\\") + os.listdir(os.path.join(rootPath, "data\\power\\SV"))[0]))
    def test_SV_Power(self, target_element):
        switchLanguage("SV")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\TC\\") + os.listdir(os.path.join(rootPath, "data\\power\\TC"))[0]))
    def test_TC_Power(self, target_element):
        switchLanguage("TC")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\TU\\") + os.listdir(os.path.join(rootPath, "data\\power\\TU"))[0]))
    def test_TU_Power(self, target_element):
        switchLanguage("TU")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.power
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\UA\\") + os.listdir(os.path.join(rootPath, "data\\power\\UA"))[0]))
    def test_UA_Power(self, target_element):
        switchLanguage("UA")
        jump_to_power_page = Jump_T0_Power_Page_win()
        result = jump_to_power_page.jump_to_power_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\AR\\") + os.listdir(os.path.join(rootPath, "data\\audio\\AR"))[0]))
    def test_AR_Audio(self, target_element):
        switchLanguage("AR")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\BR\\") + os.listdir(os.path.join(rootPath, "data\\audio\\BR"))[0]))
    def test_BR_Audio(self, target_element):
        switchLanguage("BR")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\CR\\") + os.listdir(os.path.join(rootPath, "data\\audio\\CR"))[0]))
    def test_CR_Audio(self, target_element):
        switchLanguage("CR")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\CZ\\") + os.listdir(os.path.join(rootPath, "data\\audio\\CZ"))[0]))
    def test_CZ_Audio(self, target_element):
        switchLanguage("CZ")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\DK\\") + os.listdir(os.path.join(rootPath, "data\\audio\\DK"))[0]))
    def test_DK_Audio(self, target_element):
        switchLanguage("DK")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\FI\\") + os.listdir(os.path.join(rootPath, "data\\audio\\FI"))[0]))
    def test_FI_Audio(self, target_element):
        switchLanguage("FI")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\FR\\") + os.listdir(os.path.join(rootPath, "data\\audio\\FR"))[0]))
    def test_FR_Audio(self, target_element):
        switchLanguage("FR")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\GK\\") + os.listdir(os.path.join(rootPath, "data\\audio\\GK"))[0]))
    def test_GK_Audio(self, target_element):
        switchLanguage("GK")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\GR\\") + os.listdir(os.path.join(rootPath, "data\\audio\\GR"))[0]))
    def test_GR_Audio(self, target_element):
        switchLanguage("GR")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\HE\\") + os.listdir(os.path.join(rootPath, "data\\audio\\HE"))[0]))
    def test_HE_Audio(self, target_element):
        switchLanguage("HE")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\HU\\") + os.listdir(os.path.join(rootPath, "data\\audio\\HU"))[0]))
    def test_HU_Audio(self, target_element):
        switchLanguage("HU")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\IT\\") + os.listdir(os.path.join(rootPath, "data\\audio\\IT"))[0]))
    def test_IT_Audio(self, target_element):
        switchLanguage("IT")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\JP\\") + os.listdir(os.path.join(rootPath, "data\\audio\\JP"))[0]))
    def test_JP_Audio(self, target_element):
        switchLanguage("JP")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\KR\\") + os.listdir(os.path.join(rootPath, "data\\audio\\KR"))[0]))
    def test_KR_Audio(self, target_element):
        switchLanguage("KR")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\NL\\") + os.listdir(os.path.join(rootPath, "data\\audio\\NL"))[0]))
    def test_NL_Audio(self, target_element):
        switchLanguage("NL")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\NO\\") + os.listdir(os.path.join(rootPath, "data\\audio\\NO"))[0]))
    def test_NO_Audio(self, target_element):
        switchLanguage("Norwegian")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\PL\\") + os.listdir(os.path.join(rootPath, "data\\audio\\PL"))[0]))
    def test_PL_Audio(self, target_element):
        switchLanguage("PL")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\PO\\") + os.listdir(os.path.join(rootPath, "data\\audio\\PO"))[0]))
    def test_PO_Audio(self, target_element):
        switchLanguage("PO")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\RO\\") + os.listdir(os.path.join(rootPath, "data\\audio\\RO"))[0]))
    def test_RO_Audio(self, target_element):
        switchLanguage("RO")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\RU\\") + os.listdir(os.path.join(rootPath, "data\\audio\\RU"))[0]))
    def test_RU_Audio(self, target_element):
        switchLanguage("RU")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\SC\\") + os.listdir(os.path.join(rootPath, "data\\audio\\SC"))[0]))
    def test_SC_Audio(self, target_element):
        switchLanguage("SC")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\SH\\") + os.listdir(os.path.join(rootPath, "data\\audio\\SH"))[0]))
    def test_SH_Audio(self, target_element):
        switchLanguage("SH")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\SK\\") + os.listdir(os.path.join(rootPath, "data\\audio\\SK"))[0]))
    def test_SK_Audio(self, target_element):
        switchLanguage("SK")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\SL\\") + os.listdir(os.path.join(rootPath, "data\\audio\\SL"))[0]))
    def test_SL_Audio(self, target_element):
        switchLanguage("SL")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\SP\\") + os.listdir(os.path.join(rootPath, "data\\audio\\SP"))[0]))
    def test_SP_Audio(self, target_element):
        switchLanguage("SP")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\SV\\") + os.listdir(os.path.join(rootPath, "data\\audio\\SV"))[0]))
    def test_SV_Audio(self, target_element):
        switchLanguage("SV")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\TC\\") + os.listdir(os.path.join(rootPath, "data\\audio\\TC"))[0]))
    def test_TC_Audio(self, target_element):
        switchLanguage("TC")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\TU\\") + os.listdir(os.path.join(rootPath, "data\\audio\\TU"))[0]))
    def test_TU_Audio(self, target_element):
        switchLanguage("TU")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.audio
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\audio\\UA\\") + os.listdir(os.path.join(rootPath, "data\\audio\\UA"))[0]))
    def test_UA_Audio(self, target_element):
        switchLanguage("UA")
        jump_to_audio_page = Jump_T0_Audio_Page_win()
        result = jump_to_audio_page.jump_to_audio_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\AR\\") + os.listdir(os.path.join(rootPath, "data\\display\\AR"))[0]))
    def test_AR_Display(self, target_element):
        switchLanguage("AR")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\BR\\") + os.listdir(os.path.join(rootPath, "data\\display\\BR"))[0]))
    def test_BR_Display(self, target_element):
        switchLanguage("BR")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\CR\\") + os.listdir(os.path.join(rootPath, "data\\display\\CR"))[0]))
    def test_CR_Display(self, target_element):
        switchLanguage("CR")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\CZ\\") + os.listdir(os.path.join(rootPath, "data\\display\\CZ"))[0]))
    def test_CZ_Display(self, target_element):
        switchLanguage("CZ")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\DK\\") + os.listdir(os.path.join(rootPath, "data\\display\\DK"))[0]))
    def test_DK_Display(self, target_element):
        switchLanguage("DK")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\FI\\") + os.listdir(os.path.join(rootPath, "data\\display\\FI"))[0]))
    def test_FI_Display(self, target_element):
        switchLanguage("FI")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\FR\\") + os.listdir(os.path.join(rootPath, "data\\display\\FR"))[0]))
    def test_FR_Display(self, target_element):
        switchLanguage("FR")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\GK\\") + os.listdir(os.path.join(rootPath, "data\\display\\GK"))[0]))
    def test_GK_Display(self, target_element):
        switchLanguage("GK")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\GR\\") + os.listdir(os.path.join(rootPath, "data\\display\\GR"))[0]))
    def test_GR_Display(self, target_element):
        switchLanguage("GR")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\HE\\") + os.listdir(os.path.join(rootPath, "data\\display\\HE"))[0]))
    def test_HE_Display(self, target_element):
        switchLanguage("HE")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\HU\\") + os.listdir(os.path.join(rootPath, "data\\display\\HU"))[0]))
    def test_HU_Display(self, target_element):
        switchLanguage("HU")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\IT\\") + os.listdir(os.path.join(rootPath, "data\\display\\IT"))[0]))
    def test_IT_Display(self, target_element):
        switchLanguage("IT")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\JP\\") + os.listdir(os.path.join(rootPath, "data\\display\\JP"))[0]))
    def test_JP_Display(self, target_element):
        switchLanguage("JP")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\KR\\") + os.listdir(os.path.join(rootPath, "data\\display\\KR"))[0]))
    def test_KR_Display(self, target_element):
        switchLanguage("KR")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\NL\\") + os.listdir(os.path.join(rootPath, "data\\display\\NL"))[0]))
    def test_NL_Display(self, target_element):
        switchLanguage("NL")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\NO\\") + os.listdir(os.path.join(rootPath, "data\\display\\NO"))[0]))
    def test_NO_Display(self, target_element):
        switchLanguage("Norwegian")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\PL\\") + os.listdir(os.path.join(rootPath, "data\\display\\PL"))[0]))
    def test_PL_Display(self, target_element):
        switchLanguage("PL")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\PO\\") + os.listdir(os.path.join(rootPath, "data\\display\\PO"))[0]))
    def test_PO_Display(self, target_element):
        switchLanguage("PO")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\RO\\") + os.listdir(os.path.join(rootPath, "data\\display\\RO"))[0]))
    def test_RO_Display(self, target_element):
        switchLanguage("RO")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\RU\\") + os.listdir(os.path.join(rootPath, "data\\display\\RU"))[0]))
    def test_RU_Display(self, target_element):
        switchLanguage("RU")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\SC\\") + os.listdir(os.path.join(rootPath, "data\\display\\SC"))[0]))
    def test_SC_Display(self, target_element):
        switchLanguage("SC")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\SH\\") + os.listdir(os.path.join(rootPath, "data\\display\\SH"))[0]))
    def test_SH_Display(self, target_element):
        switchLanguage("SH")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\SK\\") + os.listdir(os.path.join(rootPath, "data\\display\\SK"))[0]))
    def test_SK_Display(self, target_element):
        switchLanguage("SK")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\SL\\") + os.listdir(os.path.join(rootPath, "data\\display\\SL"))[0]))
    def test_SL_Display(self, target_element):
        switchLanguage("SL")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\SP\\") + os.listdir(os.path.join(rootPath, "data\\display\\SP"))[0]))
    def test_SP_Display(self, target_element):
        switchLanguage("SP")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\SV\\") + os.listdir(os.path.join(rootPath, "data\\display\\SV"))[0]))
    def test_SV_Display(self, target_element):
        switchLanguage("SV")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\TC\\") + os.listdir(os.path.join(rootPath, "data\\display\\TC"))[0]))
    def test_TC_Display(self, target_element):
        switchLanguage("TC")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\display\\TU\\") + os.listdir(os.path.join(rootPath, "data\\display\\TU"))[0]))
    def test_TU_Display(self, target_element):
        switchLanguage("TU")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.display
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\power\\UA\\") + os.listdir(os.path.join(rootPath, "data\\power\\UA"))[0]))
    def test_UA_Display(self, target_element):
        switchLanguage("UA")
        jump_to_display_page = Jump_T0_Display_Page_win()
        result = jump_to_display_page.jump_to_display_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\AR\\") + os.listdir(os.path.join(rootPath, "data\\input\\AR"))[0]))
    def test_AR_Input(self, target_element):
        switchLanguage("AR")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\BR\\") + os.listdir(os.path.join(rootPath, "data\\input\\BR"))[0]))
    def test_BR_Input(self, target_element):
        switchLanguage("BR")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\CR\\") + os.listdir(os.path.join(rootPath, "data\\input\\CR"))[0]))
    def test_CR_Input(self, target_element):
        switchLanguage("CR")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\CZ\\") + os.listdir(os.path.join(rootPath, "data\\input\\CZ"))[0]))
    def test_CZ_Input(self, target_element):
        switchLanguage("CZ")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\DK\\") + os.listdir(os.path.join(rootPath, "data\\input\\DK"))[0]))
    def test_DK_Input(self, target_element):
        switchLanguage("DK")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\FI\\") + os.listdir(os.path.join(rootPath, "data\\input\\FI"))[0]))
    def test_FI_Input(self, target_element):
        switchLanguage("FI")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\FR\\") + os.listdir(os.path.join(rootPath, "data\\input\\FR"))[0]))
    def test_FR_Input(self, target_element):
        switchLanguage("FR")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\GK\\") + os.listdir(os.path.join(rootPath, "data\\input\\GK"))[0]))
    def test_GK_Input(self, target_element):
        switchLanguage("GK")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\GR\\") + os.listdir(os.path.join(rootPath, "data\\input\\GR"))[0]))
    def test_GR_Input(self, target_element):
        switchLanguage("GR")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\HE\\") + os.listdir(os.path.join(rootPath, "data\\input\\HE"))[0]))
    def test_HE_Input(self, target_element):
        switchLanguage("HE")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\HU\\") + os.listdir(os.path.join(rootPath, "data\\input\\HU"))[0]))
    def test_HU_Input(self, target_element):
        switchLanguage("HU")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\IT\\") + os.listdir(os.path.join(rootPath, "data\\input\\IT"))[0]))
    def test_IT_Input(self, target_element):
        switchLanguage("IT")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\JP\\") + os.listdir(os.path.join(rootPath, "data\\input\\JP"))[0]))
    def test_JP_Input(self, target_element):
        switchLanguage("JP")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\KR\\") + os.listdir(os.path.join(rootPath, "data\\input\\KR"))[0]))
    def test_KR_Input(self, target_element):
        switchLanguage("KR")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\NL\\") + os.listdir(os.path.join(rootPath, "data\\input\\NL"))[0]))
    def test_NL_Input(self, target_element):
        switchLanguage("NL")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\NO\\") + os.listdir(os.path.join(rootPath, "data\\input\\NO"))[0]))
    def test_NO_Input(self, target_element):
        switchLanguage("Norwegian")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\PL\\") + os.listdir(os.path.join(rootPath, "data\\input\\PL"))[0]))
    def test_PL_Input(self, target_element):
        switchLanguage("PL")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\PO\\") + os.listdir(os.path.join(rootPath, "data\\input\\PO"))[0]))
    def test_PO_Input(self, target_element):
        switchLanguage("PO")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\RO\\") + os.listdir(os.path.join(rootPath, "data\\input\\RO"))[0]))
    def test_RO_Input(self, target_element):
        switchLanguage("RO")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\RU\\") + os.listdir(os.path.join(rootPath, "data\\input\\RU"))[0]))
    def test_RU_Input(self, target_element):
        switchLanguage("RU")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\SC\\") + os.listdir(os.path.join(rootPath, "data\\input\\SC"))[0]))
    def test_SC_Input(self, target_element):
        switchLanguage("SC")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\SH\\") + os.listdir(os.path.join(rootPath, "data\\input\\SH"))[0]))
    def test_SH_Input(self, target_element):
        switchLanguage("SH")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\SK\\") + os.listdir(os.path.join(rootPath, "data\\input\\SK"))[0]))
    def test_SK_Input(self, target_element):
        switchLanguage("SK")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\SL\\") + os.listdir(os.path.join(rootPath, "data\\input\\SL"))[0]))
    def test_SL_Input(self, target_element):
        switchLanguage("SL")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\SP\\") + os.listdir(os.path.join(rootPath, "data\\input\\SP"))[0]))
    def test_SP_Input(self, target_element):
        switchLanguage("SP")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\SV\\") + os.listdir(os.path.join(rootPath, "data\\input\\SV"))[0]))
    def test_SV_Input(self, target_element):
        switchLanguage("SV")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\TC\\") + os.listdir(os.path.join(rootPath, "data\\input\\TC"))[0]))
    def test_TC_Input(self, target_element):
        switchLanguage("TC")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\TU\\") + os.listdir(os.path.join(rootPath, "data\\input\\TU"))[0]))
    def test_TU_Input(self, target_element):
        switchLanguage("TU")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.input
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\input\\UA\\") + os.listdir(os.path.join(rootPath, "data\\input\\UA"))[0]))
    def test_UA_Input(self, target_element):
        switchLanguage("UA")
        jump_to_input_page = Jump_T0_Input_Page_win()
        result = jump_to_input_page.jump_to_input_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\AR\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\AR"))[0]))
    def test_AR_Advanced(self, target_element):
        switchLanguage("AR")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\BR\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\BR"))[0]))
    def test_BR_Advanced(self, target_element):
        switchLanguage("BR")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\CR\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\CR"))[0]))
    def test_CR_Advanced(self, target_element):
        switchLanguage("CR")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\CZ\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\CZ"))[0]))
    def test_CZ_Advanced(self, target_element):
        switchLanguage("CZ")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\DK\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\DK"))[0]))
    def test_DK_Advanced(self, target_element):
        switchLanguage("DK")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\FI\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\FI"))[0]))
    def test_FI_Advanced(self, target_element):
        switchLanguage("FI")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\FR\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\FR"))[0]))
    def test_FR_Advanced(self, target_element):
        switchLanguage("FR")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\GK\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\GK"))[0]))
    def test_GK_Advanced(self, target_element):
        switchLanguage("GK")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\GR\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\GR"))[0]))
    def test_GR_Advanced(self, target_element):
        switchLanguage("GR")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\HE\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\HE"))[0]))
    def test_HE_Advanced(self, target_element):
        switchLanguage("HE")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\HU\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\HU"))[0]))
    def test_HU_Advanced(self, target_element):
        switchLanguage("HU")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\IT\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\IT"))[0]))
    def test_IT_Advanced(self, target_element):
        switchLanguage("IT")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\JP\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\JP"))[0]))
    def test_JP_Advanced(self, target_element):
        switchLanguage("JP")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\KR\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\KR"))[0]))
    def test_KR_Advanced(self, target_element):
        switchLanguage("KR")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\NL\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\NL"))[0]))
    def test_NL_Advanced(self, target_element):
        switchLanguage("NL")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\NO\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\NO"))[0]))
    def test_NO_Advanced(self, target_element):
        switchLanguage("Norwegian")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\PL\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\PL"))[0]))
    def test_PL_Advanced(self, target_element):
        switchLanguage("PL")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\PO\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\PO"))[0]))
    def test_PO_Advanced(self, target_element):
        switchLanguage("PO")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\RO\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\RO"))[0]))
    def test_RO_Advanced(self, target_element):
        switchLanguage("RO")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\RU\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\RU"))[0]))
    def test_RU_Advanced(self, target_element):
        switchLanguage("RU")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\SC\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\SC"))[0]))
    def test_SC_Advanced(self, target_element):
        switchLanguage("SC")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\SH\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\SH"))[0]))
    def test_SH_Advanced(self, target_element):
        switchLanguage("SH")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\SK\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\SK"))[0]))
    def test_SK_Advanced(self, target_element):
        switchLanguage("SK")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\SL\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\SL"))[0]))
    def test_SL_Advanced(self, target_element):
        switchLanguage("SL")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\SP\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\SP"))[0]))
    def test_SP_Advanced(self, target_element):
        switchLanguage("SP")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\SV\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\SV"))[0]))
    def test_SV_Advanced(self, target_element):
        switchLanguage("SV")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\TC\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\TC"))[0]))
    def test_TC_Advanced(self, target_element):
        switchLanguage("TC")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\TU\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\TU"))[0]))
    def test_TU_Advanced(self, target_element):
        switchLanguage("TU")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True

    @pytest.mark.advanced
    @pytest.mark.parametrize('target_element', Json_to_Python(
        os.path.join(rootPath, "data\\advanced\\UA\\") + os.listdir(os.path.join(rootPath, "data\\advanced\\UA"))[0]))
    def test_UA_Advanced(self, target_element):
        switchLanguage("UA")
        jump_to_advanced_settings_page = Jump_T0_Advanced_Settings_Page_win()
        result = jump_to_advanced_settings_page.jump_to_advanced_settings_page(target_element[0])
        assert result is True



