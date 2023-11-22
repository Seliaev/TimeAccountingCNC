import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename  # Import secure_filename for filename sanitization
from utils.qr_utils.qr_reader import QRReader

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

post_task_bp = Blueprint('post_task', __name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@post_task_bp.route("/post_task", methods=['GET', 'POST'])
def post_task() -> str:
    """
    Обработка запроса на создание заявки по QR-коду станка.

    Returns:
        str: HTML-страница с запросом создания заявки.
    """
    if request.method == 'POST':
        qr_image = request.files.get('qr_image')
        if qr_image and allowed_file(qr_image.filename):
            filename = secure_filename(qr_image.filename)
            qr_image_path = os.path.join('server', 'static', 'uploads', filename)
            qr_image.save(qr_image_path)
            qr_reader = QRReader(qr_image_path)
            qr_data = qr_reader.__str__()
            if qr_data is not None:
                return render_template("post_task.html", name_machine=qr_data.get('name'))
    return render_template("post_task.html")
