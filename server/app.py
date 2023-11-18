from flask import Flask, render_template, request
from database.base import db
from database.db_utils import get_machine, create_machine, change_task
from utils.qr_utils.qr_reader import QRReader
from utils.qr_utils.qr_generator import QRGenerator
from database.config import Config
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads' # Каталог для хранения сгенерированных картинок с QR-кодами
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(Config)
db.init_app(app)


@app.route("/")
def index() -> str:
    """
    Главная страница приложения.

    Returns:
        str: HTML-страница с кнопками для перехода к отправке и чтению заявок а также созданию QR-кодов.
    """
    return render_template("index.html")


@app.route("/post_task", methods=['GET', 'POST'])
def post_task() -> str:
    """
    Обработка запроса на создание заявки по QR-коду cтанка.

    Returns:
        str: HTML-страница с запросом создания заявки.
    """
    if request.method == 'POST':
        qr_image = request.files.get('qr_image')
        if qr_image:
            qr_image_path = os.path.join("static", "uploads", qr_image.filename)
            qr_image.save(qr_image_path)
            qr_reader = QRReader(qr_image_path)
            qr_data = qr_reader.__str__()
            return render_template("post_task.html", name_machine=qr_data.get('name'))
    return render_template("post_task.html")


@app.route("/set_task", methods=['POST'])
def set_task() -> str:
    """
    Обработка запроса на установку статуса заявки.

    Returns:
        str: HTML-страница с результатами установки статуса заявки.
    """
    return_status = "Ошибка: Некорректный запрос."
    if request.method == 'POST':
        name_machine = request.form.get('name_machine')
        new_status = request.form.get('new_status')
        if name_machine and new_status:
            success = change_task(name_machine, new_status)
            if success:
                return_status = "Заявка отправлена в ремонтную службу. Ожидайте."
            else:
                return_status = "Ошибка: Станок не найден в базе данных."
    return render_template("post_task.html", return_status=return_status)



@app.route("/generate_qr", methods=["GET", "POST"])
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
        qr_code = QRGenerator(directory=f"{app.config['UPLOAD_FOLDER']}/", data=data_qr)
        qr_path = qr_code.get_filename()
        return render_template("generate.html", qr_name=name, qr_path=qr_path)
    return render_template("generate.html")


@app.route("/task_page", methods=['GET', 'POST'])
def task_page() -> str:
    """
    Страница для просмотра заявки.

    Returns:
        str: HTML-страница с информацией о задаче.
    """
    try:
        uploads_path = os.path.join(os.getcwd(), 'static', 'uploads')
        files_in_uploads = os.listdir(uploads_path)
        if request.method == 'POST':
            selected_file = request.form.get('selected_file')
            if selected_file:
                name_machine = selected_file.split('_')[-1][:-4]
                task = get_machine(name_machine)
                if task:
                    return_data = f"""
                        Станок: {task.name}<br/>
                        Дата: {task.date.strftime('%Y-%m-%d')}<br/>
                        Время: {task.date.strftime('%H:%M:%S')}<br/>
                        Статус: {task.status}<br/>
                    """
                else:
                    return_data = f"Станок с именем {name_machine} не найден в базе данных."
                return render_template("task_page.html", files_in_uploads=files_in_uploads, return_data=return_data, name_machine=(task.name or None))
        return render_template("task_page.html", files_in_uploads=files_in_uploads)
    except FileNotFoundError:
        files_not_found = f"В базе нет станков"
        return render_template("task_page.html", files_not_found=files_not_found)


@app.route("/edit_status", methods=['POST'])
def edit_status() -> str:
    """
    Страница для редактирования статуса заявки.

    Returns:
        str: HTML-страница с результатом смены статуса заявки.
    """
    return_status = "Ошибка: Некорректный запрос."
    if request.method == 'POST':
        name_machine = request.form.get('name_machine')
        new_status = request.form.get('new_status')
        if name_machine and new_status:
            success = change_task(name_machine, new_status)
            if success:
                return_status = "Статус успешно отредактирован."
            else:
                return_status = "Ошибка: Станок не найден в базе данных."
    return render_template("task_page.html", return_status=return_status)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
