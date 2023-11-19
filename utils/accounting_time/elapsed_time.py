from datetime import datetime


def calculate_elapsed_time(task_date: datetime) -> str:
    """
    Рассчитывает время, прошедшее с момента назначения статуса до текущего момента.

    Attributes:
        task_date (datetime): Дата, относительно которой рассчитывается прошедшее время.

    Returns:
        str: Строка с информацией о времени в формате "Дни: 30. Часы: 20. Минуты 10.".
    """
    current_time = datetime.now()
    elapsed_time = current_time - task_date

    days = elapsed_time.days
    hours, remainder = divmod(elapsed_time.seconds, 3600)
    minutes = remainder // 60

    return f"Дни: {days}. Часы: {hours}. Минуты {minutes}."
