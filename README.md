This is a simple python API for practicing
如何使用该API
1.下载git(https://git-scm.com/)
2.postman(https://www.postman.com/downloads/)
3.新建文件,打开控制台,定位到该文件夹路径
4.输入(git https://github.com/sh1c/login_api) 克隆python代码到该文件夹后打开python代码(自动在控制台运行)
5.打开postman,创建一个新的请求或集合（Collection),输入API的URL(http://127.0.0.1:5000/login)，选择相应的HTTP方法（POST）
6.在body标签下选择raw,JSON格式,输入{"username":"任意名称","psw":"任意密码"}后点击send,即可在下方输出相应状态

由于该API数据库内用户数据有限,若要增加用户名称和密码,可下载pycharm进行修改和添加

