#!/usr/bin/env python

# В директории logs/ может храниться любое количество лог-файлов.
#
# Каждая строчка начинается с даты в формате 20211118101717 (YYYYMMDDHHMMSS).
#
# В каждом файле даты идут по порядку. Но даты в файлах могут пересекаться.
#
# Написать программу, которая получает на входе начальную и конечную даты,
# и выдает все строчки из всех файлов, которые попадают в указанный интервал.
#
# Вывод должен происходить в порядке возрастания даты.
#
# Нужно написать тело функции parse_logs, при необходимости добавляя
# вспомогательные функции.

import argparse


def parse_logs(start, end):
    print(f"Reading logs from {start} to {end}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', default='20211120222223')
    parser.add_argument('--end', default='20211121153543')
    args = parser.parse_args()
    parse_logs(args.start, args.end)
