import logging
import pandas as pd
import sys
import numpy as np
import phonenumbers as pn
import csv
import os
import re

# if lbl == l[0], lbl = l[1]
LABEL_REPLACEMENTS = [
    ('Agent Writing Contract Start Date (Carrier appointment start date)',
     'Agent Writing Contract Start Date'),
    ('Agent Writing Contract Status (actually active and cancelled\'s should come in two different files',
     'Agent Writing Contract Status')
]
LST_FILE = 'data/NYL.lst'


def get_data_filenames():
    file_names = [f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]
    return [f for f in file_names if re.search('NYL_FieldAgent_[0-9]{8}.csv' is not None, f)]


def str_get_int(s):
    start = None
    end = None
    index = 0
    for ch in s:
        try:
            int(ch)
        except ValueError:
            if start:
                end = index
                break
        else:
            if not start:
                start = index
        finally:
            index += 1
    return int(s[start:end+1])


def get_file_length(file_name):
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        row_count = sum(1 for row in reader)
    return row_count


def check_already_processed(date):
    with open(LST_FILE) as file:
        rows = file.readlines()
    for d in rows:
        if d == date:
            return True
    return False


def replace_labels(data_frame):
    d = {}
    for rep in LABEL_REPLACEMENTS:
        d[rep[0]] = rep[1]
    data_frame.rename(columns=d)


def validate_email(email):
    regex_pattern = """^[a-z0-9]+[\\.]?[a-z0-9]+[@]\\w+[.]\\w+$"""
    ret = re.search(regex_pattern, email)
    return ret is not None


def process_file(file_name):
    df = pd.read_csv(file_name)


def main():
    fileNames = get_data_filenames()
    fileNames.sort(key=str_get_int)
    print(fileNames)


if __name__ == '__main__':
    main()
