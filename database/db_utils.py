from datetime import datetime
from typing import List

from database.base import db, Task

def create_machine(name_machine: str) -> None:
    """
    Создает новый станок в базе данных или обновляет время существующего станка.

    Args:
        name_machine (str): Название станка.

    Example:
        create_machine('Новый Станок')
    """
    existing_task = Task.query.filter_by(name=name_machine).first()

    if existing_task:
        existing_task.date = datetime.now()
        db.session.commit()
    else:
        new_task = Task(name=name_machine)
        db.session.add(new_task)
        db.session.commit()


def change_task(name_machine: str, new_status: str) -> bool:
    """
    Изменяет статус существующего станка в базе данных.

    Args:
        name_machine (str): Название станка.
        new_status (str): Новый статус для станка.

    Returns:
        bool: True, если станок найден и успешно изменен статус; False в противном случае.

    Example:
        change_task('Мой Станок', 'В ремонте')
    """
    from datetime import datetime
    task = Task.query.filter_by(name=name_machine).first()

    if task:
        task.status = new_status
        task.date = datetime.now()
        db.session.commit()
        return True
    else:
        return False


def get_machine(name_machine: str) -> Task or bool:
    """
    Получает информацию о станке из базы данных по названию.

    Args:
        name_machine (str): Название станка.

    Returns:
        Task or bool: Объект информации о станке, если найден; False в противном случае.

    Example:
        task = get_machine('Мой Станок')
    """
    task = Task.query.filter_by(name=name_machine).first()
    if task:
        return task
    else:
        return False


def get_all_machines() -> List[Task]:
    """
    Получает все записи о станках из базы данных.

    Returns:
        List[Task]: Список объектов информации о станках.

    Example:
        all_machines = get_all_machines()
    """
    machines = Task.query.all()
    return machines

