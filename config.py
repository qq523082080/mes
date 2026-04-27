import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / 'instance'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'workshop-secret-key-2024')
    
    # 数据库配置 - 支持 MySQL / SQLite 切换
    DB_TYPE = os.environ.get('DB_TYPE', 'mysql')  # mysql, sqlite
    
    if DB_TYPE == 'mysql':
        # MySQL 配置（请修改为您的实际配置）
        MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
        MYSQL_PORT = os.environ.get('MYSQL_PORT', '3306')
        MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
        MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '52qq1314')
        MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'workshop_db')
        
        SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4'
        
        # MySQL 连接池配置
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size': 20,           # 连接池大小
            'pool_recycle': 3600,      # 连接回收时间（秒）
            'pool_pre_ping': True,     # 连接前检测
            'max_overflow': 30,        # 最大溢出连接
            'pool_timeout': 30,        # 获取连接超时
        }
    else:
        # SQLite 配置（开发/测试用）
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{INSTANCE_DIR / "workshop.db"}'
        SQLALCHEMY_ENGINE_OPTIONS = {}
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 分页配置
    ITEMS_PER_PAGE = 20
    
    # 静态文件目录
    STATIC_DIR = BASE_DIR / 'app' / 'static'