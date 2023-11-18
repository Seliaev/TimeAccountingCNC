class QRGenerator:
    """
    Класс QRGenerator создает QR-код на основе предоставленных данных и сохраняет его в изображение.

    Attributes:
        __qr (QRCode): Объект QRCode для генерации QR-кода.
        __data (Dict): Словарь с данными, которые будут закодированы в QR-код.
        __img: (Image): Объект изображения сгенерированного QR-кода.

    Methods:
        __init__(self, data: Dict) -> None:
            Инициализирует объект QRGenerator с предоставленными данными.

    Example:
        data = {
            'name': 'EP-1030',
            'status': 'Emergency',
            'date': '01.01.2021',
            'time': '12:00:00',
            'trouble': 'Error with motor'
        }
        directory = "../../utils/qr_images/"
        qr_generator = QRGenerator(directory, data) | QRGenerator(directory, data)
    """
    from typing import Dict
    __slots__ = ('__qr', '__data', '__img', '__file_name')

    def __init__(self, directory: str, data: Dict) -> None:
        from qrcode import QRCode
        from os.path import exists

        if not exists(directory):
            from os import makedirs
            makedirs(directory)

        self.__qr = QRCode()
        self.__qr.add_data(data)
        self.__qr.make(fit=True)
        self.__img = self.__qr.make_image(fill_color="black", back_color="white")
        self.__file_name = f"{directory}my_qrcode_{data['name']}.png"
        self.__img.save(self.__file_name)

    def get_filename(self):
        return self.__file_name[6:]





