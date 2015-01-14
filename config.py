import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIR = ''.join((BASE_DIR, "/template/"))
STATIC_DIR = ''.join((BASE_DIR, '/static/'))

ADDRESS = {
    'port': '3000',
    'ip': '127.0.0.1'
}