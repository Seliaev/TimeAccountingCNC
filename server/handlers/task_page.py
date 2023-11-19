
from flask import Blueprint, render_template, request
from database.db_utils import get_machine
from utils.check_catalog_qr.check_catalog_qr import check_catalog_qr

task_page_bp = Blueprint('task_page', __name__)


@task_page_bp.route("/task_page", methods=['GET', 'POST'])
def task_page() -> str:
    """
    Страница для просмотра заявки.

    Returns:
        str: HTML-страница с информацией о задаче.
    """
    try:
        files_in_uploads = check_catalog_qr()
        if request.method == 'POST':
            selected_file = request.form.get('selected_file')
            if selected_file:
                name_machine = selected_file.split('_')[-1][:-4]
                task = get_machine(name_machine)
                if task:
                    return_data = f"""
                        Станок: {task.name}<br/>
                        Статус: {task.status}<br/>
                        Текущий статус с даты: {task.date.strftime('%Y-%m-%d')}<br/>
                        От времени: {task.date.strftime('%H:%M:%S')}<br/>
                    """
                else:
                    return_data = f"Станок с именем {name_machine} не найден в базе данных."
                return render_template("task_page.html", files_in_uploads=files_in_uploads, return_data=return_data,
                                       name_machine=(task.name or None))
        return render_template("task_page.html", files_in_uploads=files_in_uploads)
    except FileNotFoundError:
        files_not_found = f"В базе нет станков"
        return render_template("task_page.html", files_not_found=files_not_found)
