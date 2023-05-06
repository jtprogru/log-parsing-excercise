#!/usr/bin/env python3
"""
Тестовое задание для DevOps или SRE
"""


import argparse
import heapq
import os
import tracemalloc

LOG_PATH = "logs"


def walk_logs_dir(dir_path: str) -> list:
    """
    Get all content from dir_path
    """
    return os.listdir(dir_path)


def check_date_in_interval(start_date: str, end_date: str, log_line: str) -> bool:
    """
    Check date in interval start_date and end_date
    """
    if start_date <= log_line[0: len(start_date)] <= end_date:
        return True
    return False


def read_log_lines(file_path: str):
    """
    Read lines from log-file
    """
    with open(file_path, "r") as fr:
        for line in fr:
            yield line


def merge_logs(log_files: list):
    """
    Merge logs
    """
    log_generators = [read_log_lines(log_file) for log_file in log_files]
    return heapq.merge(*log_generators, key=lambda x: x[: len(args.start)])


def parse_logs(start, end):
    """
    Parse logs
    """
    log_files = walk_logs_dir(LOG_PATH)
    log_files = [os.path.join(LOG_PATH, log_file) for log_file in log_files]

    for line in merge_logs(log_files):
        if check_date_in_interval(start, end, line):
            print(line.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="20230507134335")
    parser.add_argument("--end", default="20230507144335")
    args = parser.parse_args()
    tracemalloc.start()
    parse_logs(args.start, args.end)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Current memory usage: {current / 1024:.3f} KiB")
    print(f"Peak memory usage: {peak / 1024:.3f} KiB")
