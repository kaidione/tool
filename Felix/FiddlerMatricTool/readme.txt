1.FiddlerScheduler.exe 如果不能直接运行，以管理员运行
2.FiddlerScheduler.exe用于启动监听程序（FiddlerCoreAPIWrap.exe），限时1min
3.抓到vantage相关数据会在本级目录先生成Matrics文件，如果刚开始没有文件，会自己创建，如果有，每次运行监听是会重置内容，以确保每次的数据都是新的
4.GetResult.exe用于分析解析Matrics文件，通过加入两个参数（1.可以唯一标识目标json数据的值，2.需要获取某个值的键）来获取我们要的值 
	eg:cmd 窗口运行：GetResult.exe FeatureClick ItemName

5.获取的数据格式： !目标值!, 方便嵌入UI自动化，调用cmd运行GetResult.exe时将获取的返回值通过“!”分割来快速获取目标值

note:FiddlerScheduler.exe 无参数程序，通过定时任务来达到异步监控的效果

第一次使用时会弹出的对话框，需要选择yes