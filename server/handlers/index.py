from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


@index_bp.route("/")
def index() -> str:
    """
    Главная страница приложения.

    Returns:
        str: HTML-страница с кнопками для перехода к отправке и чтению заявок а также созданию QR-кодов.
    """
    return render_template("index.html")
