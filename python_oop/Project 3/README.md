### FAQ
В папке app/models хранятся модули, содержащие классы Resources, CPU, Storage, HDD, SSD.
В папке tests/unit хранятся тесты для каждого класса.

Для запуска тестов, необходимо установить библиотеку pytest

'''
pip install -U pytest
'''

Чтобы запустить тест необходимо написать команду:

'''
python -m pytest tests/unit/*название файла*.py
'''