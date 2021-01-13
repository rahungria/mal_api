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


def weekday_to_int(weekday, logf):
    if weekday[-1] == "s":
        weekday = weekday[:-1]

    value = -1
    if weekday == "Monday":
        value = 0
    elif weekday == "Tuesday":
        value = 1
    elif weekday == "Wednesday":
        value = 2
    elif weekday == "Thursday":
        value = 3
    elif weekday == "Friday":
        value = 4
    elif weekday == "Saturday":
        value = 5
    elif weekday == "Sunday":
        value = 6

    log_to_file(
        logf, info="DEBUG",
        msg=f"parsing \"{weekday}\" to {value}"
    )
    return value
