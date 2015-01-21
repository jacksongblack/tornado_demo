# encoding:utf-8
import os
# 项目根目录配置
BASE_DIR = os.path.dirname(__file__)
# 模板文件根目录配置
TEMPLATE_DIR = ''.join((BASE_DIR, "/template/"))
# 静态文件根目录配置
STATIC_DIR = ''.join((BASE_DIR, '/static/'))
# 运行IP与端口配置
ADDRESS = {
    'port': '3000',
    'ip': '127.0.0.1'
}
# 单元测试文件目录
TEST_DIR = ''.join((BASE_DIR, '/tests/'))

# MYSQL配置
MYSQL_SETTINGS = {
    'host': "127.0.0.1:3306",
    'database_name': "crm",
    'username': "root",
    'password': "root"
}
# redis配置

REDIS_SETTINGS = {
    'host': "127.0.0.1",
    'port': "6379",
}
# 安全cookie设置
COOKIE_SECRET = 'unicode'
XSRF_COOKIE = True
LOGIN_URL = "/login"