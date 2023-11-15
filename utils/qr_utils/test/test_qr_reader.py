import unittest
from utils.qr_utils.qr_reader import QRReader
from utils.qr_utils.qr_generator import QRGenerator


class TestQRCode(unittest.TestCase):
    """
    Класс тестов для проверки генерации и чтения QR-кода.

    Attributes:
        __test_data (Dict): Тестовые данные для генерации QR-кода.
        __directory (str): Директория для сохранения временных файлов.
        __temp_file (str): Имя временного файла QR-кода.
        __path (str): Полный путь к временному файлу QR-кода.
    """
    @classmethod
    def setUpClass(cls):
        """Настройка тестового окружения."""
        cls.__test_data = {
            'name': 'EP-1030',
            'status': 'Emergency',
            'date': '01.01.2021',
            'time': '12:00:00',
            'trouble': 'Error with motor'
        }
        cls.__directory = "../../utils/qr_images/"
        cls.__temp_file = f"my_qrcode_{cls.__test_data['name']}.png"
        cls.__path = f"{cls.__directory}{cls.__temp_file}"

    @classmethod
    def tearDownClass(cls):
        """Завершение тестового окружения после выполнения всех тестов."""
        from os import remove
        remove(cls.__path)

    def test_qr_generator(self):
        """
        Проверка генерации QR-кода.
        Проверяет создался ли файл, по наличию.
        """
        from os.path import exists
        QRGenerator(directory=self.__directory, data=self.__test_data)
        self.assertTrue(exists(self.__path))

    def test_qr_reading(self):
        """
        Проверка чтения QR-кода.
        Сравнивает словари
        """
        qr_reader = QRReader(self.__path)
        dict_data_from_qr = qr_reader.__str__()
        self.assertDictEqual(dict_data_from_qr, self.__test_data)


if __name__ == '__main__':
    unittest.main()

