from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    """
    Модель для представления информации о станках в базе данных.

    Attributes:
        id (int): Уникальный идентификатор.
        name (str): Название станка.
        date (datetime): Дата и время начала статуса.
        status (str): Статус станка.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(100), default='Работает', nullable=False)
