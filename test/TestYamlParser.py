import unittest
import os
from yaml_parser.YamlParser import *

"""
cases:
- wrong extension
- file is not exists
- file not contains a correct content
"""


class TestYamlParser(unittest.TestCase):
    def setUp(self):
        self.parser = YamlParser()
        self.dir = os.path.dirname(os.path.abspath(__file__))

    # common situation
    def test_parse_1(self):
        code = self.parser.build(self.dir + "/../data/struct.yaml")

        expecting = {
            "graph": {
                "name": "ГКП №16",
                "childs": [
                    {"node": {"name": "Компьютеры"}},
                    {"node": {"name": "Сеть"}},
                    {"node": {"name": "Видеонаблюдение"}},
                    {"node": {"name": "МИС"}},
                    {"node": {"name": "Телефония"}},
                    {"node": {"name": "Телефония мобильная"}},
                    {"node": {"name": "Оргтехника/Картриджи"}},
                    {"node": {"name": "Прочие ИС"}},
                    {"node": {"name": "ДЛО/ЛЛО"}},
                    {"node": {"name": "1С"}},
                    {"node": {"name": "Бухгалтерия"}},
                    {"node": {"name": "ЭП/Криптография"}},
                    {"node": {"name": "Заявки в контрактную на товары и услуги"}},
                    {"node": {"name": "(Ф)РМО/(Ф)РМР"}},
                    {"node": {"name": "ВИМИС"}},
                ],
            }
        }

        self.assertEqual(expecting, self.parser.get_contents())
        self.assertEqual(code, YamlParserReturnCode.OK)

    # wrong extension
    def test_parse_2(self):
        self.assertEqual(
            self.parser.build(self.dir + "/../mock/struct.xml"),
            YamlParserReturnCode.WRONG_EXTENSION,
        )

    # file is empty
    def test_parse_3(self):
        self.assertEqual(
            self.parser.build(self.dir + "/../mock/empty.yaml"),
            YamlParserReturnCode.FILE_CONTAINS_UNEXPECTED_CONTENT,
        )

    # file does not exists
    def test_parse_4(self):
        self.assertEqual(self.parser.build(''), YamlParserReturnCode.FILE_DOES_NOT_EXISTS)
