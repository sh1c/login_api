
1.下载git(https://git-scm.com/)
2.下载postman(https://www.postman.com/downloads/)
3.下载pycharm(https://www.jetbrains.com/pycharm/)
4.新建文件,打开控制台,定位到该文件夹路径
5.输入(git https://github.com/sh1c/login_api) 克隆python代码到该文件夹
6.构建虚拟环境,导航到复制到的文件夹处(cd path/to/your/project),创建虚拟环境(python3 -m venv venv),激活虚拟环境(.\venv\Scripts\activate)
7.导入Flask充当api框架(pip insatll Flask)
8.启动代码(python LOG_IN.py)
9.打开postman,创建一个新的请求或集合（Collection),输入API的URL(http://127.0.0.1:5000/login)
10.选择相应的HTTP方法（POST）
11.在body标签下选择raw,JSON格式,输入{"username":"任意名称","psw":"任意密码"}后点击send,即可在下方输出相应状态
12.退出虚拟环境(deactivate)

由于该API数据库内用户数据有限,若要增加用户名称和密码,可在pycharm进行修改和添加

