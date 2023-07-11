import logging
from logging.config import fileConfig

fileConfig("logging_config.ini")
logger = logging.getLogger()





def main():
    logger.debug(f"often makes a very good meal of {'visting tourists'}")


if __name__ == "__main__":
    main()