import re
import os
import json
import requests
import datetime

from exceptions import LoggedException
import settings
import util


# TODO(rapha): proper modularization
def main(argv, *args, **kwargs):
    logf = kwargs.get('logf')
    user = argv.username
    list_url = settings.MAL_LIST_AIRING_URL.format(user)

    util.log_to_file(
        logf, info="DEBUG",
        msg=f"fetching MAL anime list of {user}"
    )

    res = requests.get(list_url)
    if not res:
        raise LoggedException(
            f"User not found: \"{user}\"",
            logf=logf, info="FATAL", mod_name=__name__,
        )

    airing_anime = res.json().get('anime')
    if not airing_anime:
        raise LoggedException(
            f'no airing anime in "{user}"\'s list',
            logf=logf, mod_name=__name__,
        )

    broadcast_pattern = (
        r'<span.+Broadcast:.+\s+(?:(?P<other>Unknown)|(?P<weekday>\w+) '
        r'at (?P<time>\d\d:\d\d)..(?P<timezone>\w{3}))'
    )
    aired_ptrn = (
        r'<span.*Aired:.*\s+(?:(?P<from>.*)(?: to (?P<to>.*))|'
        r'(?P<other>\?|Not available|\d\d\d\d))'
    )

    util.log_to_file(
        logf, info="INFO",
        msg=f'''fetching {len(airing_anime)} airing anime for "{user}"...'''
    )
    # TODO(rapha): make better serailization/persistency
    with open(f'out/{user}_airing_watching.json', 'w') as f:
        _animes = []
        for anime in airing_anime:
            try:
                page = requests.get(anime['url'])

                # TODO(rapha): delegate pattern matching to async task
                broadcast_match = re.search(broadcast_pattern, page.text)
                aired_match = re.search(aired_ptrn, page.text)

                if (
                    not broadcast_match or
                    broadcast_match.groupdict().get('other')
                ):
                    _broadcast = None
                    util.log_to_file(
                        logf, info="WARN",
                        msg="No \"broadcast\" info found "
                            f"for \"{anime['title']}\""
                    )
                else:
                    _broadcast = {
                        'weekday': broadcast_match.groupdict().get('weekday'),
                        'time': broadcast_match.groupdict().get('time'),
                        'timezone': broadcast_match.groupdict().get('timezone')
                    }

                if not aired_match or aired_match.groupdict().get('other'):
                    _aired = None
                    util.log_to_file(
                        logf, info="WARN",
                        msg=f"No \"aired\" info found for \"{anime['title']}\""
                    )
                else:
                    _aired = {
                        'from': aired_match.groupdict().get('from'),
                        'to': aired_match.groupdict().get('to'),
                    }

                _datetime = datetime.datetime.strptime(
                    _aired['from'] + _broadcast['time'],
                    '%b %d, %Y%H:%M'
                )
                _datetime -= datetime.timedelta(hours=12)

                _pweekday = _broadcast['weekday']
                _pweekday = util.weekday_to_int(_pweekday, logf)
                _time = dict(
                    weekday=(
                        _pweekday
                        if _pweekday != -1
                        else _datetime.weekday()
                    ),
                    hour=_datetime.hour,
                    minute=_datetime.minute,
                )

                _anime = {
                    'title': anime['title'],
                    'time': _time
                }
                _animes.append(_anime)
                util.log_to_file(
                    logf, info="INFO",
                    msg=f'''fetched data for "{anime['title']}" successfuly'''
                )
                util.log_to_file(
                    logf, info='DEBUG',
                    msg=(
                        f"\"{anime['title']}\" aired: {_aired},"
                        f" broadcast: {_broadcast}, "
                        f"time: {_time}"
                    )
                )
            except Exception:
                util.log_to_file(
                    logf, info="ERROR",
                    msg=(
                        "Failed fetching/building info on: "
                        f"\"{anime['title']}\""
                    )
                )

        util.log_to_file(
            logf, info="DEBUG",
            msg="Writing all fetched anime to json",
        )
        _animes.sort(
            key=lambda anime: (
                anime['time'].get('weekday'),
                anime['time'].get('hour'),
                anime['time'].get('minute'),
            )
        )
        f.write(json.dumps(_animes, indent=4))


# TODO(rapha): proper entry point + arg passing
# TODO(rapha): proper async pipeline
if __name__ == '__main__':
    argv = util.parse_args()
    now = datetime.datetime.now()

    # creating dirs for outputing and logging
    if not os.path.exists('logs'):
        os.makedirs('logs')
    if not os.path.exists('out'):
        os.makedirs('out')

    with open(f'logs/{str(now.date())}.log', 'a') as logf:
        try:
            util.log_to_file(
                logf, info="INFO",
                msg="Beggining operations..."
            )
            main(argv, logf=logf)
        except LoggedException as le:
            util.log_to_file(
                logf, info="FATAL", mod_name=__name__,
                msg=f"Managed Exception logged in \"main\": {str(le)}"
            )
        finally:
            util.log_to_file(
                logf, info="INFO",
                msg="Ending operations..."
            )

    print('ending...')
