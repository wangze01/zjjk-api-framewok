      # zjjk_api_demo
      公司目前在使用接口自动化框架，该项目为第一版，能够快速用到日常工作中，已经隐藏内部敏感信息。
      
      项目说明

      这是一个关于python的接口API自动化测试的项目，本项目实现接口自动化的技术选型Python+Requests+Pytest+Allure。
      通过excel进行数据驱动，对测试用例进行管理。
      封装requests的方法，测试用例中，只需一行代码即可完成输入的请求参数，获得响应内容使用 Allure 来生成测试报告。
      通过对数据库进行封装，增加数据校验的准确性。
      接口自动化进行Jenkins持续集成

	

	 
	 
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

