from util import s3
import os
from util.create_expected_wait_time_csv_file import create_expected_wait_time_csv_file
from typing import List, Tuple
import datetime
from algorithm.alg_util import wrapper_alg
from algorithm.alg_wada import IPSO
from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


def shape_dist(source: str) -> list[list[int]]:
    dist = []
    with open(source, 'r') as f:
        dist = f.read().split('\n')
    dist = [x.split(',') for x in dist][:-1]
    dist = [[int(x) for x in l] for l in dist]
    return dist


def alg_main(date: datetime.date) -> Tuple[List[int], int]:
    ipso = IPSO(16, 0.2, 0.3, display_flg=True)
    expected_wait_time_data = []
    try:
        expected_wait_time_data = s3.get_csv_file(
            'expected_wait_time_data/expected_wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    except:
        print('except except')
        print(date.day)
        expected_wait_time_data = create_expected_wait_time_csv_file(
            date.year, date.month, date.day)

        print(len(expected_wait_time_data))
        print(len(expected_wait_time_data[0]))
    finally:
        print(expected_wait_time_data)
        attractions_distances = s3.get_csv_file('attractions_dis.csv')
        return wrapper_alg(ipso, attractions_distances, expected_wait_time_data, True)