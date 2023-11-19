import os
from flask import Blueprint, render_template, request
from utils.qr_utils.qr_reader import QRReader

post_task_bp = Blueprint('post_task', __name__)


@post_task_bp.route("/post_task", methods=['GET', 'POST'])
def post_task() -> str:
    """
    Обработка запроса на создание заявки по QR-коду cтанка.

    Returns:
        str: HTML-страница с запросом создания заявки.
    """
    if request.method == 'POST':
        qr_image = request.files.get('qr_image')
        if qr_image:
            qr_image_path = os.path.join('server', 'static', 'uploads', qr_image.filename)
            qr_image.save(qr_image_path)
            qr_reader = QRReader(qr_image_path)
            qr_data = qr_reader.__str__()
            return render_template("post_task.html", name_machine=qr_data.get('name'))
    return render_template("post_task.html")
