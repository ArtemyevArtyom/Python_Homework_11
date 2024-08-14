"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

ARGS = [["ping", "yandex.ru"], ["ping", "youtube.com"]]
for el in ARGS:
    PINGS = subprocess.Popen(el, stdout=subprocess.PIPE)
    print(PINGS.stdout)
    for line in PINGS.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding'])
        print(line)
    print('-'*70)
