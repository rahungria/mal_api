import util
from io import TextIOWrapper


class LoggedException (Exception):
    '''
    base exception for this application
    properly logs any and all exceptions
    defaults level to ERROR
    '''
    def __init__(
        self, *args: object, logf: TextIOWrapper, mod_name: str,
        custom_msg=" ", info="ERROR"
    ):
        util.log_to_file(
            logf, info=info,
            msg=f'Exception in "{mod_name}": '
                f"{self.with_traceback(self.__traceback__)}. {custom_msg}"
        )
        super().__init__(*args)
