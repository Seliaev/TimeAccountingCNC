# Статус и время работы станков 

Создание и отслеживание заявок для ремонта станков.
Отслеживание времени текущено статуса.

## Структура проекта

```plaintext
.
├── server                # Код серверной части
│   ├── app.py            # Приложение flask
│   ├── handlers          # Обработчики запросов
│   └── templates         # HTML-шаблоны
├── database              # Работа с базой данных
├── utils                 # Вспомогательные утилиты
│   ├── accounting_time   # Рассчет времени работы текущего статуса.
│   ├── check_catalog_qr  # Проверка папки для QR-кодов
│   └── qr_utils          # Сервисы создания и чтения QR-кода + тесты этих сервисов
├── requirements.txt      # Зависимости проекта
└── README.md             # Документация проекта
```

## Используемые библиотеки
```plaintext
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
opencv-python==4.8.1.78
qrcode==7.4.2
```

Демо версия с выводом в html файл.
http://aicat.ru:5334/


# Status and Operation Time of Machines

Creation and tracking of repair requests for machines.
Monitoring the time in the current status.

## Project Structure

```plaintext
.
├── server                # Server-side code
│   ├── app.py            # Flask application
│   ├── handlers          # Request handlers
│   └── templates         # HTML templates
├── database              # Database operations
├── utils                 # Auxiliary utilities
│   ├── accounting_time   # Calculation of operation time in the current status
│   ├── check_catalog_qr  # Check for the QR code folder
│   └── qr_utils          # Services for creating and reading QR codes + tests for these services
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Used Libraries
```plaintext
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
opencv-python==4.8.1.78
qrcode==7.4.2
```

Demo version with output to an html file.
http://aicat.ru:5334/
