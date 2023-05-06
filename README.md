# log-parsing-excercise

Задача с собеседования. Условия:

- В директории `logs/` может храниться любое количество лог-файлов.
- Каждая строчка начинается с даты в формате `20211118101717` (`YYYYMMDDHHMMSS`).
- В каждом файле даты идут по порядку. Но даты в файлах могут пересекаться.

Задание:
- Написать программу, которая получает на входе начальную и конечную даты, и выдает все строчки из всех файлов, которые попадают в указанный интервал.
- Вывод должен происходить в порядке возрастания даты.
- Нужно написать тело функции `parse_logs`, при необходимости добавляя вспомогательные функции.

Для тестирования решения необходимо сгенерировать данные:

```shell
python3 gen.py
```

## License

[WTFPL](http://www.wtfpl.net)

