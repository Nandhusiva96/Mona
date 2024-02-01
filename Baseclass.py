import inspect
import logging


class Baseclass:
    def getlogger(self):
        LoggerName = inspect.stack()[1][3]
        logger = logging.getLogger(LoggerName)
        fileHandler = logging.FileHandler("logging.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger