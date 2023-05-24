import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env.example"
        env_file_encoding = "utf-8"


class LogConfig(BaseSettings):
    name: str = "NAME"
    format: str = "FORMAT"
    level: str = "LEVEL"
    path: str = "PATH"
    date_format: str = "DATE_FORMAT"

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "format": format,
            "datefmt": date_format,
        },
        "fileFormatter": {
            "format": format,
            "datefmt": date_format,
            "class": "logging.Formatter",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "fileHandler": {
            "level": "ERROR",
            "formatter": "fileFormatter",
            "filename": path + name,
            "class": "logging.handlers.RotatingFileHandler",
            "mode": "a",
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 5,
            "delay": 0,
            "encoding": "utf-8",
        },
    }
    loggers = {
        name: {
            "handlers": ["default", "fileHandler"],
            "level": level,
        },
    }

    env_prefix = "LOG_"
