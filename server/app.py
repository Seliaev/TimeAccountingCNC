from flask import Flask, render_template, request
from utils.qr_utils.qr_reader import QRReader
from utils.qr_utils.qr_generator import QRGenerator
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index() -> str:
    """
    Главная страница приложения.

    Returns:
        str: HTML-страница с кнопками для перехода к генерации и чтению QR-кодов.
    """
    return render_template("index.html")


@app.route("/generate")
def generate() -> str:
    """
    Страница для генерации QR-кода.

    Returns:
        str: HTML-страница с формой для ввода данных и кнопкой для генерации QR-кода.
    """
    return render_template("generate.html")


@app.route("/read")
def read() -> str:
    """
    Страница для чтения QR-кода.

    Returns:
        str: HTML-страница с формой для загрузки фото и отображением результата чтения QR-кода.
    """
    return render_template("read.html")


@app.route("/generate_qr", methods=["POST"])
def generate_qr() -> str:
    """
    Обработка запроса на генерацию QR-кода.

    Returns:
        str: HTML-страница с результатами генерации QR-кода.
    """
    data = request.form["data"]
    if data:
        from datetime import datetime

        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%d.%m.%Y")
        current_time = current_datetime.strftime("%H:%M:%S")
        data_qr = {
            'name': 'EP-1030',
            'status': 'Emergency',
            'date': current_date,
            'time': current_time,
            'trouble': data
        }
        QRGenerator(directory=f"{app.config['UPLOAD_FOLDER']}/", data=data_qr)

        return render_template("generate.html", qr_data=data, qr_path=app.config['UPLOAD_FOLDER'])
    else:
        return render_template("generate.html")


@app.route("/read_qr", methods=["POST"])
def read_qr() -> str:
    """
    Обработка запроса на чтение QR-кода.

    Returns:
        str: HTML-страница с результатами чтения QR-кода.
    """
    if "photo" in request.files:
        photo = request.files["photo"]
        if photo:
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
            photo.save(photo_path)
            qr_data = QRReader(image_path=photo_path)
            dict_qr = qr_data.__str__()
            return_data = f"""
Станок: {dict_qr['name']}<br/>
Статус: {dict_qr['status']}<br/>
Дата: {dict_qr['date']}<br/>
Время: {dict_qr['time']}<br/>
Ошибка: {dict_qr['trouble']}
"""

            return render_template("read.html", qr_data=return_data, photo_path=photo_path)
    return render_template("read.html")


if __name__ == "__main__":
    app.run(debug=True)
