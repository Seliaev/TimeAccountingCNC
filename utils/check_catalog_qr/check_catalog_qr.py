import os
from typing import List


def check_catalog_qr() -> List[str] or FileNotFoundError:
    """
    Проверяет наличие каталога с QR-кодами.

    Returns:
        List[str]: Список имен файлов в каталоге с QR-кодами.

    Raises:
        FileNotFoundError: Если каталог не найден.
    """
    try:
        uploads_path = os.path.join(os.getcwd(), 'server', 'static', 'uploads')
        return os.listdir(uploads_path)
    except FileNotFoundError:
        raise FileNotFoundError
