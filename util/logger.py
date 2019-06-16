from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG


class Logger:

    def __init__(self, name=__name__):
        # pass
        self.logger = getLogger(name)
        self.logger.setLevel(DEBUG)
        formatter = Formatter(
            "[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

        # stdout
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # file
        handler = handlers.RotatingFileHandler(filename='your_log_path.log',
                                               maxBytes=1048576,
                                               backupCount=3)
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)
        # pass

    def info(self, msg):
        self.logger.info(msg)
        # pass

    def warn(self, msg):
        self.logger.warning(msg)
        # pass

    def error(self, msg):
        self.logger.error(msg)
        # pass

    def critical(self, msg):
        self.logger.critical(msg)
        # pass
