import logging
from logging.config import dictConfig

from dotenv import load_dotenv

from settings import LOGGING_CONFIG

load_dotenv()

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def logs():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")


if __name__ == "__main__":
    logs()
