#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
生产环境启动脚本 - 使用 Waitress 服务器
"""

import os

# 设置使用 MySQL
os.environ['DB_TYPE'] = 'mysql'

from waitress import serve
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 50)
    print("生产车间质量数据登记系统 - 生产模式")
    print("数据库类型: MySQL")
    print("Web服务器: Waitress (4线程)")
    print("访问地址: http://localhost:5010")
    print("=" * 50)
    
    serve(app, host='0.0.0.0', port=5010, threads=4)