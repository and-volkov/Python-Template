import os

import pydantic
from dotenv import load_dotenv

load_dotenv()


class BaseSettings(pydantic.BaseSettings):

    class Config:
        case_sensitive = True
        env_file = ".env.example"
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
            "filename": log_config.FILE_PATH + os.sep + log_config.FILE_NAME,
            "class": "logging.handlers.RotatingFileHandler",
            "mode": "a",
            "maxBytes": log_config.MAX_FILE_SIZE,
            "backupCount": log_config.BACKUP_COUNT,
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False
        },
        "__main__": {  # if __name__ == "__main__"
            "handlers": ["default", "fileHandler"],
            "level": "DEBUG",
            "propagate": False
        },
    }
}
