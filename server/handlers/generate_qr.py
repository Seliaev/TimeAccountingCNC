from flask import Blueprint, render_template,  request, current_app
from database.db_utils import create_machine
from utils.qr_utils.qr_generator import QRGenerator

generate_qr_bp = Blueprint('generate_qr', __name__)


@generate_qr_bp.route("/generate_qr", methods=["GET", "POST"])
def generate_qr() -> str:
    """
    Обработка запроса на генерацию QR-кода.

    Returns:
        str: HTML-страница с изображением после генерации QR-кода.
    """
    name = request.form.get("name")
    if name:
        create_machine(name)
        data_qr = {'name': name}
        upload_folder = current_app.config['UPLOAD_FOLDER']
        qr_code = QRGenerator(directory=f"{upload_folder}/", data=data_qr)
        qr_path = qr_code.get_filename()
        return render_template("generate.html", qr_name=name, qr_path=qr_path)
    return render_template("generate.html")
