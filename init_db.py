#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据库初始化脚本
首次运行或需要重置数据库时执行
"""

import os
import sys

# 设置环境变量使用MySQL
os.environ['DB_TYPE'] = 'mysql'

from app import create_app
from app.extensions import db
from app.models import User, UserProductConfig
from app.quality1.models import Quality1Record
from app.quality2.models import Quality2Record
from app.quality3.models import Quality3Record
from app.quality4.models import Quality4Record

def init_database():
    """初始化数据库"""
    app = create_app()
    
    with app.app_context():
        # 创建所有表
        db.create_all()
        
        # 检查是否已有admin用户
        admin_exists = User.query.filter_by(username='admin').first()
        
        if not admin_exists:
            # 创建管理员用户
            admin = User(
                username='admin',
                role='super_admin'
            )
            admin.set_password('password')
            db.session.add(admin)
            db.session.commit()
            print("✅ 管理员账号创建成功: admin / password")
        else:
            print("✅ 管理员账号已存在")
        
        # 检查是否已有admin配置
        admin_config = UserProductConfig.query.get('admin')
        if not admin_config:
            admin_config = UserProductConfig(
                username='admin',
                config='{"products":[]}',
                suppliers='[]'
            )
            db.session.add(admin_config)
            db.session.commit()
            print("✅ 管理员配置创建成功")
        else:
            print("✅ 管理员配置已存在")
        
        print("=" * 50)
        print("数据库初始化完成！")
        print("=" * 50)

if __name__ == '__main__':
    init_database()