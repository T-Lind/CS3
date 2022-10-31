import functools
import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d%Y %H: %M: %S')


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        result = func(*args, **kwargs)
        logging.debug(f'{func.__name__!r} returned {result!r}')
        return result

    return wrapper


def setup_logger(logger: logging.Logger):
    # Create a handler
    stream_h = logging.StreamHandler()
    file_h = logging.FileHandler('file.log')

    # Set level and format of the file log
    stream_h.setLevel(logging.WARNING)
    file_h.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_h.setFormatter(formatter)
    file_h.setFormatter(formatter)

    logger.addHandler(stream_h)
    logger.addHandler(file_h)


class CountCalls:  # Documentation example below using multi line strings
    """
    A class decorator to count the number of calls a function has been run through.
    """

    def __init__(self, func):
        """
        Init function to assign a function (called indirectly with a decorator)
        :param func: The input function
        """
        self.func = func
        self.num_calls = 0
        self.__name__ = "CountCalls"

    def __call__(self, *args, **kwargs):
        """
        The function to execute when the class is called
        :param args: Arguments of the input function
        :param kwargs: Keyword arguments of the input function
        :return: The function which has run
        """
        self.num_calls += 1
        logging.debug(f'{self.func.__name__} has executed {self.num_calls} time(s).')
        return self.func(*args, **kwargs)
