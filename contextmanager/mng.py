from typing import TextIO
import logging
import traceback


class LogManager:
    def __init__(self, level: logging, log_name='file'):
        logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d%Y %H: %M: %S')
        self.__logger = logging.getLogger(__name__)
        self.__stream_h = logging.StreamHandler()
        self.__file_h = logging.FileHandler(f'{log_name}.log')
        self.__logger.addHandler(self.__stream_h)
        self.__logger.addHandler(self.__file_h)

        self.level = level

    def __enter__(self) -> logging:
        self.__logger.debug("Entering Program Manager")

        return self.__logger

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        del self.__logger
        del self.__stream_h
        del self.__file_h
