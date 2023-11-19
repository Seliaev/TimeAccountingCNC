class QRReader:
    """
    Класс QRReader предназначен для чтения данных из изображения QR-кода.

    Attributes:
        __image_path (numpy.ndarray): Изображение QR-кода.
        __detector (QRCodeDetector): Объект QRCodeDetector для декодирования QR-кода.
        __value (tuple): Кортеж с данными, полученными из QR-кода.

    Methods:
        __init__(self, image_path: str) -> None:
            Инициализирует объект QRReader с указанным путем к изображению QR-кода.

        __str__(self) -> Dict:
            Возвращает словрь с данными из QR кода.

    Пример использования:
        qr_utils = QRReader("/path/to/your/qrcode.png")
        your_dict = qr_utils.__str__()
    """
    from typing import Dict
    __slots__ = ('__image_path', '__detector', '__value')

    def __init__(self, image_path):
        from cv2 import imread, QRCodeDetector
        self.__image_path = imread(image_path)
        self.__detector = QRCodeDetector()
        self.__value = self.__detector.detectAndDecode(self.__image_path)

    def __str__(self) -> Dict:
        from ast import literal_eval
        return literal_eval(self.__value[0])


