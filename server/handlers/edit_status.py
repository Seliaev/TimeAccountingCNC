from flask import Blueprint, render_template, request

from database.db_utils import change_task

edit_status_bp = Blueprint('edit_status', __name__)


@edit_status_bp.route("/edit_status", methods=['POST'])
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
