# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

import pytest
from allure_pytest import plugin as allure_plugin
import pytest_rerunfailures
import pytest_repeater as repeat


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # args = ['-s', '-v', '--count=3', '--alluredir=allure_result', test_path]
    pytest.main(plugins=[allure_plugin, repeat, pytest_rerunfailures])
    # pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./report --clean")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
