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
import os

LOG_PATH = 'logs'
CONTENT = []
TMP = []


def walk_logs_dir(dir_path: str) -> list:
    return os.listdir(dir_path)


def read_log_content(file_path: str) -> None:
    global CONTENT
    with open(file_path, 'r') as fr:
        CONTENT.extend(fr.readlines())


def check_date_in_interval(start_date: str, end_date: str, log_line: str) -> bool:
    if start_date <= log_line[0:len(start_date)] <= end_date:
        return True
    return False


def parse_logs(start, end):
    global CONTENT
    files_list = walk_logs_dir(LOG_PATH)
    for file_name in files_list:
        read_log_content(LOG_PATH + '/' + file_name)
    CONTENT = sorted(CONTENT)
    print(f"Reading logs from {start} to {end}")
    for line in CONTENT:
        if check_date_in_interval(start_date=start, end_date=end, log_line=line):
            print(str(line))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', default='20211120222223')
    parser.add_argument('--end', default='20211121153543')
    args = parser.parse_args()
    parse_logs(args.start, args.end)
