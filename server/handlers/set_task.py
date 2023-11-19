from flask import Blueprint, render_template, request
from database.db_utils import change_task

set_task_bp = Blueprint('set_task', __name__)


@set_task_bp.route("/set_task", methods=['POST'])
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
