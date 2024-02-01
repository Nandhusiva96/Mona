import logging
def test_loggingdemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logging.log")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("some Error in this file ")
    logger.critical("Critical issue")