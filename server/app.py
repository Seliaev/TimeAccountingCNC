from flask import Flask
from database.base import db
from database.config import Config

app = Flask(__name__)

UPLOAD_FOLDER = 'server/static/uploads'  # Каталог для хранения сгенерированных картинок с QR-кодами
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(Config)
db.init_app(app)

def start_app() -> Flask:
    """
    Запуск приложения Flask.
    Установка хендлеров.
    Создание БД

    Return:
        Flask  - app
    """
    from server.handlers.index import index_bp
    from server.handlers.generate_qr import generate_qr_bp
    from server.handlers.post_task import post_task_bp
    from server.handlers.set_task import set_task_bp
    from server.handlers.task_page import task_page_bp
    from server.handlers.edit_status import edit_status_bp
    from server.handlers.time_statistics import time_statistics_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(generate_qr_bp)
    app.register_blueprint(post_task_bp)
    app.register_blueprint(set_task_bp)
    app.register_blueprint(task_page_bp)
    app.register_blueprint(edit_status_bp)
    app.register_blueprint(time_statistics_bp)

    with app.app_context():
        db.create_all()

    return app
