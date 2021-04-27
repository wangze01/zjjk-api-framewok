      # python_api_demo
      这是一个关于python的接口API自动化测试的项目，本项目实现接口自动化的技术选型Python+Requests+Pytest+Allure。
	  通过excel进行数据驱动，对测试用例进行管理。
	  封装requests的方法，测试用例中，只需一行代码即可完成输入的请求参数，获得响应内容使用 Allure 来生成测试报告。
	  通过对数据库进行封装，增加数据校验的准确性。
	
	https://blog.csdn.net/changyixue/article/details/105362848
	
	https://www.bilibili.com/video/BV1ex411x7Em
	
	学习的路线
     1.python基础
		循环         --for循环/if/else
		函数         --形参/实参/return/嵌套调用
		高级数据类型 --元组/字典/列表遍历
		模块         --__name__/import
		面向对象属性 --多继承/父类方法/类属型/类方法
		异常         --捕获/抛出异常
		文件         --读取/写入文件
		封装		--模块管理函数就是将函数的定义放到一个.py文件中.可以在其他.py文件中通过import关键字导入模块.导入
				      后就可以使用模块名+函数名的方式去使用其他模块中的函数.

	2.HTTP协议
		请求头/响应/请求方法/状态码
		扩展params /data
		
	3.JSON数据格式
		JSON语法规则，JSON数据类型 eval函数
	
	4.Requests模块基础
		读源代码 使用
	
	5.Python+Requests+Pytest+Allure。框架的学习/读已完成的代码。
	 
	 
	 项目架构目录：
      .
      |-- Case
      |   |-- conftest.py
      |   |-- __init__.py
      |   |-- logincase
      |   |   |-- conftest.py
      |   |   |-- __init__.py
      |   |   `-- test_login.py
      |   `-- usercase
      |       |-- conftest.py
      |       |-- __init__.py
      |       `-- test_user.py
      |-- Common
      |   |-- conf
      |   |   |-- env_config.ini
      |   |   `-- __init__.py
      |   |-- __init__.py
      |   `-- plugs
      |       |-- get_config.py
      |       |-- get_db.py
      |       |-- get_excle.py
      |       |-- get_globals_data.py
      |       |-- get_log.py
      |       |-- http_requests.py
      |       `-- __init__.py
      |-- OutPut
      |   `-- log
      |       `-- xx-xx-xx.log
      `-- TestData
          |-- case.xlsx
          `-- __init__.py

