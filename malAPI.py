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
    list_url = settings.MAL_LIST_URL.format(user)

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

    watching_animes = res.json().get('anime')
    if not watching_animes:
        raise LoggedException(
            f'\"{user}\" not watching any anime',
            logf=logf, mod_name=__name__,
        )

    airing_anime = [
        anime for anime in watching_animes if anime['airing_status'] == 1
    ]

    if not airing_anime:
        raise LoggedException(
            f"\"{user}\" not watching any airing anime",
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

                _anime = {
                    'title': anime['title'],
                    'broadcast': _broadcast,
                    'aired': _aired,
                }
                _animes.append(_anime)
                util.log_to_file(
                    logf, info="INFO",
                    msg=f'''fetched data for "{anime['title']}" successfuly'''
                )
            except Exception:
                util.log_to_file(
                    logf, info="ERROR",
                    msg=f'''Failed fetching info on: "{anime['title']}"'''
                )

        util.log_to_file(
            logf, info="DEBUG",
            msg="Writing all fetched anime to json",
        )
        f.write(json.dumps(_animes))


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
                logf, info="DEBUG",
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
                logf, info="DEBUG",
                msg="Ending operations..."
            )

    print('ending...')
