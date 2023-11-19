from flask import Blueprint, render_template

from database.db_utils import get_all_machines
from utils.accounting_time.elapsed_time import calculate_elapsed_time
from utils.check_catalog_qr.check_catalog_qr import check_catalog_qr

time_statistics_bp = Blueprint('time_statistics', __name__)


@time_statistics_bp.route("/time_statistics")
def time_statistics():
    """
    Страница для отображения статистики по времени работы или простоя станка.

    Returns:
        str: HTML-страница с временной статистикой.
    """
    try:
        check_catalog_qr()
        tasks = get_all_machines()
        for task in tasks:
            task.elapsed_time = calculate_elapsed_time(task.date)
        return render_template("time_statistics.html", tasks=tasks)
    except FileNotFoundError:
        files_not_found = f"В базе нет станков"
        return render_template("task_page.html", files_not_found=files_not_found)
