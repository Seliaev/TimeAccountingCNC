import os


class Config:
    """
    Конфиг для sqlalchemy, sqlite
    """
    path = os.path.join(os.getcwd(), 'database', 'site.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
