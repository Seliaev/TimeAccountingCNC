from database.base import db, Task


def create_machine(name_machine):
    task = Task(name=name_machine)
    db.session.add(task)
    db.session.commit()


def change_task(name_machine, new_status):
    from datetime import datetime
    task = Task.query.filter_by(name=name_machine).first()

    if task:
        # Изменяем статус
        task.status = new_status
        # Изменяем дату и время на текущие
        task.date = datetime.now()
        # Сохраняем изменения в базе данных
        db.session.commit()
        return True  # Успешно изменено
    else:
        return False  # Запись не найдена


def get_machine(name_machine):
    # Получаем запись из базы данных по ее идентификатору
    task = Task.query.filter_by(name=name_machine).first()
    if task:
        return task
    else:
        return False  # Запись не найдена


