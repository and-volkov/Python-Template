import os

import pydantic_settings
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseSettings(pydantic_settings.BaseSettings):
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


class LogConfig(BaseSettings):
    FILE_NAME: str = "FILE_NAME"
    FILE_PATH: str = "PATH"
    MESSAGE_FORMAT: str = "FORMAT"
    DATE_FORMAT: str = "DATE_FORMAT"
    MAX_FILE_SIZE: int = 5 * 1024 * 1024
    BACKUP_COUNT: int = 5

    class Config:
        env_prefix = "LOG_"


log_config = LogConfig()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": log_config.MESSAGE_FORMAT,
            "datefmt": log_config.DATE_FORMAT,
            "class": "logging.Formatter",
        },
        "fileFormatter": {
            "format": log_config.MESSAGE_FORMAT,
            "datefmt": log_config.DATE_FORMAT,
            "class": "logging.Formatter",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "fileHandler": {
            "formatter": "fileFormatter",
            "filename": os.path.join(
                BASE_DIR, log_config.FILE_PATH, log_config.FILE_NAME
            ),
            "class": "logging.handlers.RotatingFileHandler",
            "mode": "a",
            "maxBytes": log_config.MAX_FILE_SIZE,
            "backupCount": log_config.BACKUP_COUNT,
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default", "fileHandler"],
            "level": "INFO",
            "propagate": False,
        },
        "__main__": {  # if __name__ == "__main__"
            "handlers": ["default", "fileHandler"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
