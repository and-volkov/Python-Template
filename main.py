import logging
from logging.config import dictConfig

from dotenv import load_dotenv

from settings import LogConfig

load_dotenv()

dictConfig(LogConfig().dict())
logger = logging.getLogger(LogConfig().name)
