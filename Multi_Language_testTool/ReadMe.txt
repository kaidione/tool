多语言测试说明
环境包括appium+WindowsApplicationDriver+SDK+JDK+NODE+ALLURE
(！！！！！一定要打开开发者选项)
1.在目录Multi_Language_testTool中找到对应的exe安装 WindowsApplicationDriver
2.自查是否有以下环境变量，增加缺失的环境变量：（以下路径仅供参考，具体根据文件实际路径进行配置，指定的bat文件会自动识别文件路径）
	F:\Multi_Language_testTool\runEnvironment\npm（可手动添加路径到path，也可 以管理员权限运行该目录下的appium_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\allure-2.20.1\bin（可手动添加路径到path，也可 以管理员权限运行allure-2.20.1目录下的allure_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\android-sdk-windows-appium\build-tools\28.0.3（可手动添加路径到path，也可 以管理员权限运行该路径下的SDK_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\android-sdk-windows-appium\platform-tools（可手动添加路径到path，也可 以管理员权限运行该路径下的SDK_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\android-sdk-windows-appium\tools\bin（可手动添加路径到path，也可 以管理员权限运行该路径下的SDK_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\jdk1.8.0_171\bin（可手动添加路径到path，也可 以管理员权限运行该路径下的JDK_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\jdk1.8.0_171\jre\bin（可手动添加路径到path，也可 以管理员权限运行该路径下的JDK_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\node（可手动添加路径到path，也可 以管理员权限运行该路径下的NODE_path_system.bat自动添加）
	F:\Multi_Language_testTool\runEnvironment\node\node_modules（可手动添加路径到path，也可 以管理员权限运行该路径下的NODE_path_system.bat自动添加）

到这环境准备ok

最常使用的三个目录：（多语言测试包目前仅支持json文件格式，其他格式后续开发）
	F:\Multi_Language_testTool\Multi_Language\data\power（这里存放的是在power页面的多语言测试包，不同页面的测试内容替换对应文件夹的内容即可）
	F:\Multi_Language_testTool\Multi_Language\report（当测试程序运行完之后自动生成测试报告，查看报告的方式在cmd中切到该目录下输入命令 （allure open ./） 然后回车即可）
	F:\Multi_Language_testTool\Multi_Language目录下有pytest.ini文件（以记事本打开可以看到命令：addopts = -vs --alluredir=./temps --clean-alluredir -p no:faulthandler -m power --reruns=1 --reruns-delay=3，-m后面的power是需要测试内容所在页面，例如：测试的多语言在audio页面，需要将这个文件的power改成audio）

注意：当前测试的语言有29种，如果需要测试多语言不支持某个国家，请不要将这个国家存放的测试内容删掉，因为可能会因为某个语言包丢失导致影响到其他语言的测试

了解了上面的内容，接下来可以开始测试多语言了
开始测试多语言的方法：F:\Multi_Language_testTool\Multi_Language（找到该目录运行Multi_Launguage.exe即可）