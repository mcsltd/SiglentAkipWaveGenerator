# _

Скрипт генерации (интерполяции) волн по контрольным точкам

# Требования

Для запуска необходим [Python](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe) (версии 3.0 или выше) и пакет [numpy](https://numpy.org/).

Установить пакет `numpy` можно следующей командой

    $ pip install numpy

# Использование скрипта

Для генерации волны необходимо подготовить файл с контрольными точками, между которыми будет интерполироваться сигнал. Файл должен иметь формат CSV и содержать два столбца со значениями X и Y точек. Файл _не должен_ содержать заголовки и т.п. Пример входного файла: [./data/input.csv](./data/input.csv).  
Для запуска скрипта выполните следующую команду

    $ python wavegenerator.py path_to_input_file -l N -o path_to_result_file

- `path_to_input_file` - путь до входного файла;
- `N` - необходимое число точек в выходном файле;
- `path_to_result_file` - путь до выходного файла (если не задан, входной файл будет перезаписан).

В результате работы скрипта сосздаётся файл в формате CSV с заданным количеством точек. Пример файла [./data/result.csv](./data/result.csv).

