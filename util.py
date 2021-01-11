'''
place for all utility methods
'''

import datetime
import argparse

from io import TextIOWrapper


# TODO(rapha): make thread safe logger class
def log_to_file(file: TextIOWrapper, msg: str, info: str = "DEBUG"):
    file.write(
        f'[{datetime.datetime.now().strftime("%x %X.%f")} {info}] {msg}\n'
    )
    file.flush()


def parse_args():
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument(
        'username', type=str,
        help="name of the MAL user to find anime info of",
    )

    args = parser.parse_args()
    # checking / default values

    return args
