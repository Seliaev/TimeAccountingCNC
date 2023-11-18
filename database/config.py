class Config:
    """
    Конфиг для sqlalchemy, sqlite
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
